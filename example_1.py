# Задайте список. Напишите проограмму, которая определит,
# присутсвует ли в заданном списке строк некое число.
# ПРИМЕР: 12 -> ['asd12', '12', 'asd', '87'] -> 'asd12', '12'

my_list = ['123', 'asd32', '67', '7823', '23', '92', 'rhe', 'lme23']
for i in my_list:
    if '23' in i:
        print(i) 
        