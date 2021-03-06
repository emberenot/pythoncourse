#Напишите генератор frange как аналог range() с дробным шагом.


#start = 1
#stop = 10
#step = 0.1
#while start < stop - step:
#    round(start, 1)
#    start += step
#    print(start)


def frange(start, stop, step):
    while start < stop - step:
        yield round(start, 1)
        start += step

[print(i, end = "\n") for i in frange(1, 25, 0.3)]
