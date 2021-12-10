from rq import Worker

from pixie_plugin.config import get_config
from pixie_plugin.task_queue.exception_handlers import retry_handler
from pixie_plugin.task_queue.redis_queue import redis_queue


def get_worker():
    """
    Creates a redis queue worker with a retry exception handler.

    To run the worker:
    >> worker = get_worker()
    >> worker.work(with_scheduler=True)
    """
    settings = get_config()
    queue = redis_queue(settings)
    return Worker(
        queues=[queue], connection=queue.connection, exception_handlers=[retry_handler]
    )
