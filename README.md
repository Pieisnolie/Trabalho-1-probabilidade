# Máquina Estatística

Simulador acadêmico desenvolvido em Python para o Trabalho I da disciplina de Probabilidade e Estatística I, do curso de Sistemas de Informação do IFES, Campus Serra, período 2026/2.

O projeto simula uma máquina de rolos com três posições independentes. São utilizados cinco símbolos possíveis (A, B, C, D e E), e o jogador recebe um prêmio quando os três símbolos da linha central são iguais.

A simulação utiliza apenas créditos fictícios e tem finalidade didática.

## Requisitos

- Python 3.10 ou superior.
- pandas
- NumPy
- Matplotlib

## Instalação

Crie e ative um ambiente virtual na pasta do projeto:

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

Caso o arquivo `simulador.py` esteja diretamente na raiz do projeto, utilize:

```bash
python simulador.py
```

O programa apresenta uma rodada de exemplo e executa automaticamente os cinco experimentos. Ao finalizar, os arquivos gerados ficam organizados nas pastas `resultados/` e `graficos/`.

## Experimentos

**E1 - Frequências observadas**

Executa 10.000 rodadas com a semente 2026 e compara as frequências observadas com as probabilidades teóricas. Calcula também o lucro médio, o desvio-padrão amostral, o RTP observado e a proporção de rodadas premiadas.

**E2 - Médias acumuladas**

Executa três sequências de 10.000 rodadas, utilizando as sementes 10, 2026 e 123456. Compara as médias acumuladas após 100, 1.000 e 10.000 rodadas e verifica a reprodução dos dez primeiros resultados com a semente 2026.

**E3 - Participantes com saldo limitado**

Simula 100 participantes, cada um com saldo inicial de 100 créditos e limite de 500 rodadas. A sessão termina quando o saldo fica abaixo de 1 crédito ou quando o limite de rodadas é atingido.

**E4 - Probabilidade condicional**

Analisa os 9.999 pares consecutivos do E1 para comparar a frequência de prêmios após uma rodada premiada e após uma rodada sem prêmio.

**E5 - Aumento dos prêmios**

Compara a tabela de pagamentos original com outra que aumenta todos os prêmios em 10%, utilizando os mesmos resultados do E1.

## Arquivos de resultados

Os arquivos CSV são salvos automaticamente na pasta `resultados/`.

| Arquivo | Descrição |
|---|---|
| `experimento1_rodadas.csv` | Resultados individuais das 10.000 rodadas do E1. |
| `experimento1_frequencias.csv` | Probabilidades teóricas, contagens e frequências observadas do E1. |
| `experimento1_resumo.csv` | Lucro médio, desvio-padrão, RTP e proporção de rodadas premiadas. |
| `experimento2_medias_acumuladas.csv` | Médias acumuladas das três sequências do E2. |
| `experimento2_reproducibilidade.csv` | Resultado da conferência dos dez primeiros resultados com a semente 2026. |
| `experimento3_participantes.csv` | Dados individuais dos 100 participantes do E3. |
| `experimento3_resumo.csv` | Resumo estatístico dos participantes do E3. |
| `experimento3_trajetorias.csv` | Trajetórias dos cinco primeiros participantes. |
| `experimento4_condicional.csv` | Frequências e probabilidades condicionais do E4. |
| `experimento5_comparacao.csv` | Comparação dos pagamentos, lucros médios e RTP do E5. |

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
| Prêmio A-A-A | 5 créditos |
| Prêmio B-B-B | 10 créditos |
| Prêmio C-C-C | 15 créditos |
| Prêmio D-D-D | 25 créditos |
| Prêmio E-E-E | 50 créditos |
| Rodadas do E1 | 10.000 |
| Semente do E1 | 2026 |
| Sementes do E2 | 10, 2026 e 123456 |
| Semente do E3 | 42 |
| Participantes do E3 | 100 |
| Saldo inicial do E3 | 100 créditos |
| Limite de rodadas do E3 | 500 |

O gerador pseudoaleatório utilizado é o Mersenne Twister, disponibilizado pelo módulo `random` do Python. A semente é inicializada uma vez no início de cada sequência, permitindo reproduzir os resultados nas mesmas condições de execução.

## Verificações de reprodução

O programa realiza duas verificações durante a execução:

- No E2, compara os dez primeiros resultados de uma nova execução com semente 2026 com os resultados originais do E1.
- No E5, verifica se as duas configurações de pagamento utilizam exatamente as mesmas linhas centrais.

Essas verificações estão incorporadas ao próprio simulador. O projeto não possui uma suíte independente de testes automatizados.

## Declaração de uso de inteligência artificial

Utilizei ferramentas de inteligência artificial como apoio ao estudo dos conceitos de probabilidade, à organização do código, à elaboração do relatório, à revisão textual e à busca de referências relacionadas ao tema. Também usei para esclarecer dúvidas sobre os experimentos e melhorar a apresentação das explicações. Entretanto, executei o simulador e conferi os cálculos, as frequências, as médias, a reprodução das sementes e a correspondência entre os dados gerados e os resultados apresentados no relatório.
