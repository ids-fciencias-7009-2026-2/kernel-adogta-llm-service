from pydantic import BaseModel, Field

class ClasificacionRequest(BaseModel):
    nombre: str = Field(..., description="Nombre de la raza")
    texto_a_clasificar: str = Field(..., description="El texto del temperamento a clasificar")

class ResultadoClasificacion(BaseModel):
    nombre: str = Field(..., description="Nombre traducido al español")
    temperamento: str = Field(..., description="Temperamento traducido al español")
    nivelEnergia: int = Field(ge=1, le=5, description="Nivel de energía del perro del 1 al 5")
    sociableNinos: int = Field(ge=1, le=5, description="Sociabilidad con niños del 1 al 5")
    sociableMascotas: int = Field(ge=1, le=5, description="Sociabilidad con otras mascotas del 1 al 5")
    independencia: int = Field(ge=1, le=5, description="Nivel de independencia del 1 al 5")