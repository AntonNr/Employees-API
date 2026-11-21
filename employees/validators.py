from django.core.exceptions import ValidationError

def validate_not_only_digits(value: str):
    if value.isdigit():
        raise ValidationError(("String cannot contain only digits"))

def validate_has_letter(value: str):
    if not any(char.isalpha() for char in value):
        raise ValidationError("Value must contain at least one letter")