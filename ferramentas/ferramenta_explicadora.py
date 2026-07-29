from typing import Any

from langchain.tools import BaseTool
from langchain_community.chat_models import ChatMaritalk
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain.prompts import ChatPromptTemplate, PromptTemplate


from my_keys import GEMINI_API_KEY
from my_models import GEMINI_FLASH
import ast

class FerramentaExplicadora(BaseTool):
    name : str = "Ferramenta Explicadora"
    description : str = """
    Utilize esta ferramente sempre que for solicitado que você explique um conteudo para pessoas.
    
    # Entrada Requeridas
    - 'tema' (str) : Tema principal informado na pergunta do usuario
    """

    return_direct : bool = True

    def _run(self, acao):
        acao = ast.literal_eval(acao)
        tema_parametro  = acao.get("tema", "")

        llm = ChatGoogleGenerativeAI(
            api_key=GEMINI_API_KEY,
            model=GEMINI_FLASH,
        )

        template_resposta = PromptTemplate(
        template = """
        Assuma o papel de um professor preocupado com aspectos de didática do usuario.
        
        1. Elabore uma explicação sobre o tema {tema} que seja compreesível por estudantes na fase de conclusão do ensino medio.
        2. Utilise exemplos do contidiano para tornar a explicação mais facil
        3. Caso sugira algum recurso par apoiar a explicação, lembre-se do cenário e contexto brasileiro.
        4. Caso você apresente um codigo, seja didático e utlilise Python
        
        Tema pergunta: {tema}
        """,
        input_variables=["tema"]
        )

        cadeia = template_resposta | llm | StrOutputParser()

        resposta = cadeia.invoke({"tema": tema_parametro})
        print("RESPOSTA:", resposta)