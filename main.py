from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# In-memory request counter
request_counter = {"count": 0}

@app.get("/getstatus")
def get_status():
    request_counter["count"] += 1
    if request_counter["count"] == 1:
        return JSONResponse(content={"status": "picked up"})
    elif request_counter["count"] == 2:
        return JSONResponse(content={"status": "in progress"})
    else:
        return JSONResponse(content={"status": "delivered"})