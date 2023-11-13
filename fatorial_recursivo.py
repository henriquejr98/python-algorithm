import timeit

def fatorial(x):
    # Base
    if x == 1:
        return 1
    # Recursividade
    else:
        print(x)
        return x * fatorial(x-1)


def fatorial_em_cauda(x, resultado=1):
    if x == 0:
        return resultado
    else:
        return fatorial_em_cauda(x-1, x*resultado)

print(fatorial_em_cauda(5))