from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

request_counter = {"count": 0}

statuses = ["picked up", "in progress", "delivered"]

@app.get("/getstatus")
def get_status():
    request_counter["count"] += 1
    # Use modulo to cycle through 0,1,2
    index = (request_counter["count"] - 1) % len(statuses)
    return JSONResponse(content={"status": statuses[index]})
