import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

# +--------------------------------------------------------------------------------------------------+#
# API ROOT
# +--------------------------------------------------------------------------------------------------+#
@app.get("/")
async def root():
    return {"message": "Hello from Square API"}

# +--------------------------------------------------------------------------------------------------+#
# API endpoint example without any params
# GET API endpoint for healthcheck
# +--------------------------------------------------------------------------------------------------+#
@app.get("/health")
async def read_health():
    return {"health": "good"}

# +--------------------------------------------------------------------------------------------------+#
# API Endpoint Path Parameter Example
# GET API endpoint to calculate square of a x
# +--------------------------------------------------------------------------------------------------+#
@app.get("/square/{x}")
async def get_square(x:int) -> dict:
    status = True
    squarenumber = (x ** 2)
    print(f"Number={x}; Square={squarenumber}")
    return {'status': status, 'number': x, 'result': squarenumber}

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8800))
    uvicorn.run(app, host="0.0.0.0", port=PORT)
