#operaciones con conjuntos
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#union
set_c = set_a.union(set_b) # o tambien con un operador "set_a | set_b"
print(set_c)

#intercepcion
set_c = set_a.intersection(set_b) # o tambien con un operador "set_a & set_b"
print(set_c)

#diferencia
set_c = set_a.difference(set_b) # o tambien con un operador "set_a - set_b"
print(set_c)

#diferencia simetrica (hacer una union sin lso elementos que tienen en conjunto)
set_c = set_a.symmetric_difference(set_b)# o tambien con un operador "set_a ^ set_b"
print(set_c)