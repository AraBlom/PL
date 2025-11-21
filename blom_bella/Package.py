class Package:
    def __init__(self, p_type, capacity):
        self._id = p_type
        self._capacity = capacity
        self._holding = 0

    def fill(self, units):
        if self._holding + units > self._capacity:
            self._holding = self._capacity
        else:
            self._holding += units

    def isFull(self):
        return self._holding == self._capacity

    def toString(self):
        cap = str(self._id) + ' ' + str(self._holding) +'/' +str(self._capacity)
        return("⍽:" + cap)