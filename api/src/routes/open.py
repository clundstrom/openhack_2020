from flask import Blueprint
from src.auth import connect as conn
open_routes = Blueprint('open_routes', __name__)


@open_routes.route("/test")
def test():
   val = conn.execute('SELECT * FROM general.users')
   return val

