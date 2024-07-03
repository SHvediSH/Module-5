class Building:                     #Создали класс.
    total = 0                       #Объявили атрибут класса.

    def __init__(self):             #Первый метод класса. Прибавляет значение к атрибуту total нашего класса.
        Building.total += 1

    def __str__(self):                              #Второй метод возвращает классовый атрибут с текстом.
        return f'Building number {Building.total}'


for Building1 in range(40):                         #Создание цикла который в нашем случае 40 раз пройдёт по методам нашего класса.
    new_Building = Building()


print(new_Building.__str__())                       #Вывод итогового значения в консоль.


