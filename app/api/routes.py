from fastapi import APIRouter
from app.models.schemas import ClasificacionRequest, ResultadoMapeo
from app.services.llm_service import llm_service

router = APIRouter()

@router.post("/clasificar-temperamento", response_model=ResultadoMapeo)
async def clasificar_temperamento(payload: ClasificacionRequest) -> ResultadoMapeo:
    """
    Recibe un texto descriptivo del temperamento de un animal y devuelve 
    4 valores numéricos (1-5) procesados por IA.
    """
    result = await llm_service.clasificar_texto(payload.texto_a_clasificar)
    return result