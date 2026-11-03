from __future__ import annotations

import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Configurações da máquina
SIMBOLOS = ("A", "B", "C", "D", "E")

PREMIOS = {
    "A": 5.0,
    "B": 10.0,
    "C": 15.0,
    "D": 25.0,
    "E": 50.0,
}

APOSTA = 1.0
QUANTIDADE_RODADAS = 10_000

# Permite executar o arquivo na raiz ou dentro da pasta src.
PASTA_ARQUIVO = Path(__file__).resolve().parent
PASTA_RAIZ = (
    PASTA_ARQUIVO.parent
    if PASTA_ARQUIVO.name == "src"
    else PASTA_ARQUIVO
)

PASTA_RESULTADOS = PASTA_RAIZ / "resultados"
PASTA_GRAFICOS = PASTA_RAIZ / "graficos"

PASTA_RESULTADOS.mkdir(parents=True, exist_ok=True)
PASTA_GRAFICOS.mkdir(parents=True, exist_ok=True)


def girar_roleta(gerador, tabela_premios=PREMIOS):
    """Sorteia três rolos independentes e avalia somente a linha central."""
    simbolos_sorteados = [
        SIMBOLOS[(gerador.randrange(5) + 1) % 5]
        for _ in range(3)
    ]

    if (
        simbolos_sorteados[0]
        == simbolos_sorteados[1]
        == simbolos_sorteados[2]
    ):
        premio = float(tabela_premios[simbolos_sorteados[0]])
    else:
        premio = 0.0

    lucro = premio - APOSTA

    return simbolos_sorteados, premio, lucro


def executar_sequencia(semente, quantidade=QUANTIDADE_RODADAS,
                       tabela_premios=PREMIOS):
    """Executa uma sequência de rodadas usando uma semente definida."""
    gerador = random.Random(semente)
    dados = []

    for rodada in range(1, quantidade + 1):
        simbolos, premio, lucro = girar_roleta(
            gerador,
            tabela_premios
        )

        dados.append({
            "rodada": rodada,
            "linha_central": "-".join(simbolos),
            "premio_bruto": premio,
            "lucro_liquido": lucro,
            "premiada": int(premio > 0),
        })

    return pd.DataFrame(dados)


def salvar_grafico_barras(
    dados,
    legendas,
    titulo,
    nome_eixo_y,
    nome_arquivo,
    series,
):
    """Gera e salva um gráfico de barras com uma ou mais séries."""
    posicoes = np.arange(len(legendas))
    largura = 0.35

    plt.figure(figsize=(9, 5))

    for indice, (coluna, legenda) in enumerate(series):
        deslocamento = (
            indice - (len(series) - 1) / 2
        ) * largura

        plt.bar(
            posicoes + deslocamento,
            dados[coluna],
            largura,
            label=legenda,
        )

    plt.xticks(posicoes, legendas)
    plt.xlabel("Resultado")
    plt.ylabel(nome_eixo_y)
    plt.title(titulo)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        PASTA_GRAFICOS / nome_arquivo,
        dpi=180
    )

    plt.close()
