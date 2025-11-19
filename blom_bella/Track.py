from Component import Component
class Track(Component):
    def __init__(self):
        self._package = None

    def print(self):
        if self._package:
            print(self._package.toString())
        else:
            print("||")
    def update(self, package =None):
        curr_pkg = None
        if self._package:
            curr_pkg = self._package
        if package:
            self._package = package

