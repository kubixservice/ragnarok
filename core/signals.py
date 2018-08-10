from django.core.mail import send_mail
from django.template.loader import render_to_string

from rest_framework.reverse import reverse

from alfheimproject.settings import CONFIG, SECRETS


def send_account_verification(sender, instance, **kwargs):
    html_msg = render_to_string('email_verification.html', {
        'server_name': CONFIG['server']['conf']['server_name'],
        'username': instance.user.username,
        'email': instance.user.email,
        'staff_email': SECRETS['smtp']['email_host_user'],
        'creation_date': instance.created_date,
        'verify_url': '{domain}{url}?verify={token}'.format(
            domain=CONFIG['server']['conf']['server_domain'],
            url=reverse('master_account'),
            token=instance.token
        )
    })
    send_mail(
        subject=CONFIG['emails']['default_subject'].format(server_name=CONFIG['server']['conf']['server_name']),
        message=CONFIG['emails']['default_message'].format(server_name=CONFIG['server']['conf']['server_name'],
                                                           user=instance.user.username),
        from_email=SECRETS['smtp']['email_host_user'],
        recipient_list=[instance.user.email],
        html_message=html_msg
    )
