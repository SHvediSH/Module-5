class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.buildingType = buildingType
        self.numberOfFloors = numberOfFloors

    def __eq__(self, other):
        return self.buildingType == other.buildingType
        return self.numberOfFloors == other.numberOfFloors

Building1 = Building(40, "ПятиэтажОчка")
Building2 = Building(40, "ПятиэтажОчка")
Building3 = Building(55, "ВысотОчка")
Building4 = Building(562, "СталИнка")
print(Building1 == Building2)
print(Building3 == Building4)