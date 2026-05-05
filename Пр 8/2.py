flag = False
for _ in range(10):
    num = int(input('Введите целое число: '))
    if num % 2 != 0:
        flag = True
        break
if flag:
    print('NO')
else:
    print('YES')
