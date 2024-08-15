from flask import request, Blueprint, jsonify
from app.base import BaseView
from app.services import ProductService


class ProductView(BaseView):

    def get_list(self):
        products_data = []
        products = ProductService.list()
        for product in products:
            products_data.append(product.as_dict())
        return jsonify(products_data)

    def get_detail(self, product_id):
        product = ProductService.load(product_id)
        return product.as_dict()

    def create(self):
        data = request.json
        product = ProductService.create(**data)
        return product.as_dict()

    def update(self, product_id):
        data = request.json
        product = ProductService.update(product_id, **data)
        return product.as_dict()

    def destroy(self, product_id):
        deleted = ProductService.delete(product_id)
        return deleted


products_blueprint = Blueprint('products', __name__)
products_blueprint.add_url_rule('/products/', view_func=ProductView.as_view("products"))
products_blueprint.add_url_rule('/products/<int:product_id>', view_func=ProductView.as_view("product"))
