from fastapi import FastAPI

from users import urls

app = FastAPI(title="FastAPI, Docker, and Traefik")


app.include_router(urls.router)
