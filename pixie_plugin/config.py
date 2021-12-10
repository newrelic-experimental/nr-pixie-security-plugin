import logging
import os

from redis.sentinel import Sentinel

logger = logging.getLogger(__name__)

# These are required to start a developer instance of the application,
# if they are not present a ValueError will be raised.
REQUIRED_PARAMS = [
    "PIXIE_API_TOKEN",
    "PIXIE_CLUSTER_ID",
    "NR_INSERT_KEY",
    "NR_ACCOUNT_ID",
]
# If REDIS_SENTINEL env var is present REDIS_SENTINEL params are required, otherwise
# it is assumed Redis Sentinel is not being used and REDIS params are required.
REDIS_REQUIRED_PARAMS = ["REDIS_URL"]
REDIS_SENTINEL_REQUIRED_PARAMS = [
    "REDIS_SENTINEL_PORT",
    "REDIS_SENTINEL_HOST1",
    "REDIS_SENTINEL_HOST2",
    "REDIS_SENTINEL_HOST3",
    "REDIS_SENTINEL_MASTER",
]

# These are required in production but a developer instance can function without them,
# and they'll be set to None.
OPTIONAL_PARAMS = [
    # Redis
    "REDIS_PASSWORD",
    "REDIS_QUEUE_CHECKIN_ENDPOINT",
]


def get_config():
    logging.basicConfig(level="INFO")
    settings = {
        # Redis queue static settings.
        "REDIS_QUEUE_NAME": "pixie_plugin",
        "REDIS_QUEUE_SCHEDULER_NAME": "pixie_plugin",
        # This is disabled when unit testing in order to run jobs on the same thread.
        "REDIS_QUEUE_IS_ASYNC": True,
    }
    settings.update({key: _get_required_env_var(key) for key in REQUIRED_PARAMS})

    if os.environ.get("REDIS_SENTINEL"):
        redis_sentinel_settings = {
            key: _get_required_env_var(key) for key in REDIS_SENTINEL_REQUIRED_PARAMS
        }
        sentinel_port = redis_sentinel_settings["REDIS_SENTINEL_PORT"]
        sentinel = Sentinel(
            [
                (redis_sentinel_settings["REDIS_SENTINEL_HOST1"], sentinel_port),
                (redis_sentinel_settings["REDIS_SENTINEL_HOST2"], sentinel_port),
                (redis_sentinel_settings["REDIS_SENTINEL_HOST3"], sentinel_port),
            ],
        )
        host, port = sentinel.discover_master(
            redis_sentinel_settings["REDIS_SENTINEL_MASTER"]
        )
        settings["REDIS_URL"] = f"redis://{host}:{port}"
    else:
        settings.update(
            {key: _get_required_env_var(key) for key in REDIS_REQUIRED_PARAMS}
        )

    settings.update({key: _get_optional_env_var(key) for key in OPTIONAL_PARAMS})

    return settings


def _get_required_env_var(env_var_name):
    try:
        return os.environ[env_var_name]
    except KeyError:
        raise ValueError(
            f"required environment variable {env_var_name} has not been set."
        )


def _get_optional_env_var(env_var_name):
    value = os.environ.get(env_var_name)
    if value is None:
        logger.warning(
            f"environment variable {env_var_name} has not been set, using None."
        )
    return value
