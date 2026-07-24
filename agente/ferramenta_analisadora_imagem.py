from langchain.tools import BaseTool

class FerramentaAnalisadoraImagem(BaseTool):
    name:str = "Ferramenta Analisadora Imagem"
    description:str = """
    Utilize esta ferramenta sempre que for solicitada que você faça uma analise de imagem.
    
    # Entradas Requiridas
    - 'nome_imagem' (str) : Nome da imagem a ser analisada com extensão da JPG.
    Exemplo: teste.jpg ou teste.jpeg
    """

    return_direct : bool = False

    def _run(self, acao):
        return ""