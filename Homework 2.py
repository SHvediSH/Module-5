class House:                                                                #Объявляем класс.
    def __init__(self, numberOfFloors):                                     #Создаем инициализатор с указателем и одним параметром.
        self.numberOfFloors = numberOfFloors                                #Объявляем переменную которой будем присваивать значение указаного параметра.
        print(numberOfFloors)                                               #Вывод в консоль.

    def setNewNumberOfFloors(self, floors):                                 #Объявляем метод с указателем и параметром.
        self.floors = floors                                                #Присваиваем переменной значение параметра.
        self.numberOfFloors = floors                                        #Переобъявляем переменную из инициализатора (для изменения значения по тех. заданию).
        print(self.numberOfFloors)                                          #Вывод в консоль.

h1 = House(0)                                                               #Создаем переменную h1 присваивая ей инициализатор (начало класса), вводим параметр (по тех. заданию 0).
h1.setNewNumberOfFloors(2)                                                  #Вызов переменной с использованием метода setNewNumberOfFloors (так же передали один параметр).
h1.setNewNumberOfFloors(6)
h1.setNewNumberOfFloors(4)
h1.setNewNumberOfFloors(8)