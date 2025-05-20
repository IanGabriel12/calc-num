def fixed_point(a, b, phi, precision):
    iterations = 0
    max_iterations = 500

    x = (a + b) / 2
    prev = None

    while iterations < max_iterations:
        prev = x
        x = phi(x)
        error = abs(x - prev)

        if error < precision:
            return (x, iterations)

        iterations += 1

    return (x, iterations)
