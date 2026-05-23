from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.core.config import settings
from app.models.schemas import ResultadoClasificacion

class LLMService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.openai_model,
            api_key=settings.openai_api_key,
            temperature=0
        ).with_structured_output(ResultadoClasificacion)

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "Eres un experto en comportamiento canino. Traduce al español el nombre de la raza y el temperamento. Clasifica obligatoriamente en valores enteros del 1 al 5 y devuelve exactamente los campos solicitados."
            ),
            (
                "human",
                "Nombre: {nombre}. Temperamento: {text}. Genera la traducción y las métricas."
            )
        ])
        
        self.chain = self.prompt | self.llm

    async def clasificar_texto(self, nombre: str, text: str) -> ResultadoClasificacion:
        try:
            return await self.chain.ainvoke({"nombre": nombre, "text": text})
        except Exception as e:
            return ResultadoClasificacion(
                nombre=nombre,
                temperamento=text,
                nivelEnergia=3,
                sociableNinos=3,
                sociableMascotas=3,
                independencia=3,
            )

llm_service = LLMService()