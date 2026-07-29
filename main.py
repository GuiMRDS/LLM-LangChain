import time

from langchain.agents import AgentExecutor
from agente.orquestrador import AgenteOrquestrador


def main():
    agente = AgenteOrquestrador()

    orquestrador = AgentExecutor(
        agent=agente.agente,
        tools=agente.tools,
        verbose=True,
    )

    inicio = time.time()

    print("""
    === Assistente IA ===

    Exemplos:
    - Explique o que são desvios condicionais
    - Faça uma análise da imagem exemplo_grafico.jpg

    Digite 'sair' para encerrar.
    """)

    while True:
        pergunta = input("Você: ")

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Até logo!")
            break

        try:
            resposta = orquestrador.invoke({
                "input": pergunta
            })

            fim = time.time()

            print("\nAssistente:")
            print(resposta["output"])
            print(f"\n⏱ Tempo: {fim - inicio:.2f}s")

        except Exception as e:
            print(f"\nErro: {e}\n")


if __name__ == "__main__":
    main()