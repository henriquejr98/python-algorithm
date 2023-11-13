def half(x):
    return x / 2

counter = 0
x = 200
while x > 1:
    print(x)
    x = half(x)
    counter += 1
print(f'COUNTER -> {counter}')