s = input('Введите начало и ĸонец диапазона загаданного числа: ')
s = s.split()

if s[0] > s[1]:
    print('Некоректный ввод чисел')

length = len(s)

count = 0

left = 0
right = int(s[1]) - 1
while left < right:
    count += 1
    if count > 7:
        break
    middle = (left + right) // 2 + 1
    print(middle)
    i = input()
    if i == 'больше':
        left = middle + 1
    elif i == 'меньше':
        right = middle - 1
    else:
        print(f'Я угадал! Загаданное число: {middle}.Количиство попыток: {count}')

# что бы проверить на число надо применить isdigit

# В пункте 3 можно воспользоваться бинарным поиском
