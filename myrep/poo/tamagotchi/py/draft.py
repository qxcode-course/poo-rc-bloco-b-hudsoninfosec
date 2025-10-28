class Tamagotchi:
    def __init__(self, energyMax: int, cleanMax: int):
        self.__energyMax = energyMax
        self.__cleanMax = cleanMax
        self.__energy = energyMax
        self.__clean = cleanMax
        self.__age = 0
        self.__alive = True

    def set_energy(self, value: int):
        if value <= 0:
            self.__energy = 0
            self.__alive = False
            return 'fail: pet morreu de fraqueza'
        elif value > self.__energyMax:
            self.__energy = self.__energyMax
        else:
            self.__energy = value
        return None
