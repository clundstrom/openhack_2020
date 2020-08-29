from enum import Enum


class Req(Enum):
    GET_ALL_USERS = 1
    GET_USER = 2
    GET_USER_BY_ID = 3
    GET_LOGIN = 4
    POST_REGISTER_USER = 5
    GET_USER_BY_NAME = 6

