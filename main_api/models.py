from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save, post_save

from core.signals import send_account_verification

from alfheimproject.settings import SECRETS

User = get_user_model()


class MasterAccount(AbstractUser):
    pass


class UserVerification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='verification',
        verbose_name='Master account'
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
        default=True,
        verbose_name='Is token available?'
    )

    class Meta:
        db_table = '{prefix}user_verification'.format(prefix=SECRETS['table_prefix'])
        verbose_name = 'E-Mail Verification'
        verbose_name_plural = 'E-Mail Verifications'

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


class UserProfile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Master account'
    )
    balance = models.IntegerField(
        default=0,
        verbose_name='Account balance',
    )

    class Meta:
        db_table = '{prefix}user_profile'.format(prefix=SECRETS['table_prefix'])

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, **kwargs):
    if kwargs.get('created'):
        UserProfile.objects.create(
            user=instance
        )


pre_save.connect(send_account_verification, sender=UserVerification)
post_save.connect(create_user_profile, sender=User)
