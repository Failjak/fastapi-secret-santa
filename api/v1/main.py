from fastapi import APIRouter

from .secretsanta import router as secretsanta_router

router = APIRouter(prefix='/v1')

router.include_router(secretsanta_router)
