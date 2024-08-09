from fastapi import APIRouter

from . import redirect, short_url


def setup_routers() -> APIRouter:
    router = APIRouter()
    router.include_router(redirect.router)
    router.include_router(short_url.router)
    return router
