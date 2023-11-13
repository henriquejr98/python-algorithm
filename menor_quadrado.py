def dividir_conquistar(x, y):
    if x > y:
        if x == 2*y:
            return y
        else:
            x = ((x % y)/y) * y
            return dividir_conquistar(x, y)
    else:
        if y == 2*x:
            return x
        else:
            y = ((y % x)/x) * x
            return dividir_conquistar(x, y)

print(dividir_conquistar(1680,640))

