from fastapi import FastAPI
import os

from users import urls


DATABASE_URL = os.environ.get("DATABASE_URL")


app = FastAPI(title="FastAPI, Docker, and Traefik")


app.include_router(urls.router)
