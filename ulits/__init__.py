import pika
import redis
from config import config
from .cache import RedisCache

redisPool = redis.ConnectionPool(host=config.REDIS_HOST, port=config.CACHE_REDIS_PORT, decode_responses=True, max_connections=config.CACHE_REDIS_MAX_CONN)
myCache = RedisCache(connection_pool=redisPool)

# MessageQueuePool = pika.BlockingConnection(pika.ConnectionParameters(config.MQ_HOST))