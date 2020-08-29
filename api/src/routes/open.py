from flask import Blueprint, request, make_response, abort
from src.auth import connect as conn
from src.models.request_type import Req
from src.interfaces.open_interface import SQL

open_routes = Blueprint('open_routes', __name__)


@open_routes.route("/test", methods=['GET'])
def test():
    return make_response('Connection OK', 200)


@open_routes.route("/get_user/", methods=['GET'])
def get_user():
    if request.args.get('id'):
        id = request.args.get('id')
        query = SQL(Req.GET_USER_BY_ID, request.args.get('id'))
        res = conn.execute(query, id)
    else:
        query = SQL(request_type=Req.GET_ALL_USERS)
        res = conn.execute(query)

    return make_response(res, 200)


@open_routes.route("/abort", methods=['GET'])
def get_abort():
    return abort(404)




