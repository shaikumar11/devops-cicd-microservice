import os
import redis
from flask import Flask, jsonify, request, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
r = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"), decode_responses=True)
REQS = Counter("app_requests_total", "Total requests", ["endpoint", "method"])


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    try:
        r.ping()
        return {"status": "ready"}
    except redis.exceptions.RedisError:
        return {"status": "redis unavailable"}, 503


@app.get("/api/items")
def list_items():
    REQS.labels("/api/items", "GET").inc()
    return jsonify(r.lrange("items", 0, -1))


@app.post("/api/items")
def add_item():
    REQS.labels("/api/items", "POST").inc()
    name = (request.get_json(silent=True) or {}).get("name")
    if not name:
        return {"error": "name required"}, 400
    r.rpush("items", name)
    return {"added": name}, 201


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)