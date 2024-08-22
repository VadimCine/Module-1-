immutable_var = "Луна", 55, 12.5
print(immutable_var)
immutable_var [0] = "Земля" #Кортеж не поддерживат обращение по элементам, поэтому элемент таким образом изменить нельзя.

mutable_list = [25, 55.5, "Осень"]
mutable_list[0] = 5
mutable_list[1] = 50
mutable_list[2] = "Лето"
print(mutable_list)