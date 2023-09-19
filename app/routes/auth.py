from flask import Blueprint
from flask import request
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity
from app.services import AuthService

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    return AuthService.register(data)


@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    return AuthService.login(data)


class AuthRoute(Blueprint):
    def __init__(self, name, url_prefix):
        self.name = name
        self.url_prefix = url_prefix
        self.bp = Blueprint(self.name, __name__, url_prefix=self.url_prefix)

        @self.bp.route('/register', methods=['POST'])
        def register_user():
            data = request.json
            return AuthService.register(data)

        @self.bp.route('/login', methods=['POST'])
        def login():
            data = request.json
            return AuthService.login(data)

        @self.bp.route('/my-profile', methods=['GET'])
        @jwt_required()
        def profile():
            current_user = get_jwt_identity()
            return AuthService.profile(pk=current_user.get("id"))
