class Package:
    def __init__(self, type, capacity):
        self.__id = type
        self.__capacity = capacity
        self.__holding = 0

    def fill(self, units):
        if self.__holding + units > self.__capacity:
            self.__holding = self.__capacity
        else:
            self.__holding += units

    def isFull(self):
        return self.__holding == self.__capacity

    def toString(self):
        cap = str(self.__id) + ' ' + str(self.__holding) +'/' +str(self.__capacity)
        return("⍽:" + cap)