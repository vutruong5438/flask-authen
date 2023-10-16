from flask import request, Blueprint, jsonify
from app.services import ProductService


class ProductRoute(Blueprint):
    def __init__(self, name, url_prefix):
        self.name = name
        self.url_prefix = url_prefix
        self.bp = Blueprint(self.name, __name__, url_prefix=self.url_prefix)

        @self.bp.route("/", methods=["POST"])
        def create():
            data = request.json
            product = ProductService.create(**data)
            return product.as_dict()

        @self.bp.route("/<product_id>", methods=["GET"])
        def retrieve(product_id):
            product = ProductService.load(product_id)
            return product.as_dict()

        @self.bp.route("/<product_id>", methods=["PUT"])
        def update(product_id):
            data = request.json
            product = ProductService.update(product_id, **data)
            return product.as_dict()

        @self.bp.route("/", methods=["GET"])
        def list():
            products_data = []
            products = ProductService.list()
            for product in products:
                products_data.append(product.as_dict())
            return jsonify(products_data)
