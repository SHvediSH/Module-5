class House:                                                                    #Создание класса.
    def __init__(self, name, number_of_floors):                                 #Инициализация параметров с ссылкой на них.
        self.name = name                                                        #Объявление переменной значение которой будет ровно первому параметру.
        self.number_of_floors = number_of_floors                                #Аналогично только уже с 2 параметром.

    def go_to(self, current_floor):                                             #Объявление функции с ссылкой и 1 параметром.
        self.current_floor = current_floor                                      #Объявление третьей аналогичной переменной.
        if current_floor < 1 or current_floor > self.number_of_floors:          #Первое условие.
            print("Дружище, куда едешь?")                                        #Результат выполнения условия.
        else:                                                                   #"Что делать иначе"
            current_floor >= 1 and current_floor <= self.number_of_floors       #Второе условие.
            for lift in range(1, current_floor + 1):                            #Начало цикла.
                print(lift)                                                     #Вывод результата цикла.
                your_floor = + current_floor                                    #Объявляем переменнную и прибавляем к ней наше введеное значение.
            print("Вы прибыли на", your_floor, "этаж")                          #Выводим в консоль последнее значение цикла.


h1 = House("ЖК Эльбрус", 30)                                #Объявляем переменную и присваиваем ей класс и 2 параметра из 1 функции.
h2 = House("ЖК Спиральные небеса", 1000)                    #Аналогично.
h1.go_to(30)                                                                    #Вызываем нашу переменную и присоеденяем к ней метод из 2 функции с 1 параметром.
h2.go_to(1001)                                                                  #Аналогично.

#Матрёшка стала побольше чем раньше...