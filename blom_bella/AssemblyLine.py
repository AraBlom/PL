from Component import Component
from Package import Package
from Track import Track
from Station import Station
from Package import Package
class AssemblyLine:
    def __init__(self):
        self.line= [Track(), Track(), Track(), Station(), Track(), Track()]

    def print_line(self):
        for component in self.line:
            component.print()

    def addPackage(self, pkg_type, capacity):
        pkg = Package(pkg_type, capacity)
        if not self.line[0].empty():
            self.line[0].update(pkg)


