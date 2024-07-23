def pares():
    for numero in range(0, 100, 2):
        yield numero
        print('Se reanuda la ejecucion')

generator = pares()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))