#!/usr/bin/env bash

cd /var/app

exec newrelic-admin run-program python pixie_plugin/task_queue/run_scheduler.py 2>&1 &
exec newrelic-admin run-program python pixie_plugin/task_queue/run_worker.py
