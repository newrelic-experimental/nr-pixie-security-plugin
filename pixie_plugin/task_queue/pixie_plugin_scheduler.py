import logging

from rq_scheduler import Scheduler

from pixie_plugin.config import get_config
from pixie_plugin.task_queue.redis_queue import redis_queue
from pixie_plugin.tasks import identify_sql_injections

logger = logging.getLogger(__name__)


def get_scheduler():
    """
    Creates a scheduler with scheduled jobs.

    To run the scheduler:
    >> scheduler = get_scheduler()
    >> scheduler.run()
    """
    settings = get_config()
    queue = redis_queue(settings)
    scheduler = Scheduler(queue_name=queue.name, connection=queue.connection)

    # Clear the queue and scheduler of all old jobs on startup otherwise the previously
    # scheduled jobs from the previous run will remain in the queue and scheduler and
    # result in duplicated jobs.
    queue.empty()
    for job in scheduler.get_jobs():
        scheduler.cancel(job)
        logger.info(f"Removed old job {job} from scheduler.")

    # Run the identify sql injections task every minute.
    identify_sql_injections_job = scheduler.cron(
        cron_string="*/1 * * * *",
        func=identify_sql_injections,
        queue_name=settings["REDIS_QUEUE_NAME"],
    )
    logger.info(f"Added job {identify_sql_injections_job}")

    return scheduler
