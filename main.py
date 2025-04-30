import funcoes
import time
from mtd_bissecao import bissecao_method
from mtd_muller import mtd_muller
from mtd_falsa_posicao import falsa_posicao_method
from mtd_secante import mtd_secante
from mtd_ponto_fixo import fixed_point
from mtd_newton import mtd_newton

metodos = [
    ("Bissecção", bissecao_method),
    ("Falsa posição", falsa_posicao_method),
    ("Ponto fixo", fixed_point),
    ("\"Newton\"", mtd_newton),
    ("Secante", mtd_secante),
    ("Muller", mtd_muller)
]

BISSECAO_ID = 0
FALSA_POS_ID = 1
PONTO_FIXO_ID = 2
NEWTON_ID = 3
SECANTE_ID = 4
MULLER_ID = 5

while True:
    print("0 - f(x) = x**2 + x - 6\n1 - f(x) = 2*x**4 + 4*x**3 + 3*x**2 - 10*x - 15\n2 - f(x) = x**5 - 2*x**4 - 9*x**3 + 22*x**2 + 4*x - 24")
    id_funcao = int(input("Digite qual função você pretende rodar: "))
    if id_funcao >= len(funcoes.lista_func):
        print("Digite um número entre 0 e " + len(funcoes.lista_func) - 1)
        continue

    f = funcoes.lista_func[id_funcao]

    a = float(input("Digite o início do intervalo de busca (a): "))
    b = float(input("Digite o fim do intervalo de busca (b): "))
    real = float(input("Digite a raiz real do intervalo: "))

    precision_opt = -1
    while precision_opt != 0 and precision_opt != 1:
        precision_opt = int(input("Digite 0 para precisao de 10**-8 ou 1 para precisao de 10**-10: "))

    precision = 10**(-10) if precision_opt else 10**(-8) 

    print(f"Executando função {id_funcao} no intervalo [{a}, {b}] com precisao de {precision}")

    print(f"{"Método":<20}|{"Raiz encontrada":<20}|{"Qtd. Iterações":<20}|{"Tempo (s)":<10}|{"Erro abs.":<10}|{"Erro rel.":<10}")

    
    for indice, tupla in enumerate(metodos):
        divergiu = False
        nome, func = tupla
        
        start_time = time.time()
        raiz = 0

        if indice == BISSECAO_ID:
            raiz, iteracoes = func(a, b, precision, f)
        elif indice == FALSA_POS_ID:
            raiz, iteracoes = func(a, b, precision, f)
        elif indice == PONTO_FIXO_ID:
            try:
                raiz, iteracoes = func(a, b, funcoes.lista_iter_func[id_funcao], precision)
            except:
                divergiu = True
        elif indice == MULLER_ID:
            raiz, iteracoes = func(f, a, b, precision)
        elif indice == NEWTON_ID:
            raiz, iteracoes = func(f, funcoes.lista_derivadas[id_funcao], a, b, precision)
        elif indice == SECANTE_ID:
            raiz, iteracoes = func(f, a, b, precision)


        end_time = time.time()
        tempo_segundos = end_time - start_time
        erro_abs = abs(raiz - real)
        erro_rel = erro_abs / real
        
        raiz_formatted = f"{raiz:.8f}".ljust(20) if not divergiu else f"Divergiu".ljust(20)
        tempo_formatted = f"{tempo_segundos:.8f}".ljust(10)
        erro_abs_formatted = f"{erro_abs:.8f}".ljust(10)
        erro_rel_formatted = f"{erro_rel:.8f}".ljust(10)

        print(f"{nome:<20}|{raiz_formatted}|{iteracoes:<20}|{tempo_formatted}|{erro_abs_formatted}|{erro_rel_formatted}")



