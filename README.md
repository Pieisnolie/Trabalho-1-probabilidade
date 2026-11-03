# Máquina Estatística — Trabalho I

Simulador acadêmico para Probabilidade e Estatística I (IFES — Campus Serra, 2026/2).

## Requisitos
- Python 3.10 ou superior
- pandas
- numpy
- matplotlib

## Instalação
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

## Execução
Na raiz do projeto:
```bash
python src/simulador.py
```
O programa exibe uma rodada e executa os cinco experimentos. Os CSVs são gravados em `resultados/` e os gráficos em `graficos/`.

## Testes automatizados
```bash
python -m unittest discover -s testes -v
```
Os testes verificam pagamentos, desconto da aposta, reprodutibilidade, quantidade de rodadas, símbolos e regra de premiação.

## Arquivos de resultados
- `experimento1_rodadas.csv`: 10.000 rodadas da semente 2026.
- `experimento1_frequencias.csv` e `experimento1_resumo.csv`: distribuição e estatísticas.
- `experimento2_medias_acumuladas.csv`: médias nas sementes 10, 2026 e 123456.
- `experimento2_reproducibilidade.csv`: conferência dos dez primeiros resultados.
- `experimento3_participantes.csv`, `experimento3_resumo.csv` e `experimento3_trajetorias.csv`: sessões com saldo limitado.
- `experimento4_condicional.csv`: frequências condicionais.
- `experimento5_comparacao.csv`: comparação das tabelas de pagamento.
- `testes_automatizados.txt`: saída registrada dos testes.

## Parâmetros principais
Aposta: 1 crédito. Símbolos: A, B, C, D e E. Pagamentos: 5, 10, 15, 25 e 50 créditos. Sementes: E1 = 2026; E2 = 10, 2026 e 123456; E3 = 42. O gerador é inicializado uma vez por sequência, conforme o enunciado.

## Declaração de uso de IA
Foi utilizada ferramenta de IA como apoio à organização do código, elaboração inicial do relatório e revisão dos cálculos. 

