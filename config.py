from enum import Enum


URL = 'https://stellarburgers.nomoreparties.site/api/'


class ENDPOINT(str, Enum):
    CREATE_USER = "auth/register"
    LOGIN = "auth/login"
    User = "auth/user"


class ERROR(str, Enum):
    MISSING_PARAMETER = "Email, password and name are required fields"
    USER_EXIST = "User already exists"
    INCORRECT_AUTHORIZATION_DATA = "email or password are incorrect"
    USER_NOT_AUTHORIZED = "You should be authorised"
