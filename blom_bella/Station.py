from Component import Component
class Station(Component):
    def __init__(self, units=0, max_weight=1, st_type = 0, fill_f = None):
        self._package = None
        self._fill = units
        self._id = st_type
        self._weight = max_weight
        self.__fill_f = fill_f
        self._dropped = 0
        self.__display = None

    def set_display (self, display):
        self.__display = display(self._fill, self._weight, self._id)

    def print(self):
       print (self.__display.display(self._package, self._dropped))

    def update(self, package =None):
        if not self._package:
            self._package = package
            return None
        elif self.__fill_f:
            return self.__fill_f(self)
        else:
            pkg = self._package
            self._package = None
            return pkg
