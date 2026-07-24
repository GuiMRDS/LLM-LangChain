from langchain_google_genai import ChatGoogleGenerativeAI
from my_keys import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=GEMINI_API_KEY
)

resposta = llm.invoke(
    "Explique o que é LangChain em uma frase."
)

print(resposta.content)