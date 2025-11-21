"""
Packages along the track
"""
class Package:
    """
    Initialises the package
    :param p_type: the type of package
    :type p_type: int
    :param capacity: the capacity of the package
    :type capacity: int
    """
    def __init__(self, p_type, capacity):
        self._id = p_type
        self._capacity = capacity
        self._holding = 0

    """
    Fills the package
    :param p_type: the type of package
    :type p_type: int
    """
    def fill(self, units):
        if self._holding + units > self._capacity:
            self._holding = self._capacity
        else:
            self._holding += units

    """
    checks if the package has been filled
    :return bool: True if the package has been filled
    """
    def is_full(self):
        return self._holding == self._capacity
    """
    :return int current units held
    """
    def curr_units(self):
        return self._holding
    """
    :return int capacity
    """
    def get_capacity(self):
        return self._capacity
    """
    :return int id
    """
    def get_id(self):
        return self._id
    """
    String of the package's details
    """
    def toString(self):
        cap = str(self._id) + ' ' + str(self._holding) +'/' +str(self._capacity)
        return("⍽:" + cap)