

# СПИСКИ - изменяемый, индексируемый 


# КОРТЕЖИ - typle() - не изменяемый, но идексируемый 

# my_tiple = (1, 4, 5 ,7)
# print(my_tiple[1])


# МНОЖЕСТВА - set() - изменяемый, но не идексируемый 

# my_set = set([1, 7, 2, 12, 'asd',  2])    # {1, 7, 2, 12, 2}  , пустое множество {} создать нельзя
# my_set.add(4)
# print(my_set)

# my_set = {1, 7, 2, 12, 'asd',  2}
# for item in {1, 7, 2, 12, 'asd',  2}:
#     print(item)

# сортирует множества на уникальные эллементы



# СЛОВАРИ - dict() - изменяемый, но не индексируемый 

# my_dict = {}
# print(type(my_dict))

# my_dict = {
#     12: 'стол',     # (12, 6):
#     54: 'кровать'
# }

# a = 123
# my_dict = {
#     (12, 6): {
#         'стол': []
#     },    
#     a: 'кровать'
# }

# (my_dict[(12, 6)]) = 'NEW'
# print(my_dict)

# for key in my_dict:
#     print(key)          # ключ

# for key in my_dict:
#     print(my_dict[key])   # значение

# for val in my_dict.values():
#     print(val)              # второй вариант значения 


# for dbl in my_dict.items():
#     print(dbl)               # ключ и значение (кортеж) 2 эллемента

# for key, val in my_dict.items():
#     print(f'key -> {key} val -> {val}')     # ключ и значение (кортеж) 2 эллемента (вариант 2)