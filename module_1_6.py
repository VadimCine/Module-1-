my_dict = {'Олег': 1995, 'Игорь' : 1990, 'Мария' : 1999}
print(my_dict)
print(my_dict['Олег'])
print(my_dict.get('Михаил'))
my_dict.update({'Вадим': 1990,
                'Дарья': 1992})
b = my_dict.pop('Игорь')
print(b)
print(my_dict)

my_set = {1, 2, 3, 4, 3, 3, 4, 1, False, (66,44,88)}
print(my_set)
my_set.add(12.5)
my_set.add('Moon')
my_set.discard(1)
print(my_set)