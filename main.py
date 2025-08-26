from fastapi import FastAPI
from home.routes import home_router

app = FastAPI()

app.include_router(home_router)