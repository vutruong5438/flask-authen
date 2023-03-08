from flask import jsonify
from flask import Blueprint
from flask import request
from services import AuthenService


# auth_blueprint = Blueprint('auth', __name__)
#
#
# @auth_blueprint.route('/register', methods=['POST'])
# def register():
#     data = request.json


class AuthenRoute(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        @self.route('/register', methods=['POST'])
        def index():
            data = request.json
            return AuthenService.register(data)