from flask import Blueprint, request, make_response, abort
from auth.auth import authenticate
from src.auth import connect as conn
from src.interfaces.open_interface import sql
from src.auth import auth
import uuid

open_routes = Blueprint('open_routes', __name__)


@open_routes.route("/test", methods=['GET'])
def test():
    response = {"message": "Connection OK"}
    return make_response(response, 200)


@open_routes.route("/test_auth", methods=['GET'])
@authenticate
def test_auth():
    response = {"message": "Authorized"}
    return make_response(response, 200)


@open_routes.route("/get_user/", methods=['GET'])
def get_user():
    if request.args.get('id'):
        id = request.args.get('id')
        query = sql('GET_USER_BY_ID', request.args.get('id'))
        res = conn.execute(query, id)
    else:
        query = sql(request_type='GET_ALL_USERS')
        res = conn.execute(query)

    return make_response(res, 200)


@open_routes.route("/abort", methods=['GET'])
def get_abort():
    return abort(404)


@open_routes.route("/register", methods=['POST'])
def register():
    data = request.json
    if data.get('username') and data.get('password'):
        query = sql('GET_USER_BY_NAME', data.get('username'))
        res = conn.execute(query, data.get('username'))

        if len(res.json) != 1:
            hash = auth.hash_password(password=data.get('password'))
            query = sql('POST_REGISTER_USER', data.get('username'), hash)
            conn.execute(query, data.get('username'), hash)
        else:
            abort(400, 'Username taken.')

    else:
        return abort(400)

    response = {"message": "Registration successful"}
    return make_response(response, 200)


@open_routes.route("/login", methods=['GET'])
def login():
    data = request.json

    if data.get('username') and data.get('password'):
        query = sql('GET_USER_BY_NAME', data.get('username'))
        user = conn.execute(query, data.get('username')).json
        if not user:
            return make_response('No such user.', 200)
        user = user[0]
        if auth.is_valid_login(data.get('password'), user[2]):
            token = uuid.uuid4().hex
            query = sql('POST_UPDATE_TOKEN')
            conn.execute(query, token, user[0])
            user = {"username": user[1],
                    "token": token
                    }
            return make_response(user, 200)

        else:
            response = {"message": "Access denied"}
            return make_response(response, 401)
    return abort(400)
