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
    try:
        with lock, db:
            db[key] = body
        return {"success": True}
    except Exception:
        return {"error": "Failed to set key"}


@app.get("/get/{key}")
def get_key(key: str) -> Any:
    # Retrieve the value at the given key
    try:
        with lock, db:
            value = db.get(key, None)
            if value is not None:
                return {"value": value}
    except KeyError:
        return {"error": "Key not found"}
    except Exception:
        return {"error": "Failed to get key"}


@app.delete("/delete/{key}")
def delete_key(key: str):
    # Remove the value at the given key
    try:
        with lock, db:
            if key in db:
                del db[key]
                return {"success": True}
    except KeyError:
        return {"error": "Key not found"}
    except Exception:
        return {"error": "Failed to delete key"}


@app.get("/exists/{key}")
def key_exists(key: str):
    # Check if the key exists in the database
    try:
        with lock, db:
            return {"exists": key in db}
    except Exception:
        return {"error": "Failed to check if key exists"}

@app.get("/keys")
def get_keys():
    # Return all keys in the database
    try:
        with lock, db:
            return {"keys": list(db.keys())}
    except:
        return {"error": "Failed to get keys"}

@app.get("/values")
def get_values():
    # Return all values in the database
    try:
        with lock, db:
            return {"values": list(db.values())}
    except:
        return {"error": "Failed to get values"}

@app.get("/items")
def get_items():
    # Return all items in the database
    try:
        with lock, db:
            return {"items": list(db.items())}
    except:
        return {"error": "Failed to get items"}

@app.delete("/clear")
def clear_db():
    # Clear the database
    try:
        with lock, db:
            db.clear()
            return {"success": True}
    except:
        return {"error": "Failed to clear database"}