import os
import pickle
import redis
from .base import CRUDMixin


class RedisModel(CRUDMixin):

    redis_client = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=os.getenv('REDIS_PORT', 6379), db=10)

    @classmethod
    def cache_set(cls, key, value):
        h_name = cls.__name__
        h_value: bytes = pickle.dumps(value)
        cls.redis_client.hset(name=h_name, key=key, value=h_value)

    @classmethod
    def cache_get(cls, key):
        hash_name = cls.__name__
        value = cls.redis_client.hget(hash_name, key)
        if value is not None:
            value = pickle.loads(value)
        return value

    @classmethod
    def load(cls, pk):
        value = cls.cache_get(pk)
        if not value:
            value = cls.get_by_id(pk)
            cls.cache_set(pk, value)
        return value

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        res = super().create(**kwargs)
        cls.cache_set(res.id, res)
        return res

    def save(self, commit=True):
        res = super().save(commit)
        self.cache_set(self.id, self)
        return res
