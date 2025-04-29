import time

def absolute_error(aprox_x, real_x):
  return abs(aprox_x - real_x)


def relative_error(absolute_error_value, real_x):
  return (absolute_error_value/(abs(real_x)))

f3 = lambda x: x**5 - 2 * x**4 - 9 * x**3 + 22 * x**2 + 4 * x - 24
  
def falsa_posicao_method(a, b, epsilon, f3):
  start_time = time.time()

  fa = f3(a)
  fb = f3(b)

  if fa * fb >= 0:
    raise Exception("f(a) e f(b) devem ter sinais opostos.")

  x = (a*fb - b*fa)/(fb - fa)

  fx = f3(x)

  count = 0

  while abs(fx) > epsilon:
    if(fa * fx < 0):
      b = x
      fb = fx
    else:
      a = x
      fa = fx

    x = (a*fb - b*fa)/(fb - fa)
    fx = f3(x)
    count += 1

  end_time = time.time()
  calculated_time = end_time - start_time

  print("O método da falsa posição iterou sobre a função f3 {} vezes".format(count))
  print("Tempo de execução: {:.6f} segundos".format(calculated_time))

  return x

epsilon = 10**(-10)
# Executando o método
real_x = 2
aproximate_x = falsa_posicao_method(1.8, 2.2, epsilon, f3)

print("A raiz encontrada pelo método da falsa posição é: {}".format(aproximate_x))

absolute_error_value = absolute_error(aproximate_x, real_x)
relative_error_value = relative_error(absolute_error_value, real_x)

print(f"O erro absoluto da falsa posição é: {absolute_error_value:.10f}")
print(f"O erro relativo da falsa posição é: {relative_error_value:.10f}")
