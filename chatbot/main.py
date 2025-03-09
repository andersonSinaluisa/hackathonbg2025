from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from typing import Dict, List
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

chat_histories: Dict[str, List[Dict[str, str]]] = {}


DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY","")

SYSTEM_PROMPT = """Eres un oficial de credito y tienes que realizar las siguientes preguntas de forma separada (diferentes mensajes) una vez que te resopondan una pregunta avanza con la siguiente:
1. ¿De cuanto son tus ingresos mensuales?  (numero)
2. ¿Cuanto son tus gastos mensuales?  (numero)
3. ¿Cuantas cargas familiares tienes? (numero)
Cuando tengas todas las respuestas tienes que completar la siguiente respuesta en formato JSON con los valores obtenidos:
{ ingreso_mensual: valor, gasto_mensual: valor, cargas: valor }
"""

SYSTEM_PROMPT_EVIDENCE = """Eres un oficial de credito y tienes que realizar las siguientes preguntas de forma separada (diferentes mensajes) una vez que te resopondan una pregunta avanza con la siguiente:
1. ¿Adjunta tu numero ?  (numero)
2. ¿Cuanto son tus gastos mensuales?  (numero)
3. ¿Cuantas cargas familiares tienes? (numero)
Cuando tengas todas las respuestas tienes que completar la siguiente respuesta en formato JSON con los valores obtenidos:
{ ingreso_mensual: valor, gasto_mensual: valor, cargas: valor }
"""

SYSTEM_PROMPT_FINAL = """Eres un oficial de credito y tienes que realizar las siguientes preguntas de forma separada (diferentes mensajes) una vez que te resopondan una pregunta avanza con la siguiente:
1. ¿Escribe tu numero celular?  (numero)
2. ¿Escribe tu correo electronico?
3. ¿Adjunta evidencia de solvencia? (numero)
Cuando tengas todas las respuestas tienes que completar la siguiente respuesta en formato JSON con los valores obtenidos:
{ ingreso_mensual: valor, gasto_mensual: valor, cargas: valor }
"""

class ChatMessage(BaseModel):
    user_id: str  # Each client must send a unique identifier
    message: str


def getCreditScore(json):
    print("JSON")
    print(json)
    return 600


@app.post("/chat")
async def chat(chat_message: ChatMessage):
    print(chat_histories)
    client = OpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com",
    )
    if chat_message.user_id not in chat_histories:
        chat_histories[chat_message.user_id] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    # Append the user's message to history
    chat_histories[chat_message.user_id].append(
        {"role": "user", "content": chat_message.message}
    )

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=chat_histories[chat_message.user_id],
            stream=False,
        )
        response_message:str = response.choices[0].message.content
        # Append assistant's response to history
        if "{" in response_message:
            score_value =  getCreditScore(response_message)
            if(score_value<600):
                response_message =  "Lo siento no cumples los requerimientos para un credito con esas caracteristicas"
            if(score_value>750):
                response_message =  "Felicidades, por favor adjunta tu numero de celular y correo electronico para que un asesor se contacte contigo"
            if(score_value>=600):
                response_message =  "Necesitamos mas informacion, a continuacion te haremos un par de preguntas mas"


        chat_histories[chat_message.user_id].append(
            {"role": "assistant", "content": response_message}
        )
        return {"message": response_message}

    except Exception as e:
        return {"message": e.message}
