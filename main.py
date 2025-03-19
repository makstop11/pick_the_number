s = input('Введите начало и ĸонец диапазона загаданного числа: ')
s = s.split()

length = len(s)

count = 0

left = int(s[0])
right = int(s[1])
while left <= right:
    count += 1
    max_number_of_attempts = 7
    if count > max_number_of_attempts:
        break
    middle = (left + right) // 2
    print(middle)
    i = input()
    if i == 'угадал':
        print(f'Я угадал! Загаданное число: {middle}.Количиство попыток: {count}')
        break

    if i == 'больше':
        left = middle + 1
    elif i == 'меньше':
        right = middle - 1
    else:
        print('Ошибка. Введите значение заново')
        count -= 1

# 6.1: проверка значения: ответы: больше меньше угадал - корректные а остальные нет
# При некорректных ответах попытка не засчитывается
