import google.generativeai as genai
from my_keys import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

for model_name in [
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
    "gemini-2.0-flash",
]:
    try:
        print(f"\nTestando {model_name}")

        model = genai.GenerativeModel(model_name)

        response = model.generate_content(
            "Diga apenas OK"
        )

        print(response.text)

    except Exception as e:
        print("ERRO:", e)