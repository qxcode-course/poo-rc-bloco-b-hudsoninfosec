class Battery:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__level = capacity

    def usingBattery(self):
        return f'{self.__level}/{self.__capacity}'