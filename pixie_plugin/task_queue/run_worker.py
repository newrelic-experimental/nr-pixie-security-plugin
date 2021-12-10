from pixie_plugin.task_queue.pixie_plugin_worker import get_worker

worker = get_worker()
worker.work(with_scheduler=True)
