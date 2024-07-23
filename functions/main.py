def add(one, two): 
    result = one + two
    return result, 'EL resultado es entero'

one = int(input("First number: "))
two = int(input("Second number: "))

result, message = add(one, two)

print(result, message)

# Multiple arguments (n) args
def promedio(*args):
    return sum(args) / len(args)

print(promedio(10, 10, 10, 20))

# Kwards 
def users(**kwargs):
    print(kwargs)

users(angel=[10, 10, 9], luis=[8, 7, 5])
