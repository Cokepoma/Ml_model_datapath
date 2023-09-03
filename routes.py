# importamos API router para Enrutamiento de API web.
from fastapi import APIRouter
# importamos el script ml_controller de la carpaeta controllers
from controllers.ml_controller import router as ml_routes

router = APIRouter()

router.include_router(ml_routes)