from rest_framework.serializers import ValidationError


def change_debt(value):
    """Нельзя изменять сумму задолженности"""
    if value is not None:
        raise ValidationError("Нельзя изменять сумму задолженности!")
