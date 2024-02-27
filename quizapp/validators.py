from django.core.exceptions import ValidationError


def validate_difficulty_question(value):
    if not value.isdigit():
        raise ValidationError('Qiyinlik darajasi 1 dan 4 gacha bo\'lgan qiymatlarda kiritiladi')
    if value < 1 or value > 4:
        raise ValidationError('Qiyinlik darajasi 1 dan 4 gacha bo\'lgan qiymatlarda kiritiladi')
    return value

