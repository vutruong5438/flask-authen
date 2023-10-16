from .base import CRUDMixin
from .base import TimestampMixin
from .redis_mixin import RedisModel
from app.extensions import db


class Product(db.Model, TimestampMixin, RedisModel):
    __tablename__ = "products"

    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float)
    active = db.Column(db.Boolean, default=True)
    category = db.Column(db.String(255))

    def __init__(self, name, code):
        self.name = name
        self.code = code
