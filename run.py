#!/usr/bin/env python3
from uvicorn import run
import fire
# run.py
def run_server(host:str="0.0.0.0",port:int=8000,reload:bool=True):
    run("mini_redis.main:app", host=host, port=port, reload=reload)

if __name__ == "__main__":
    fire.Fire(run_server)