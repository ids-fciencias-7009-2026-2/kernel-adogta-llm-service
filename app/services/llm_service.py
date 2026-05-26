from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.core.config import settings
from app.models.schemas import ResultadoMapeo

class LLMService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.openai_model,
            api_key=settings.openai_api_key,
            temperature=0
        ).with_structured_output(ResultadoMapeo)

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "Eres un experto en comportamiento canino. Evalúa los rasgos proporcionados y clasifícalos obligatoriamente en valores enteros del 1 al 5."),
            ("human", "Analiza esta información y extrae las métricas: {text}")
        ])
        
        self.chain = self.prompt | self.llm

    async def clasificar_texto(self, text: str) -> ResultadoMapeo:
        try:
            return await self.chain.ainvoke({"text": text})
        except Exception as e:
            raise RuntimeError("Error al invocar OpenAI") from e

llm_service = LLMService()