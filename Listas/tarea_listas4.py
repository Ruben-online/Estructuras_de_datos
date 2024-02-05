# Dadas dos listas, encontrar los elementos que se encuentran en una y no en la otra

list1 = [1, 2, 3, 5, 6]
list2 = [6, 3, 2, 3]

my_set1 = set(list1)
my_set2 = set(list2)

print(my_set1)
print(my_set2)

diff_result = my_set1.difference(my_set2)
print(diff_result)