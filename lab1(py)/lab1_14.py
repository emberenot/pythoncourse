#Напишите декоратор non_empty, который дополнительно проверяет списковый результат любой функции: если в нем содержатся пустые
#строки или значение None, то они удаляются. Пример кода:
#@non_empty
#def get_pages():
#return ['chapter1', '', 'contents', '', 'line1'].


def non_empty(fn):
    def wrapped():
        return list(filter(None, fn()))
    return wrapped

@non_empty
def get_pages():
    return ['prindaaw', 'dawdawfna', '', 'halo1', '']

print(get_pages())