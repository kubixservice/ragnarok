import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MaximumLengthValidator:
    def __init__(self, max_length=8):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                _("This password length must not exceed %(max_length)d characters."),
                code='password_too_long',
                params={'max_length': self.max_length},
            )

    def get_help_text(self):
        return _(
            "Your password length must not exceed %(max_length)d characters."
            % {'max_length': self.max_length}
        )


class MinimumLengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("This password must contain at least %(min_length)d characters."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_length)d characters."
            % {'min_length': self.min_length}
        )


class MinimumNumberValidator:
    def __init__(self, min_num=0):
        self.min_num = min_num

    def validate(self, password, user=None):
        if self.min_num > 0:
            num = sum(1 for c in password if c.isnumeric())
            if num < self.min_num:
                raise ValidationError(
                    _("This password must contain at least %(min_num)d numbers."),
                    code='password_numbers_not_enough',
                    params={'min_num': self.min_num},
                )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_num)d numbers."
            % {'min_num': self.min_num}
        )


class MinimumUpperValidator:
    def __init__(self, min_upper=0):
        self.min_upper = min_upper

    def validate(self, password, user=None):
        if self.min_upper > 0:
            num = sum(1 for c in password if c.isupper())
            if num < self.min_upper:
                raise ValidationError(
                    _("This password must contain at least %(min_upper)d uppercase characters."),
                    code='password_upper_not_enough',
                    params={'min_upper': self.min_upper},
                )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_upper)d uppercase characters."
            % {'min_upper': self.min_upper}
        )


class MinimumLowerValidator:
    def __init__(self, min_lower=0):
        self.min_lower = min_lower

    def validate(self, password, user=None):
        if self.min_lower > 0:
            num = sum(1 for c in password if c.islower())
            if num < self.min_lower:
                raise ValidationError(
                    _("This password must contain at least %(min_lower)d lowercase characters."),
                    code='password_lower_not_enough',
                    params={'min_lower': self.min_lower},
                )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_lower)d lowercase characters."
            % {'min_lower': self.min_lower}
        )


class MinimumSymbolValidator:
    def __init__(self, min_symbol=0):
        self.min_symbol = min_symbol

    def validate(self, password, user=None):
        if self.min_symbol > 0:
            match = re.sub('[^^&!@#%(){}[\]*$]+', '', password)
            num = len(match)
            if num < self.min_symbol:
                raise ValidationError(
                    _("This password must contain at least %(min_symbol)d symbols."),
                    code='password_symbols_not_enough',
                    params={'min_symbol': self.min_symbol},
                )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_symbol)d symbols."
            % {'min_symbol': self.min_symbol}
        )
