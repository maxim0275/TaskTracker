import re

from rest_framework.serializers import ValidationError


class NameValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile(r"^[а-яА-Яa-zA-Z0-9\.\-\,\ ]")
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError(
                "В поле возможны только буквы, цифры, запятая, точка, тире, пробел.")
