from app.models import Product


class ProductService:

    @classmethod
    def create(cls, **data):
        product = Product(**data).save()
        return product

    @classmethod
    def update(cls, pk, **data):
        product = cls.load(pk)
        product = product.update(**data)
        return product

    @classmethod
    def get(cls, pk):
        product = Product.get_by_id(pk)
        return product

    @classmethod
    def list(cls):
        products = Product.query.all()
        return products

    @classmethod
    def load(cls, pk):
        product = Product.load(pk)
        return product
