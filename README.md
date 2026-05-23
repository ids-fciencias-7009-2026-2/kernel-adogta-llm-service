# adogta-llm-service

Microservicio FastAPI para mapear respuestas de APIs a valores numéricos (1-5) usando LLM.

## Ejecutar local

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Endpoint

- `POST /clasificar-temperamento`
  - request:
    ```json
    {
      "nombre": "Pug",
      "texto_a_clasificar": "Affectionate, playful, friendly, charming, adaptable"
    }
    ```
    1. Nuestro backend envía el temperamento de la raza
    2. El LLM traduce al español el nombre y el temperamento, y mapea el temperamento a los 4 campos numéricos (1-5), con reintento si el formato es inválido.
    3. Este servicio responde por HTTP con el JSON que incluye traducciones y métricas.
  - response:
    ```json
    {
      "nombre": "Pug",
      "temperamento": "Cariñoso, juguetón, simpático, encantador, adaptable",
      "nivelEnergia": 4,
      "sociableNinos": 5,
      "sociableMascotas": 5,
      "independencia": 2
    }
    ```
