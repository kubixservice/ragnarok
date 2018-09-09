from django.db import models
from django.contrib.auth.models import User

from alfheimproject.settings import SECRETS


class DonationsLog(models.Model):
    PAYMENT_SYSTEMS = (
        (1, 'Paypal'),
        (2, 'Yandex.Money'),
        (3, 'Unitpay')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255)
    payer_id = models.CharField(max_length=255, default='')
    payment_system = models.IntegerField(choices=PAYMENT_SYSTEMS)
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)
    execute_url = models.CharField(max_length=255, default='')
    approval_url = models.CharField(max_length=255, default='')
    excecuted = models.BooleanField(default=False)

    class Meta:
        db_table = '{prefix}donations_log'.format(prefix=SECRETS['table_prefix'])
        verbose_name = 'Donation Log'
        verbose_name_plural = 'Donations Log'
