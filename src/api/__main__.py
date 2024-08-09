import uvicorn

from fastapi import FastAPI
from src.api.setup import create_app
from src.api.routes import setup_routers


def main() -> FastAPI:
    app = create_app()
    app.include_router(setup_routers())
    return app


def run():
    uvicorn.run('src.api.__main__:main')


if __name__ == "__main__":
    run()
