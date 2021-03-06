#Напишите собственную версию генератора enumerate под названием extra_enumerate. В переменной cum хранится накопленная сумма на момент текущей
#итерации, в переменной frac – доля накопленной суммы от общей суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
#вывод будет таким: (1, 1, 0.1) (3, 4, 0.4) (4, 8, 0.8) (2, 10, 1).


def extra_enumerate(list):
    cum = 0
    frac = 0
    sum_elem = 0
    for i in list:
        sum_elem += i 
    for i in list:
        cum += i
        frac = cum / sum_elem
        yield i, cum, frac

[print((elem, cum, frac), end="  ") for elem, cum, frac in extra_enumerate([1, 3, 4, 2])]