import newrelic.agent


def retry_handler(job, exc_type, exc_value, traceback):
    """
    Requeue a failed job max_retry times before giving up.

    The number of times the job is requeued and the number of times is has been requeued
    are configured and tracked in the job metadata:
        job.meta["max_retry"]              default: 3
        job.meta["retry_attempts"]         default: 0
    """
    max_retry = job.meta.get("max_retry", 3)
    retry_attempts = job.meta.get("retry_attempts", 0)

    # Record exception in New Relic.
    app = newrelic.agent.register_application(timeout=10)
    with newrelic.agent.BackgroundTask(app, "retry_handler"):
        newrelic.agent.record_exception(
            exc_type,
            exc_value,
            traceback,
            params={"retry_attempt": retry_attempts, "job_id": job.id},
        )
    newrelic.agent.shutdown_agent(timeout=10)

    if retry_attempts < max_retry:
        job.meta["retry_attempts"] = retry_attempts + 1
        job.meta["max_retry"] = max_retry
        job.save_meta()
        job.requeue()
