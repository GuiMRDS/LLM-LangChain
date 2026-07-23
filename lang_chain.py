from langchain.chains.qa_with_sources.stuff_prompt import template
from langchain_google_genai import ChatGoogleGenecativeAI
from langchain_community.chat_models import ChatMaritalk
from langchain_core.messages import HumanMessage

from my_models import GEMINI_FLASH, MARITACA_SABIA
from my_keys import GEMINI_API_KEY, MARITACA_API_KEY
from my_helper import encode_image
from langchain.prompts import ChatPromptTemplate


llm = ChatGoogleGenecativeAI(
    api_key=GEMINI_API_KEY,
    model=GEMINI_FLASH,
)



llm = ChatMaritalk(
    api_key=MARITACA_API_KEY,
    model=MARITACA_SABIA,
)

template_analisador = ChatPromptTemplate.from_messages(
    [
        (
            "systen",
            """
            Assuma que vocé é um analisador de imagens. A sua tarefa principal 
            consiste em: analisar uma imagem e extrari informações importantes 
            de forma objetiva.
            """
        ),
        (
            "user",
            [
                {
                    "type": "text",
                    "text": "Descreva a imagem: ",
                },
                {
                    "type": "image_url",
                    "image_url": "data:image/png;base64,{imagem}",
                }
            ]
        )
    ])

imagem = encode_image("dados\exemplo_grafico.jpg")
mensagem = HumanMessage(

)

resposta = llm.invoke([mensagem])
print(resposta)