from redis import Redis


class RedisCache(Redis):
    def __init__(self, connection_pool):
        super().__init__()
        self.connection_pool = connection_pool