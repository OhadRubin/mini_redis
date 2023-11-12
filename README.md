
# Mini-Redis Project

This project is a simplified version of a Redis-like key-value store implemented in Python using FastAPI. It provides basic functionality to set, get, and delete byte strings associated with string keys.

## Features

- Set a value for a given key.
- Retrieve a value for a given key.
- Delete a key-value pair.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/OhadRubin/mini_redis.git
cd mini_redis
```

Install the package:

```bash
pip install .
```

To install in editable mode (useful for development):

```bash
pip install -e .
```

## Running the Server

To start the server, use the following command:

```bash
mini_redis start

# uvicorn mini_redis.main:app --reload --host 0.0.0.0 
```

The server will start running on `http://127.0.0.1:8000`.

mini_redis stop


### Alternatively:

To start the server, run the following command after installation:

```bash
start_mini_redis

## Usage

Once the server is running, you can use the following endpoints:

- `POST /set/{key}`: Set a value for a key.
- `GET /get/{key}`: Get the value for a key.
- `DELETE /delete/{key}`: Delete a key-value pair.

## Example

Setting a value for a key:

```bash
curl -X 'POST' 'http://127.0.0.1:8000/set/my_key' -H 'accept: application/json' -d 'my_value'
```

Getting a value for a key:

```bash
curl -X 'GET' 'http://127.0.0.1:8000/get/my_key' -H 'accept: application/json'
```

Deleting a key-value pair:

```bash
curl -X 'DELETE' 'http://127.0.0.1:8000/delete/my_key' -H 'accept: application/json'
```

## Client Usage

You can interact with the server programmatically using the provided Python client. Here's an example of how to use the client:

```python
from mini_redis.client import MiniRedisClient

# Initialize the client
client = MiniRedisClient('http://localhost:8000')

# Set a value
client['my_key'] = b'my_value'

# Get a value
value = client['my_key']

# Delete a key
del client['my_key']
```

## Contributions

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.