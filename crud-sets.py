#conjunto original
set_numbers = set((1,2,3,4,5))
print("=======conjunto original========")
print(set_numbers)

#add (un elemento)
set_numbers.add(6);
print(set_numbers)

#update (un subconjunto)
set_numbers.update((1,2,3,4,5,6,7,8,9))
print(set_numbers)

#delete (sino existe el elemento el programa se detiene)
set_numbers.remove((1))
print(set_numbers)

#delete (con esta forma no genera excepción el programa si el elemento no existe)
set_numbers.discard((2))
print(set_numbers)

#tamaño
print(len(set_numbers))