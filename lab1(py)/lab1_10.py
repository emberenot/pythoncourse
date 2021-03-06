#Напишите скрипт, позволяющий определить надежность вводимого пользователем пароля. Это задание является творческим: алгоритм
#определения надежности разработайте самостоятельно.


password = input("Введите пароль: ")
if len(password)>8 and not password.isdigit() and password.startswith('!'):
	print("Плохой пароль!")
else:
	print("Пароль надёжный")