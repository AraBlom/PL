from Component import Component
"""
Station: controls the station functionality and 
has a package if necessary.
Strategy pattern for packages and display
"""
class Station(Component):
    """
    Station initialization, called by assembly line
    :param units: the units to fill
    :type units: number
    :param fill_f: fill function
    :type fill_f: function or None
    :param max_weight: maximum weight of the package before getting kicked
    :type max_weight: int
    :param st_type: type of station
    :type st_type: int
    """
    def __init__(self, units=0, max_weight=1, st_type = 0, fill_f = None):
        self._package = None
        self._fill = units
        self._id = st_type
        self._weight = max_weight
        self.__fill_f = fill_f
        self._dropped = 0
        self.__display = None

    """
    Sets the display class, must be called before print will work
    :param display: the display class
    :type display: Display
    """
    def set_display (self, display):
        self.__display = display(self)

    """
    Calls the display method of the display class and prints it
    """
    def print(self):
        if self.__display is not None:
            print (self.__display.display(self._package, self._dropped))

    """
    Fills the package  (calls fill function) or updates package on station
    :param package: the package to fill
    :type package: Package
    :return: None or pkg
    :type plg: Package
    """
    def update(self, package =None):
        if not self._package:
            self._package = package
            return None
        elif self.__fill_f:
            return self.__fill_f(self, self._package)
        else:  #GRADING: NULL
            pkg = self._package
            self._package = None
            return pkg
    """
    adds package to station
    :param package: the package to add
    """
    def add_pkg(self, package):
        self._package = package
    """
    Drop a package, updates drop count
    """
    def drop(self):
        self._dropped += 1
    """
    get station id
    :return: station id
    """
    def get_id(self):
        return self._id
    """
    get station id
    :return: station id
    """
    def get_fill(self):
        return self._fill
    """
    get station weight
    :return int
    """
    def get_weight(self):
        return self._weight