def salvar_grafico_e1(dados):
    fig, (eixo1, eixo2) = plt.subplots(
        1, 2,
        figsize=(12, 5),
        gridspec_kw={"width_ratios": [1, 2]}
    )

    cores = ["#4472C4", "#ED7D31"]

    # Painel 1: resultado sem prêmio
    sem_premio = dados[dados["resultado"] == "Sem prêmio"]

    posicoes = np.arange(len(sem_premio))
    largura = 0.35

    eixo1.bar(
        posicoes - largura / 2,
        sem_premio["probabilidade_teorica"] * 100,
        largura,
        label="Probabilidade teórica",
        color=cores[0]
    )

    eixo1.bar(
        posicoes + largura / 2,
        sem_premio["frequencia_observada"] * 100,
        largura,
        label="Frequência observada",
        color=cores[1]
    )

    eixo1.set_title("Sem prêmio")
    eixo1.set_ylabel("Frequência (%)")
    eixo1.set_xticks(posicoes)
    eixo1.set_xticklabels(sem_premio["resultado"])
    eixo1.set_ylim(0, 100)

    # Painel 2: combinações premiadas
    premiadas = dados[dados["resultado"] != "Sem prêmio"]

    posicoes = np.arange(len(premiadas))

    eixo2.bar(
        posicoes - largura / 2,
        premiadas["probabilidade_teorica"] * 100,
        largura,
        label="Probabilidade teórica",
        color=cores[0]
    )

    eixo2.bar(
        posicoes + largura / 2,
        premiadas["frequencia_observada"] * 100,
        largura,
        label="Frequência observada",
        color=cores[1]
    )

    eixo2.set_title("Combinações premiadas")
    eixo2.set_ylabel("Frequência (%)")
    eixo2.set_xticks(posicoes)
    eixo2.set_xticklabels(premiadas["resultado"])
    eixo2.set_ylim(0, 2)

    fig.suptitle(
        "E1 — Probabilidades teóricas e frequências observadas"
    )

    eixo1.legend()
    eixo2.legend()
    plt.tight_layout()

    plt.savefig(
        PASTA_GRAFICOS / "e1_frequencias.png",
        dpi=180
    )

    plt.close()

def experimento_1():
    """Compara as probabilidades teóricas com as frequências observadas."""
    dados = executar_sequencia(2026)

    dados.to_csv(
        PASTA_RESULTADOS / "experimento1_rodadas.csv",
        index=False,
        encoding="utf-8-sig",
    )

    valores = [
        ("Sem prêmio", -1, 120 / 125),
        ("A-A-A", 4, 1 / 125),
        ("B-B-B", 9, 1 / 125),
        ("C-C-C", 14, 1 / 125),
        ("D-D-D", 24, 1 / 125),
        ("E-E-E", 49, 1 / 125),
    ]

    linhas = []

    for nome, lucro, probabilidade in valores:
        contagem = int(
            (dados["lucro_liquido"] == lucro).sum()
        )

        linhas.append({
            "resultado": nome,
            "lucro_por_rodada": lucro,
            "probabilidade_teorica": probabilidade,
            "contagem_observada": contagem,
            "frequencia_observada": contagem / len(dados),
        })

    frequencias = pd.DataFrame(linhas)

    frequencias.to_csv(
        PASTA_RESULTADOS / "experimento1_frequencias.csv",
        index=False,
        encoding="utf-8-sig",
    )

    resumo = {
        "rodadas": len(dados),
        "semente": 2026,
        "lucro_medio": dados["lucro_liquido"].mean(),
        "desvio_padrao_amostral": dados["lucro_liquido"].std(ddof=1),
        "rtp_observado_pct": 100 * dados["premio_bruto"].mean(),
        "proporcao_premiadas_pct": 100 * dados["premiada"].mean(),
    }

    pd.DataFrame([resumo]).to_csv(
        PASTA_RESULTADOS / "experimento1_resumo.csv",
        index=False,
        encoding="utf-8-sig",
    )

    salvar_grafico_e1(frequencias)

    return dados


