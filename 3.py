price = int(input('Введите стоимость: '))

count = 0

while price >=25:
    price = price - 25
    count += 1
while price >=10:
    price = price - 10
    count += 1
while price >=5:
    price = price - 5
    count += 1
while price >=1:
    price = price -  1
    count += 1
print (count)