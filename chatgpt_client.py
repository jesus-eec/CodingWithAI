from openai import OpenAI
from dotenv import load_dotenv
import os

# 1) Cargar variables desde .env
load_dotenv()

# 2) Crear cliente usando la variable de entorno
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 3) Preguntar al usuario
pregunta = input("¿Cuál es tu pregunta para ChatGPT? ")

# 4) Enviar la pregunta a OpenAI
respuesta = cliente.chat.completions.create(
    modelo="gpt-5.2",
    mensajes=[
        {"role": "user", "content": pregunta}
    ]
)

# 5) Mostrar respuesta
print("\nRespuesta de ChatGPT:\n")
print(respuesta.choices[0].mensajes.content)

