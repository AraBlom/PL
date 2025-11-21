class Display:
    def __init__(self, fill, weight, id):
        self._fill = fill
        self._weight = weight
        self._id = id

    def display(self, pkg, dropped = 0):
        img = "⼐"
        if pkg:
            img = "|"+  self._getPkgStr(pkg) + "|"
        T = self._getT()
        w = str(self._fill).rjust(3) + "/" + str(self._weight).ljust(3)
        det = " [" + T.center(5) + w.center(3) + "]"
        return img.ljust(12) + det

    def _getT(self):
        return "T" + str(self._id)

    def _getPkgStr(self, pkg):
        img = pkg.toString()
        return img