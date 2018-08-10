from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

from core.signals import send_account_verification

from alfheimproject.settings import SECRETS


class UserVerification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='verification'
    )
    token = models.CharField(
        max_length=255,
        unique=True,
        null=False
    )
    expiration_date = models.DateField()
    created_date = models.DateField(
        auto_now=True
    )
    is_available = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = '{prefix}user_verification'.format(prefix=SECRETS['table_prefix'])

    def __str__(self):
        return self.user.username


class ServerHighestPeak(models.Model):
    peak = models.IntegerField(
        default=0
    )
    peak_date = models.DateField(
        auto_now=True
    )

    class Meta:
        db_table = '{prefix}highest_peak'.format(prefix=SECRETS['table_prefix'])

    def __str__(self):
        return '{peak} - {date}'.format(peak=self.peak, date=self.peak_date)


pre_save.connect(send_account_verification, sender=UserVerification)
