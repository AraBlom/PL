from Component import Component
"""
Track components
"""
class Track(Component):
    """
    initialize
    """
    def __init__(self):
        self._package = None

    """
    Print track defaults
    """
    def print(self):
        if self._package:
            print(self._package.toString())
        else:
            print("||")

    """
    Adds a package to track if necessary
    :param package: package to add
    """
    def update(self, package =None):
        curr_pkg = self._package
        self._package = package
        return curr_pkg

