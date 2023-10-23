from .base import CRUDMixin, TimestampMixin
from .redis_mixin import RedisModel
from app.extensions import db


class UserProfile(db.Model, RedisModel):
    __tablename__ = "user_profiles"

    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
