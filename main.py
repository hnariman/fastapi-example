from fastapi import FastAPI
from controllers.root import root_controller

app = FastAPI()

@app.get("/")
async def root():
    return root_controller()
