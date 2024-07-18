import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

# +--------------------------------------------------------------------------------------------------+#
# API ROOT
# +--------------------------------------------------------------------------------------------------+#
@app.get("/")
async def root():
    return {"message": "Hello from Sum API"}

# +--------------------------------------------------------------------------------------------------+#
# API endpoint example without any params
# GET API endpoint for healthcheck
# +--------------------------------------------------------------------------------------------------+#
@app.get("/health")
async def read_health():
    return {"health": "good"}

# +--------------------------------------------------------------------------------------------------+#
# API Endpoint Query Parameter Example
# GET API endpoint to calculate sum of x and y
# +--------------------------------------------------------------------------------------------------+#
@app.get("/sum")
async def get_sum(x:int, y:int) -> dict:
    status = True
    sum = (x + y)
    print(f"Number={x}; sum={sum}")
    return {'status': status, 'number1': x, 'number2':y, 'result': sum}

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8800))
    uvicorn.run(app, host="0.0.0.0", port=PORT)
