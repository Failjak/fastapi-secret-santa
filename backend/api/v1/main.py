from fastapi import APIRouter

from api.v1.secretsanta import router as secretsanta_router
from api.v1.player import router as player_router
from api.v1.card import router as card_router

router = APIRouter(prefix='/v1')

router.include_router(secretsanta_router)
router.include_router(player_router)
router.include_router(card_router)
