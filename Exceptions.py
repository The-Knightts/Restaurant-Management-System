# exceptions.py
class CustomException(Exception):
    pass

class InvalidMenuItemError(CustomException):
    pass

class InsufficientQuantityError(CustomException):
    pass