def experimento_2(dados_iniciais):
    """Compara as médias acumuladas para três sementes."""
    linhas = []
    trajetorias = {}

    for semente in (10, 2026, 123456):
        dados = (
            dados_iniciais
            if semente == 2026
            else executar_sequencia(semente)
        )

        medias = (
            dados["lucro_liquido"].cumsum()
            / np.arange(1, len(dados) + 1)
        )

        trajetorias[semente] = medias

        for quantidade in (100, 1000, 10000):
            linhas.append({
                "semente": semente,
                "rodadas": quantidade,
                "media_acumulada": medias.iloc[quantidade - 1],
            })

    pd.DataFrame(linhas).to_csv(
        PASTA_RESULTADOS / "experimento2_medias_acumuladas.csv",
        index=False,
        encoding="utf-8-sig",
    )

    repeticao = executar_sequencia(2026, 10)

    reproduzido = bool(
        (
            repeticao["linha_central"].values
            == dados_iniciais.head(10)["linha_central"].values
        ).all()
    )

    pd.DataFrame([{
        "semente": 2026,
        "primeiros_10_reproduzidos": reproduzido,
    }]).to_csv(
        PASTA_RESULTADOS / "experimento2_reproducibilidade.csv",
        index=False,
        encoding="utf-8-sig",
    )

    plt.figure(figsize=(9, 5))

    for semente, medias in trajetorias.items():
        plt.plot(
            np.arange(1, 10001),
            medias,
            label=f"Semente {semente}",
            linewidth=0.8,
        )

    plt.axhline(
        -0.16,
        linestyle="--",
        label="Esperança = -0,16"
    )

    plt.xlabel("Rodadas")
    plt.ylabel("Lucro médio acumulado (créditos)")
    plt.title("E2 — médias acumuladas")
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        PASTA_GRAFICOS / "e2_medias_acumuladas.png",
        dpi=180
    )

    plt.close()


def experimento_3():
    """Simula 100 participantes com saldo inicial de 100 créditos."""
    gerador = random.Random(42)

    participantes = []
    trajetorias = []

    for numero_participante in range(1, 101):
        saldo = 100.0
        caminho = [saldo]
        quantidade_rodadas = 0

        while quantidade_rodadas < 500 and saldo >= APOSTA:
            _, _, lucro = girar_roleta(gerador)

            saldo += lucro
            quantidade_rodadas += 1
            caminho.append(saldo)

        if saldo > 100:
            classificacao = "ganho"
        elif saldo == 100:
            classificacao = "empate"
        else:
            classificacao = "perda"

        participantes.append({
            "participante": numero_participante,
            "saldo_inicial": 100,
            "saldo_final": saldo,
            "rodadas": quantidade_rodadas,
            "esgotamento": int(saldo < APOSTA),
            "classificacao": classificacao,
        })

        trajetorias.append(caminho)

    dados_participantes = pd.DataFrame(participantes)

    dados_participantes.to_csv(
        PASTA_RESULTADOS / "experimento3_participantes.csv",
        index=False,
        encoding="utf-8-sig",
    )

    resumo = {
        "participantes": 100,
        "ganho_qtd": int(
            (dados_participantes["classificacao"] == "ganho").sum()
        ),
        "ganho_pct": 100 * (
            dados_participantes["classificacao"] == "ganho"
        ).mean(),
        "empate_qtd": int(
            (dados_participantes["classificacao"] == "empate").sum()
        ),
        "empate_pct": 100 * (
            dados_participantes["classificacao"] == "empate"
        ).mean(),
        "perda_qtd": int(
            (dados_participantes["classificacao"] == "perda").sum()
        ),
        "perda_pct": 100 * (
            dados_participantes["classificacao"] == "perda"
        ).mean(),
        "esgotamento_qtd": int(
            dados_participantes["esgotamento"].sum()
        ),
        "esgotamento_pct": 100 * (
            dados_participantes["esgotamento"].mean()
        ),
        "saldo_medio_final": dados_participantes["saldo_final"].mean(),
        "saldo_mediano_final": dados_participantes["saldo_final"].median(),
    }

    pd.DataFrame([resumo]).to_csv(
        PASTA_RESULTADOS / "experimento3_resumo.csv",
        index=False,
        encoding="utf-8-sig",
    )

    registros = []

    for numero_participante, caminho in enumerate(trajetorias[:5], 1):
        caminho_completo = (
            caminho + [caminho[-1]] * (501 - len(caminho))
        )

        for rodada, saldo in enumerate(caminho_completo):
            registros.append({
                "participante": numero_participante,
                "rodada": rodada,
                "saldo": saldo,
            })

    pd.DataFrame(registros).to_csv(
        PASTA_RESULTADOS / "experimento3_trajetorias.csv",
        index=False,
        encoding="utf-8-sig",
    )

    plt.figure(figsize=(9, 5))

    for numero_participante, caminho in enumerate(trajetorias[:5], 1):
        caminho_completo = (
            caminho + [caminho[-1]] * (501 - len(caminho))
        )

        plt.plot(
            range(501),
            caminho_completo,
            label=f"Participante {numero_participante}",
        )

    plt.xlabel("Rodada")
    plt.ylabel("Saldo (créditos)")
    plt.title("E3 — cinco primeiras trajetórias")
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        PASTA_GRAFICOS / "e3_trajetorias.png",
        dpi=180
    )

    plt.close()

    return dados_participantes


