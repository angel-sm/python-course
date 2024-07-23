"""
a -> main function
b -> decorator function
c -> Colocamos el codigo que queremos ejecutar
"""

def fucntion_a(function_b):
    def function_c():
        print("Antes del llamado de b")
        function_b()
        print("Despues del llamado")

    return function_c


def decorator(function_b):
    def function_c(*args, **kwargs):
       print(args, kwargs)
       result = function_b(*args, **kwargs)
       return result
    return function_c

@decorator
def add(one, two):
    return one + two

@fucntion_a
def saludar():
    print("Hola")


@fucntion_a
def adios():
    print("Adios")

# saludar()
# adios()
print(add(1, 20))