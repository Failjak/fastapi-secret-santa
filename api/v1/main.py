from fastapi import APIRouter

from .secretsanta import router as secretsanta_router
from .player import router as player_router

router = APIRouter(prefix='/v1')

router.include_router(secretsanta_router)
router.include_router(player_router)
