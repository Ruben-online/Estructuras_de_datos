# Investigar y trabajar las operaciones basicas entre conjuntos

# Crear conjuntos
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 6, 7}

# Union de conjuntos
uni_result = a.union(b)
print('Union: ', uni_result)

# Interseccion de conjuntos
inter_result = a.intersection(b)
print('Interseccion:  ', inter_result)

# Diferencia de conjuntos a-b
diff_result = a.difference(b)
print('Diferencia a-b : ', diff_result)

# Difernecia de conjuntos b-a
diff_result2 = b.difference(a)
print('Diferencia b-a', diff_result2)

# Diferencia simetrica
sim_diff = a.symmetric_difference(b)
print('Diferencia simetrica: ', sim_diff)

# Verificar si es subconjunto a-b
sub_set = a.issubset(b)
print('a es subconjunto de b: ', sub_set)

# Verificar si es superconjunto a-b
super_set = a.issuperset(b)
print('a es superconjunto de b: ', super_set)

# Comprobar si son disjuntos
dis_set = a.isdisjoint(b)
print('a y b son disjuntos: ', dis_set)

# Los conjuntos inmutables son aquellos a los cuales no se pueden modificar despues de ser creador

inmu_set = frozenset([11, 12, 13, 14, 15])