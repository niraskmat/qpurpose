from fastapi import FastAPI
from .database import Base, engine
from .routes import user_routes, task_routes

Base.metadata.create_all(bind=engine)

def create_app():
    app = FastAPI()
    app.include_router(user_routes.router)
    app.include_router(task_routes.router)
    return app
