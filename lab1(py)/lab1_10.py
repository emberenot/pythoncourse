#Напишите скрипт, позволяющий определить надежность вводимого пользователем пароля. Это задание является творческим: алгоритм
#определения надежности разработайте самостоятельно.


password = input("Введите пароль: ")
if len(password)>8 and not password.isdigit():
	print("Пароль надёжный")
else:
	print("Плохой пароль!")
