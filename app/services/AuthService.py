from flask import jsonify
from app.models import User, UserProfile
from app.services import UserService
from flask_jwt_extended import create_access_token, jwt_required


class AuthService:

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """

        payload = {
            "id": user_id
        }
        return create_access_token(payload)

    @classmethod
    def register(cls, data):
        email = data.get("email")
        password = data.get("password")
        exist_user = User.get_by_email(email)
        if exist_user:
            return jsonify(message='That email already exists'), 409
        try:
            user = UserService.create_user(data)
        except Exception as e:
            return jsonify(message=e), 409
        return {'user_id': user.id}

    @classmethod
    def login(cls, data):
        email = data.get("email")
        password = data.get("password")
        exist_user = User.get_by_email(email)
        if exist_user and exist_user.check_password_hash(exist_user.password_hash, password):
            return {"token": cls.encode_auth_token(exist_user.id)}
        else:
            return jsonify(message='Try again'), 500

    @classmethod
    def profile(cls, pk):
        profile = UserProfile.get_by_user_id(pk)
        return profile.as_dict()
