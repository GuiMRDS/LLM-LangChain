from google import genai
from my_keys import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explique o que é LangChain em uma frase."
)

print(response.text)