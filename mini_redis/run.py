#!/usr/bin/env python3
import os
import sys
import signal
from uvicorn import run
import fire
from functools import partial
import logging

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s [%(levelname)s]: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(asctime)s [%(levelname)s]: %(client_addr)s - "%(request_line)s" %(status_code)s',  # noqa: E501
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.FileHandler",
            "filename": "/tmp/mini_redis/mini_redis.log",
        },
        "access": {
            "formatter": "access",
            "class": "logging.FileHandler",
            "filename": "/tmp/mini_redis/mini_redis.log",
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
    },
}

if not os.path.exists("/tmp/mini_redis"):
    os.makedirs("/tmp/mini_redis")
logging.basicConfig(
    filename="/tmp/mini_redis/mini_redis.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
# run.py


def daemonize():
    pid = os.fork()
    if pid > 0:
        sys.exit(0)

    os.chdir("/")
    os.setsid()
    os.umask(0)

    pid = os.fork()
    if pid > 0:
        sys.exit(0)

    sys.stdout.flush()
    sys.stderr.flush()
    si = open(os.devnull, 'r')
    so = open(os.devnull, 'a+')
    se = open(os.devnull, 'a+')
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

    with open("/tmp/mini_redis/mini_redis.pid", "w") as f:
        f.write(str(os.getpid()))
    logging.info("Daemon started")

from typing import Optional
def start(host: str = "0.0.0.0", port: int = 8000, reload: bool = False, workers: Optional[int] = None):
    if os.path.exists("/tmp/mini_redis/mini_redis.pid"):
        print("Daemon already running")
        sys.exit(0)
    daemonize()
    run("mini_redis.main:app", host=host, port=port, reload=reload,log_config=LOGGING_CONFIG, workers=workers)

def run_server(host: str = "0.0.0.0", port: int = 8000, reload: bool = False, workers: Optional[int] = None):
    run("mini_redis.main:app", host=host, port=port, reload=reload,log_config=LOGGING_CONFIG, workers=workers)
    
def stop():
    try:
        with open("/tmp/mini_redis/mini_redis.pid", "r") as f:
            pid = int(f.read())
        os.kill(pid, signal.SIGTERM)
        os.remove("/tmp/mini_redis/mini_redis.pid")
        logging.info("Daemon stopped")
    except FileNotFoundError:
        logging.error("Daemon not running or pid file not found")
    except ProcessLookupError:
        logging.error("Daemon process not found")
        os.remove("/tmp/mini_redis/mini_redis.pid")



def main():
    fire.Fire()


if __name__ == '__main__':
    main()
    
# #!/usr/bin/env python3
# from uvicorn import run
# import fire
# # run.py
# def run_server(host:str="0.0.0.0",port:int=8000,reload:bool=False):
#     run("mini_redis.main:app", host=host, port=port, reload=reload)

    
# def main():
#     fire.Fire(run_server)

# if __name__ == '__main__':
#     main()