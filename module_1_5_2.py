immutable_var = 1, 5, 'дом', True
print(immutable_var)
# immutable_var[0] = 7 содержимое кортежей не подлежит изменениям
mutable_var = [2, 3, "звезда", False]
print(mutable_var)
mutable_var[3] = True
mutable_var[1] = 9
print(mutable_var)