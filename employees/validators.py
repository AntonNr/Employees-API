from django.core.exceptions import ValidationError

def validate_not_only_digits(value: str):
    if value.isdigit():
        raise ValidationError(("String cannot contain only digits"))