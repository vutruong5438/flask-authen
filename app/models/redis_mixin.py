import os
import pickle
import redis


class RedisModel:
    def __init__(self, redis_url=None):
        if redis_url is None:
            redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
        self.redis_client = redis.from_url(redis_url)

    def set_value(self, key, value):
        self.redis_client.set(key, pickle.dumps(value))

    def get_value(self, key):
        value = self.redis_client.get(key)
        if value is not None:
            value = pickle.loads(value)
        return value
