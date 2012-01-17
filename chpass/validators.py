from django.core.exceptions import ValidationError

def validate_password(value):
    if len(value) < 8:
        raise ValidationError("Password must be longer than 8 characters")