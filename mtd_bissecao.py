def absolute_error(aprox_x, real_x):
  return abs(aprox_x - real_x)


def relative_error(absolute_error_value, real_x):
  return (absolute_error_value/(abs(real_x)))

def bissecao_method(a, b, epsilon, f3):
  x = (a+b)/2
  fx = f3(x)
  fa = f3(a)
  fb = f3(b)
  count = 0

  if fa * fb >= 0:
        raise Exception("f(a) e f(b) devem ter sinais opostos.")

  while abs(fx) > epsilon:
    if(fa * fx < 0):
      b = x
    else:
      a = x
      fa = fx

    x = (a+b)/2
    fx = f3(x)
    count += 1

  return (x, count)
