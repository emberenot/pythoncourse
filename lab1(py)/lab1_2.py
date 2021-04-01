# #2 Написать скрипт, который выводит на экран «True», если элементы
# программно задаваемого списка представляют собой возрастающую
# последовательность, иначе – «False».



mas = [89, 3, 4, 5]
i = 0
if (i for i in range(len(mas) - 1)):
	if mas[i] <= mas[i + 1]:
		print(True) 
	elif mas[i] >= mas[i + 1]:
		import sys
		sys.exit()
