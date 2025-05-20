def falsa_posicao_method(a, b, epsilon, f3):
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

    if count >= 500:
        break

  return (x, count)
