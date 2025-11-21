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
        curr_pkg = self._package
        self._package = package
        return curr_pkg

