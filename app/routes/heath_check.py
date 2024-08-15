from flask import Blueprint, jsonify


auth_blueprint = Blueprint('auth', __name__)


class HealthCheck(Blueprint):
    def __init__(self, name, url_prefix):
        self.name = name
        self.url_prefix = url_prefix
        self.bp = Blueprint(self.name, __name__, url_prefix=self.url_prefix)

        @self.bp.route('/ping', methods=["GET"])
        def ping():
            return jsonify("pong!")
