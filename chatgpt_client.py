from openai import OpenAI
from dotenv import load_dotenv
import os

# 1) Cargar variables desde .env
load_dotenv()

# 2) Crear cliente usando la variable de entorno
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 3) Preguntar al usuario
pregunta = input("What is your question for ChatGPT? ")

# 4) Enviar la pregunta a OpenAI
response = client.chat.completions.create(
    model="gpt-5.2",
    messages=[
        {"role": "user", "content": pregunta}
    ]
)

# 5) Mostrar respuesta
print("\nRespuesta de ChatGPT:\n")
print(response.choices[0].message.content)

