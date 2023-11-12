from fastapi import FastAPI
from routes.activity_routes import activity_router
app = FastAPI()

app.include_router(activity_router)