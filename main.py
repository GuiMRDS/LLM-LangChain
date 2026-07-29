from langchain.agents import AgentExecutor
from agente.orquestrador import AgenteOrquestrador

def main():
    agente = AgenteOrquestrador()
    orquestrador = AgentExecutor(
        agent=agente.agente,
        tools=agente.tools,
        verbose=True,
    )

    pergunta = "Gostaria que você me explicasse como funcionam os devios condicionais"
    resposta = orquestrador.invoke({"input": pergunta})
    print(resposta)


if __name__ == "__main__":
    main()