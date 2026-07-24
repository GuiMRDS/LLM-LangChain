from pydantic import BaseModel


class DetalhesImagemModelo(BaseModel):
    descricao: str
    rotulos: list[str]