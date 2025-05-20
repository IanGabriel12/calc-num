"""
Faz o tabelamento da função f no intervalo [a, b] com
passo igual a h

f - Função - Assume-se que é Real -> Real
a - Começo do intervalo
b - Fim do intervalo
h - Tamanho do passo

Observações: f precisa ser contínua em [a, b]
"""
def get_table(f, a, b, h):
    print("x | f(x)")
    x = a
    while x <= b:
        print(f"{x:.3f} | {f(x):.9f}")
        x += h
