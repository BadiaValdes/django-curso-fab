from django.core.exceptions import ValidationError
from ..auxiliar.constants import length_error


def validate_length(field, max_length, min_length):
    def inner_fn(value):
        if len(value) > max_length:
            raise ValidationError(length_error(field, max_length, True))
        elif len(value) < min_length:
            raise ValidationError(length_error(field, min_length, False))
    return inner_fn
