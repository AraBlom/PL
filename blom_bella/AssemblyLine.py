from Component import Component
from Package import Package
from Track import Track
from Station import Station
from Package import Package
from FillStrategy import fill, type_fill
class AssemblyLine:
    def __init__(self):
        self.line= [Track(), Track(), Track(), Station(), Track(), Track()]

    def print_line(self):
        for component in self.line:
            component.print()

    def add_package(self, pkg_type, capacity):
        pkg = Package(pkg_type, capacity)
        if self.line[0].empty():
            self.line[0].update(pkg)

    def tick(self):
        pkg = None
        for index, component in enumerate (reversed(self.line)):
            i = len(self.line)- index
            pkg = component.update(None)
            if pkg and i < len(self.line) and self.line[i].empty():
                self.line[i].update(pkg)

    def tick_x(self, x):
        for i in range(x -1):
            self.tick()
            self.print_line()
        self.tick()

    def clear_track(self):
        self.line = []

    def add_track(self, units):
        for i in range(units):
            self.line.append(Track())

    def add_station(self, s_type=0, fill_units= 0, pkg_weight =1, fill_type = 1):
        if fill_type == 1:
            sat = Station(fill_units, pkg_weight, s_type)
        elif fill_type == 2:
            sat = Station(fill_units, pkg_weight, s_type,fill )
        else: # fill_type == 3:
            sat = Station(fill_units, pkg_weight, s_type, type_fill)
        self.line.append(sat)