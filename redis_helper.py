import redis


class RedisCache:
	redis_client = redis.Redis(host='localhost', port=6378, decode_responses=True)
	@classmethod
	def key_with_ttl(cls, key: str, data, ttl_in_seconds: int, namespace: str = ''):
		key = f"{namespace}:{key}"
		cls.redis_client.setex(key, ttl_in_seconds, data)
		return True
	
	@classmethod
	def get_with_key(cls, key: str, namespace: str = ''):
		key = f"{namespace}:{key}"
		return cls.redis_client.get(key)
