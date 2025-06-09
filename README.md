# calc-num
Arquivos da disciplina de cálculo numérico

## Como usar
Apenas rode o comando:
```
python3 main.py
```
e seja feliz!


## Código da unidade 2

Tudo referente a segunda unidade está contido no diretório `mtds_U2`, para executar o código é necessário ter algumas dependências, que podem ser instaladas seguindo as seguintes intruções:

```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Feito isso, há dois executaveis:

### Código da Lista 2

Para executar e verificar os resultados da questões solucionadas da lista, basta executar:

```python
python3 main.py
```


### Resultados com as matrizes do Matrix Market

Para executar o código utilizando como entradas as matrizes disponibilizadas, basta executar:

```python3
python3 mtds_U2/sistemas_lineares/resolucao_das_matrizes.py "<nome_do_metodo>" 
```

Onde `<nome_do_metodo>` pode ser umas das seguintes opções:


- `gauss` : Resolução pelo método de Eliminação de Gauss
- `fatoracao_lu`: Resolução por fatoração L.U
- `gauss_jacobi`: Resolução por Gauss-Jacobi
- `gauss_jacobi2`: Resolução por Gauss-Jacobi implementado com numpy (Mais rápido)
- `gauss_seidel`: Resolução por Gauss-Seidel



