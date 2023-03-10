from .base import CRUDMixin, SurrogatePK, TimestampMixin
from .redis_mixin import RedisModel
from app.extensions import db, bcrypt
from datetime import datetime


class User(CRUDMixin, SurrogatePK, db.Model, RedisModel):
    __tablename__ = "users"

    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password).decode()
        self.registered_on = datetime.now()
        self.admin = admin

    def get_by_email(self, email):
        return self.query.filter_by(email=email).first()
