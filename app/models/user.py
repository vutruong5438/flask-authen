from .base import CRUDMixin, TimestampMixin
from .redis_mixin import RedisModel
from app.extensions import db, bcrypt
from datetime import datetime


class User(db.Model, RedisModel):
    __tablename__ = "users"

    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))
    profile = db.relationship("UserProfile", backref="user",  uselist=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password).decode()
        self.registered_on = datetime.now()
        self.admin = admin

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def load(cls, id):
        return User.query.get(id)

    @staticmethod
    def check_password_hash(password_hash, password):
        return bcrypt.check_password_hash(password_hash, password)


