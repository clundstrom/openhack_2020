from flask import Blueprint, request, make_response, abort
from src.auth import connect as conn
from src.models.request_type import Req
from src.interfaces.open_interface import sql
from src.auth import auth

open_routes = Blueprint('open_routes', __name__)


@open_routes.route("/test", methods=['GET'])
def test():
    return make_response('Connection OK', 200)


@open_routes.route("/get_user/", methods=['GET'])
def get_user():
    if request.args.get('id'):
        id = request.args.get('id')
        query = sql(Req.GET_USER_BY_ID, request.args.get('id'))
        res = conn.execute(query, id)
    else:
        query = sql(request_type=Req.GET_ALL_USERS)
        res = conn.execute(query)

    return make_response(res, 200)


@open_routes.route("/abort", methods=['GET'])
def get_abort():
    return abort(404) @ open_routes.route("/abort", methods=['GET'])


@open_routes.route("/register", methods=['POST'])
def register():
    data = request.json
    if data['username'] and data['password']:
        query = sql(Req.GET_USER_BY_NAME, data['username'])
        res = conn.execute(query, data['username'])

        if len(res.json) != 1:
            hash = auth.hash_password(password=data['password'])
            query = sql(Req.POST_REGISTER_USER, data['username'], hash)
            res = conn.execute(query, data['username'], hash)
        else:
            abort(400, 'Username taken.')

    else:
        return make_response('Bad request', 400)

    return res
