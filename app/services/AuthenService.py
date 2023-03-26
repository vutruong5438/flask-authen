from flask import jsonify
from models import User


class AuthenService:

    @staticmethod
    def register(data):
        email = data.get("email")
        exist_user = User.get_by_email(email=email)
        password = data.get("password")
        if exist_user:
            return jsonify(message='That email already exists'), 409
        try:
            user = User(email=email, password=password).save()
        except Exception as e:
            return jsonify(message=e.message), 409
        return {'user_id': user.id}

    @staticmethod
    def login(data):
        return True
