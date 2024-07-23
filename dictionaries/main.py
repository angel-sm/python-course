elements = {}

elements["person_one"] = {
    "name": "Cody"
}

print(elements)

cody = elements.get('persone_one')
print(cody)

error_message = elements.get('a', 'a not accessible')
print(error_message)

keys = tuple(elements.keys())
print(keys)

values = tuple(elements.values())
print(values)

items = tuple(elements.items())
print(items)