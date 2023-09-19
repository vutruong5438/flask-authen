from .base import CRUDMixin, SurrogatePK, TimestampMixin
from .redis_mixin import RedisModel
from app.extensions import db
from flask_sqlalchemy import Model


class UserProfile(db.Model, CRUDMixin, SurrogatePK, RedisModel):
    __tablename__ = "user_profiles"

    first_name = db.Column(db.String(50), )
    last_name = db.Column(db.String(50), )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
