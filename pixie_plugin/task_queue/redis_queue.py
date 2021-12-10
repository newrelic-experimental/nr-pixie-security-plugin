from urllib.parse import urlparse

from redis import Redis
from rq import Queue


def redis_connection(config):
    url = urlparse(config["REDIS_URL"])
    return Redis(host=url.hostname, port=url.port, password=config["REDIS_PASSWORD"])


def redis_queue(config):
    redis = redis_connection(config)
    queue = Queue(
        name=config["REDIS_QUEUE_NAME"],
        connection=redis,
        is_async=config["REDIS_QUEUE_IS_ASYNC"],
    )
    return queue
