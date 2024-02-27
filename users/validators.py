from django.core.exceptions import ValidationError


def check_phone_number(value: str):
    if len(value) != 13:
        raise ValidationError('Telefon raqam uzunligi 13 ta '
                              'belgi bo\'lishi va +998 dan '
                              'boshlanishi kerak')
    if not value.startswith("+998"):
        raise ValidationError('Telefon raqam +998 dan boshlanishi kerak')
    return value
