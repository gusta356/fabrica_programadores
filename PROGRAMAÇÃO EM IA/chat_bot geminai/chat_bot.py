from google import genai
from dotenv import load_dotenv
import os
import pygame
from gtts import gTTS
import os

# CARREGA AS VARIAVEIS DO ARQUIVO .ENV
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


#cria o client gemini
client = genai.Client(api_key=API_KEY)

def speak(texto:)
    tts = gTTS(text=texto, lang='pt-br')
    arquivo = "voz.mp3"
    try:
    os.remove(arquivo)
except OSError:
    pass
tts.save(arquivo)

pygame.mixer.init()
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy()
    pass

pygame.mixer.music.unload()
#chatbot
print("=" * 50)
print("🤖 CHATBOT GEMINI")
print("digite 'sair' para encerrar.")
print("=" * 50)

historico = []

while True:

    pergunta = input("\nVocê: ")

    if pergunta.lower() == "sair":
        print("\nAté logo!")
        break

    #armazena o historico 
    historico.append(
        {
            "role" : "user",
            "parts" : [{"text" :pergunta}]
        }
    )

    #envia todo o história
    resposta = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=historico
    )

    texto = resposta.text

    #armazena a resposta da ia para manter o contexto
    historico.append(
        {
            "role" : "model",
            "parts" : [{"text: texto"}]
        }
    )

    print(f"🤖 {texto}")
    speak(texto:)