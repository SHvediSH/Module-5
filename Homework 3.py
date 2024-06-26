class Building:                                                    #Объявление класса.
    def __init__(self, numberOfFloors, buildingType):              #Объявление инициализатора с 2 параметрами.
        self.buildingType = buildingType                           #Создание атрибута(переменной).
        self.numberOfFloors = numberOfFloors                       #Аналогично.

    def __eq__(self, other):                                       #Объявление метода перегрузки(сравнение).
        return self.buildingType == other.buildingType             #Первый объект сравнения(тип строения)
        return self.numberOfFloors == other.numberOfFloors         #Второй объект сравнения

Building1 = Building(40, "ПятиэтажОчка")   #Создали переменнные, задали параметры. -
Building2 = Building(40, "ПятиэтажОчка")
Building3 = Building(55, "ВысотОчка")
Building4 = Building(562, "СталИнка")      #-
print(Building1 == Building2)                                      #Вывод результата первого сравнения.
print(Building3 == Building4)                                      #Второй вывод.

                    #Такие перегрузки можно применять для проверки выполнения условий или сравнения, что в дальнейшем
                    #можно использовать для написания последующих действий(в случае выполнения или не выполнения условий)