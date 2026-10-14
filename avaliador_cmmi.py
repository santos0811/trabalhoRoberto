# Trabalho: Avaliador Simplificado de Maturidade CMMI
# Simulacao didatica: nao substitui uma avaliacao real de CMMI.

perguntas = [
    "Projetos sao planejados?",
    "Requisitos sao controlados?",
    "Responsaveis estao definidos?",
    "Existe acompanhamento?",
    "Existe processo padrao?",
    "Equipes seguem o processo?",
    "Existem indicadores?",
    "Existem metas?",
    "Causas dos problemas sao analisadas?",
    "Melhorias sao acompanhadas?"
]

nomes_niveis = {
    1: "Inicial",
    2: "Gerenciado",
    3: "Definido",
    4: "Gerenciado quantitativamente",
    5: "Em otimizacao"
}


def calcular_maturidade(respostas):
    # Cada etapa precisa estar completa antes de avancar.
    # Neste trabalho, completa significa todas as notas iguais a 2.
    if any(nota < 2 for nota in respostas[0:4]):
        return 1
    if any(nota < 2 for nota in respostas[4:6]):
        return 2
    if any(nota < 2 for nota in respostas[6:8]):
        return 3
    if any(nota < 2 for nota in respostas[8:10]):
        return 4
    return 5


def main():
    print("AVALIADOR SIMPLIFICADO DE MATURIDADE CMMI")
    print("0 - Nao | 1 - Parcialmente | 2 - Sim")
    respostas = []

    for pergunta in perguntas:
        print("\n" + pergunta)
        while True:
            resposta = input("Resposta (0, 1 ou 2): ").strip()
            if resposta in ["0", "1", "2"]:
                respostas.append(int(resposta))
                break
            print("Resposta invalida. Digite 0, 1 ou 2.")

    media = sum(respostas) / len(respostas)
    nivel = calcular_maturidade(respostas)

    print("\nRESULTADO")
    print(f"Pontuacao: {sum(respostas)} de 20")
    print(f"Media: {media:.2f}")
    print(f"Nivel estimado: {nivel} - {nomes_niveis[nivel]}")
    print("O nivel depende das etapas completas, e nao apenas da media.")
    print("Esta e uma simulacao didatica.")

    print("\nPontos que precisam melhorar:")
    for pergunta, nota in zip(perguntas, respostas):
        if nota < 2:
            print("-", pergunta, "Nota:", nota)
    if nivel == 5:
        print("Todas as praticas foram atendidas. Manter a melhoria continua.")


if __name__ == "__main__":
    main()
