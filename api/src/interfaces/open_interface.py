from src.models.request_type import Req


def SQL(request_type, *args):
    """
    Composes queries based on type of request.
    """

    query = ''

    if request_type == Req.GET_ALL_USERS:
        query = """ SELECT * FROM users"""

    elif request_type == Req.GET_USER_BY_ID:
        query = """SELECT * FROM users where id = %s"""

    return query