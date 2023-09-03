from fastapi import APIRouter
from controllers.ml_controller import router as ml_routes

router = APIRouter()

router.include_router(ml_routes)