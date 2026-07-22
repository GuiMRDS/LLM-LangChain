
from langchain_google_genai import ChatGoogleGenecativeAI
from langchain_community.chat_models import ChatMaritalk
from langchain_core.messages import HumanMessage

from my_models import GEMINI_FLASH, MARITACA_SABIA
from my_keys import GEMINI_API_KEY, MARITACA_API_KEY
from my_helper import encode_image

llm = ChatGoogleGenecativeAI(
    api_key=GEMINI_API_KEY,
    model=GEMINI_FLASH,
)
resposta = llm.invoke("Quais canais de Youtuber você recomenda para que eu possa saber mais a respeito de smartphones")
print("Gemini: ", resposta.content)


llm = ChatMaritalk(
    api_key=MARITACA_API_KEY,
    model=MARITACA_SABIA,
)
resposta = llm.invoke("Quais canais de Youtuber você recomenda para que eu possa saber mais a respeito de smartphones")
print("Maritaca: ", resposta.content)

imagem = encode_image("dados\exemplo_grafico.jpg")
pergunta = "Descreva a imagem: "
mensagem = HumanMessage(
    content=[
        {
            "type": "text",
            "text": pergunta,
        },
        {
            "type": "image_url",
            "image_url": f"data:image/png;base64,{imagem}",
        }
    ]
)

resposta = llm.invoke([mensagem])
print(resposta)