def experimento_4(dados):
    """Calcula a frequência de prêmio após prêmio e após não prêmio."""
    resultados_anteriores = dados["premiada"].iloc[:-1].to_numpy()
    resultados_seguintes = dados["premiada"].iloc[1:].to_numpy()

    linhas = []

    for nome, condicao in (
        ("Após prêmio", resultados_anteriores == 1),
        ("Após não prêmio", resultados_anteriores == 0),
    ):
        total = int(condicao.sum())
        premios_seguinte = int(resultados_seguintes[condicao].sum())

        linhas.append({
            "resultado_anterior": nome,
            "total_pares": total,
            "premios_seguinte": premios_seguinte,
            "proporcao_observada": (
                premios_seguinte / total if total else None
            ),
            "referencia_teorica": 0.04,
        })

    pd.DataFrame(linhas).to_csv(
        PASTA_RESULTADOS / "experimento4_condicional.csv",
        index=False,
        encoding="utf-8-sig",
    )


def experimento_5(dados_iniciais):
    """Compara a tabela original com pagamentos aumentados em 10%."""
    linhas = []

    for nome_tabela, multiplicador in (
        ("Base", 1.0),
        ("Prêmios +10%", 1.1),
    ):
        nova_tabela = {
            simbolo: valor * multiplicador
            for simbolo, valor in PREMIOS.items()
        }

        dados = executar_sequencia(
            2026,
            QUANTIDADE_RODADAS,
            nova_tabela
        )

        # Garante que a comparação use exatamente as mesmas rodadas.
        assert (
            dados["linha_central"].values
            == dados_iniciais["linha_central"].values
        ).all()

        linhas.append({
            "tabela": nome_tabela,
            "probabilidade_teorica_premio_pct": 4,
            "frequencia_observada_premio_pct": (
                100 * dados["premiada"].mean()
            ),
            "premio_medio_observado": dados["premio_bruto"].mean(),
            "lucro_medio_observado": dados["lucro_liquido"].mean(),
            "rtp_teorico_pct": 84 * multiplicador,
            "rtp_observado_pct": 100 * dados["premio_bruto"].mean(),
        })

    comparacao = pd.DataFrame(linhas)

    comparacao.to_csv(
        PASTA_RESULTADOS / "experimento5_comparacao.csv",
        index=False,
        encoding="utf-8-sig",
    )

    salvar_grafico_barras(
        dados=comparacao,
        legendas=comparacao["tabela"],
        titulo="E5 — comparação do RTP",
        nome_eixo_y="RTP (%)",
        nome_arquivo="e5_rtp.png",
        series=[
            ("rtp_teorico_pct", "RTP teórico"),
            ("rtp_observado_pct", "RTP observado"),
        ],
    )


def principal():
    print("Simulador acadêmico — somente créditos fictícios")
    print("1) Exibir uma rodada")

    gerador = random.Random(2026)

    simbolos, premio, lucro = girar_roleta(gerador)

    print(
        "Linha central:",
        "-".join(simbolos),
        "Prêmio:",
        premio,
        "Lucro:",
        lucro,
    )

    print("Executando os cinco experimentos...")

    dados_iniciais = experimento_1()

    experimento_2(dados_iniciais)
    experimento_3()
    experimento_4(dados_iniciais)
    experimento_5(dados_iniciais)

    print(
        "Concluído. Consulte as pastas resultados/ e graficos/."
    )


if __name__ == "__main__":
    principal()