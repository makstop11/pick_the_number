s = input('Введите начало и ĸонец диапазона загаданного числа: ')
s = s.split()

length = len(s)

count = 0

left = int(s[0])
right = int(s[1])
while left <= right:
    count += 1
    if count > 7:
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
