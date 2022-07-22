# Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.
my_list = ["kdk", "lsl", "kdk", "ryr", "trt"]
count = 0
for i in range(len(my_list)):
    if my_list[i] == "kdk":
        count += 1
        
        if count > 1:
            print(i)
            break