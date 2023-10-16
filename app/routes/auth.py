from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity
from app.services import AuthService

auth_blueprint = Blueprint('auth', __name__)


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

        @self.bp.route('/update-my-profile', methods=['POST'])
        @jwt_required()
        def update_profile():
            current_user = get_jwt_identity()
            data = request.json
            user_id = current_user.get("id")
            return jsonify(AuthService.update_profile(pk=user_id, data=data))
