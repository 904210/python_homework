# реализация структуры "Рейтинг"

lst_rate = [7, 5, 3, 3, 2]
print('Текущий рейтинг', lst_rate)

while True:
    print('для выхода введите 00')
    n = int(input('Введите новый элемент рейтинга: '))
    if n == 00:
        break
    elif n in lst_rate:
        lst_rate.insert(lst_rate.index(n), n)
        print(f'Пользователь ввел число {n}. Результат: ', *lst_rate)
    else:
        lst_rate.insert(0, n)
        print(f'Пользователь ввел число {n}. Результат: ', *lst_rate)
