from typing import Union, Any
from fastapi import FastAPI,Request

app = FastAPI()

# This will act as our in-memory 'database'
db = {}


@app.post("/set/{key}")
async def set_key(key: str, request: Request):
    body = await request.body()
    # print(key,value)
    # Store the value at the given key
    db[key] = body
    return {"success": True}


@app.get("/get/{key}")
def get_key(key: str) -> Any:
    # Retrieve the value at the given key
    value = db.get(key, None)
    if value is not None:
        return {"value": value}
    return {"error": "Key not found"}


@app.delete("/delete/{key}")
def delete_key(key: str):
    # Remove the value at the given key
    if key in db:
        del db[key]
        return {"success": True}
    return {"error": "Key not found"}
