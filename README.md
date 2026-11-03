# Máquina Estatística

Simulador acadêmico desenvolvido em Python para o Trabalho I da disciplina de Probabilidade e Estatística I, do curso de Sistemas de Informação do IFES, Campus Serra, período 2026/2.

O programa simula uma máquina de rolos com três posições independentes. O jogador utiliza créditos fictícios e recebe um prêmio quando os três símbolos da linha central são iguais.

## Requisitos

- Python 3.10 ou superior.
- pandas
- NumPy
- Matplotlib

## Instalação

Clone o repositório e acesse a pasta do projeto.

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Na pasta raiz do projeto, execute:

```bash
python src/simulador.py
```

O programa apresenta uma rodada de exemplo e executa automaticamente os cinco experimentos. Ao finalizar, os arquivos gerados ficam organizados nas pastas `resultados/` e `graficos/`.

O programa também pode ser executado diretamente da pasta raiz, caso o arquivo `simulador.py` esteja localizado nela:

```bash
python simulador.py
```

## Experimentos

O simulador executa os seguintes experimentos:

**E1 - Frequências observadas:** realiza 10.000 rodadas com semente 2026 e compara as frequências obtidas com as probabilidades teóricas.

**E2 - Médias acumuladas:** executa três sequências de 10.000 rodadas, utilizando as sementes 10, 2026 e 123456. Compara as médias acumuladas e verifica a reprodução dos dez primeiros resultados com a semente 2026.

**E3 - Participantes com saldo limitado:** simula 100 participantes, cada um com saldo inicial de 100 créditos e limite de 500 rodadas. A sessão termina quando o saldo fica abaixo de 1 crédito ou quando o limite de rodadas é atingido.

**E4 - Probabilidade condicional:** analisa os 9.999 pares consecutivos do E1 para comparar a frequência de prêmios após uma rodada premiada e após uma rodada sem prêmio.

**E5 - Aumento dos prêmios:** compara a tabela de pagamentos original com outra que aumenta todos os prêmios em 10%, utilizando os mesmos resultados do E1.

## Arquivos de resultados

Os arquivos CSV são salvos automaticamente na pasta `resultados/`.

| Arquivo | Descrição |
|---|---|
| `experimento1_rodadas.csv` | Resultados individuais das 10.000 rodadas do E1. |
| `experimento1_frequencias.csv` | Probabilidades teóricas, contagens e frequências observadas. |
| `experimento1_resumo.csv` | Lucro médio, desvio-padrão, RTP e proporção de rodadas premiadas. |
| `experimento2_medias_acumuladas.csv` | Médias acumuladas das três sequências. |
| `experimento2_reproducibilidade.csv` | Resultado da conferência dos dez primeiros resultados com a semente 2026. |
| `experimento3_participantes.csv` | Saldo final, quantidade de rodadas, esgotamento e classificação dos participantes. |
| `experimento3_resumo.csv` | Resumo estatístico dos participantes. |
| `experimento3_trajetorias.csv` | Trajetórias dos cinco primeiros participantes. |
| `experimento4_condicional.csv` | Frequências observadas e probabilidades condicionais. |
| `experimento5_comparacao.csv` | Comparação dos pagamentos, lucros médios e RTP. |

Os gráficos são salvos automaticamente na pasta `graficos/`.

| Arquivo | Descrição |
|---|---|
| `e1_frequencias.png` | Comparação entre probabilidades teóricas e frequências observadas. |
| `e2_medias_acumuladas.png` | Evolução das médias acumuladas nas três sequências. |
| `e3_trajetorias.png` | Evolução do saldo dos cinco primeiros participantes. |
| `e5_rtp.png` | Comparação entre o RTP teórico e observado nas duas tabelas de pagamentos. |

O E4 apresenta seus resultados em tabela, sem gerar um gráfico.

## Parâmetros principais

| Parâmetro | Valor |
|---|---|
| Símbolos | A, B, C, D e E |
| Aposta por rodada | 1 crédito |
| Prêmios | A = 5, B = 10, C = 15, D = 25 e E = 50 créditos |
| Rodadas do E1 | 10.000 |
| Sementes do E1 | 2026 |
| Sementes do E2 | 10, 2026 e 123456 |
| Semente do E3 | 42 |
| Participantes do E3 | 100 |
| Saldo inicial do E3 | 100 créditos
