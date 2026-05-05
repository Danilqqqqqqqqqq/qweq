num = int(input('Введите натуральное число: '))
total = 0
sign = 1
for i in range(1, num + 1):
    total += i * sign
    sign *= -1
print(total)




