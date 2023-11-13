from typing import Union, Any
from fastapi import FastAPI,Request
import os

app = FastAPI()
from sqlitedict import SqliteDict
from filelock import FileLock

if not os.path.exists("/tmp/mini_redis"):
    os.makedirs("/tmp/mini_redis")


# This will act as our in-memory 'database'
db = SqliteDict("/tmp/mini_redis/mini_redis_database.sqlite", autocommit=True)
lock = FileLock("/tmp/mini_redis/mini_redis_database.lock")




@app.post("/set/{key}")
async def set_key(key: str, request: Request):
    body = await request.body()
    # print(key,value)
    # Store the value at the given key
    with lock, db:
        db[key] = body
    return {"success": True}


@app.get("/get/{key}")
def get_key(key: str) -> Any:
    # Retrieve the value at the given key
    with lock, db:
        value = db.get(key, None)
        if value is not None:
            return {"value": value}
    return {"error": "Key not found"}


@app.delete("/delete/{key}")
def delete_key(key: str):
    # Remove the value at the given key
    with lock, db:
        if key in db:
            del db[key]
            return {"success": True}
    return {"error": "Key not found"}


@app.get("/exists/{key}")
def key_exists(key: str):
    # Check if the key exists in the database
    with lock, db:
        return {"exists": key in db}

@app.get("/keys")
def get_keys():
    # Return all keys in the database
    with lock, db:
        return {"keys": list(db.keys())}

@app.get("/values")
def get_values():
    # Return all values in the database
    with lock, db:
        return {"values": list(db.values())}

@app.get("/items")
def get_items():
    # Return all items in the database
    with lock, db:
        return {"items": list(db.items())}

@app.delete("/clear")
def clear_db():
    # Clear the database
    with lock, db:
        db.clear()
        return {"success": True}