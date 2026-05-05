start_pop = int(input('Введите стартовое число организма: '))
average_grow_percent = int(input('Введите среднесуточное увеличение (%): '))
num_days = int(input('Введите количество для для размножения: '))

daily_grow = 1 + average_grow_percent / 100

current_population = start_pop
for i in range(1,num_days + 1):
    print(i, current_population)
    current_population *= daily_grow

