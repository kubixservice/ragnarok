import datetime
import paypalrestsdk

from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from django.urls import reverse

from . import serializers
from . import models
from main_api.models import UserProfile

from alfheimproject.settings import DONATIONS, CONFIG


class PayPalCreatePaymentViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        data = request.data
        approvalurl = executeurl = ''
        response = None
        serializer = serializers.DonationSerializer(data=data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            points = serializer.validated_data['points']
            payment = paypalrestsdk.Payment({
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal"
                },
                "redirect_urls": {
                    "return_url": DONATIONS['paypal']['redirect_url'].format(
                        domain=CONFIG['server']['conf']['server_domain'],
                        reversed_for_view=reverse('paypal_execute')),
                    "cancel_url": DONATIONS['paypal']['cancel_url'].format(
                        domain=CONFIG['server']['conf']['server_domain'],
                        reversed_for_view=reverse('paypal_execute'))
                },
                "transactions": [{
                    "item_list": {
                        "items": [{
                            "name": "item",
                            "sku": "item",
                            "price": "{price:.2f}".format(price=amount),
                            "currency": "USD",
                            "quantity": 1  # switch to {points}
                        }]
                    },
                    "amount": {
                        "total": "{total:.2f}".format(total=amount),
                        "currency": "USD"
                    },
                    "description": DONATIONS['paypal']['description'].format(points=points, amount=amount,
                                                                             currency=DONATIONS['paypal']['currency'])
                }]
            })

            if payment.create():
                for link in payment.links:
                    if link.method == "REDIRECT":
                        approvalurl = link.href
                    if link.method == "POST":
                        executeurl = link.href

                models.DonationsLog.objects.create(
                    user=self.request.user,
                    payment_id=payment['id'],
                    approval_url=approvalurl,
                    execute_url=executeurl,
                    amount=amount,
                    payment_system=1
                )

                for link in payment.links:
                    if link.method == "REDIRECT":
                        redirect_url = str(link.href)
                        return Response(data=redirect_url, status=status.HTTP_200_OK)
            else:
                response = payment.error
        else:
            response = serializer.errors
        return Response(data=response, status=status.HTTP_200_OK)


class PayPalExecutePaymentViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request):
        data = request.query_params
        try:
            payment_id = data['paymentId']
            payer_id = data['PayerID']
        except KeyError:
            return Response(data='Could not find variables', status=status.HTTP_400_BAD_REQUEST)

        payment_log = models.DonationsLog.objects.get(payment_id=payment_id)
        payment = paypalrestsdk.Payment.find(payment_id)
        if payment.execute({'payer_id': payer_id}):
            payment_log.payer_id = payer_id
            payment_log.update_date = datetime.datetime.now()
            payment_log.executed = True
            payment_log.save()
            user = UserProfile.objects.get(user=payment_log.user)
            user.balance += payment_log.amount
            user.save()
            response = 'OK'
        else:
            response = payment.error
        return Response(data=response, status=status.HTTP_200_OK)
