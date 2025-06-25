# Dummy Status API

This is a simple FastAPI app with one endpoint `/getstatus` that returns the following statuses on successive requests:

1. `{"status": "picked up"}`
2. `{"status": "in progress"}`
3. `{"status": "delivered"}` (for all future requests)

## How to Run Locally

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Start the server

```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/getstatus` in your browser or use `curl`.

## Deployment

You can deploy this API for free using services like:

- [Render](https://render.com)
- [Replit](https://replit.com)
- [Fly.io](https://fly.io)