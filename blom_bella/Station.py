from Component import Component
class Station(Component):
    def __init__(self, units=0, max_weight=1, st_type = 0, fill_f = None):
        self._package = None
        self.__fill = units
        self.__id = st_type
        self.__weight = max_weight
        self.__fill_f = fill_f

    def print(self):
        img = "⼐"
        if self._package:
            img = "|"+self._package.toString() +"|"
        T = "T" + str(self.__id)
        w = str(self.__fill).rjust(3) + "/" + str(self.__weight).ljust(3)
        det = " [" + T.center(5) + w.center(3) + "]"
        print(img.ljust(12) + det)

    def update(self, package =None):
        if not self._package:
            self._package = package
        elif self.__fill:
            return self.__fill_f(self)
        else:
            pkg = self._package
            self._package = None
            return pkg
