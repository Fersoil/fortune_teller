import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext


class UppercaseValidator(object):
    '''The password must contain at least 1 uppercase letter, A-Z.'''

    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                gettext("The password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return gettext(
            "Your password must contain at least 1 uppercase letter, A-Z."
        )
