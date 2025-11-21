class Display:
    """
    Initialize method with station details
    :param station: station
    """
    def __init__(self, station):
        self._fill = station.get_fill()
        self._weight = station.get_weight()
        self._id = station.get_id()

    """
    Display method basic
    :param pkg: station package
    :type pkg: Package
    :param dropped: not used
    :return string, the string to display
    """
    def display(self, pkg, dropped = 0): #GRADING: NOT_NULL
        img = "⼐"
        if pkg:
            img = "|" + pkg.toString() + "|"
        T = "T" + str(self._id)
        w = str(self._fill).rjust(3) + "/" + str(self._weight).ljust(3)
        det = " [" + T.center(5) + w.center(3) + "]"
        return img.ljust(12) + det

