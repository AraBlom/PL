from Component import Component
from Package import Package
from Track import Track
from Station import Station
from Package import Package
from FillStrategy import fill, type_fill
from Display import Display
from CompactedDisplay import CompactedDisplay
from ColorDisplay import ColorDisplay

"""
Handles the line's components.
Approved change from the OOP diagram
"""
class AssemblyLine:
    """
    Create default track
    """
    def __init__(self):
        self.line= [Track(), Track(), Track(), Station(), Track(), Track()]
        self.__display = 1
    """
    Get display class from int display method set by program
    :return Display
    """
    def __get_display (self):
        if self.__display == 1:
            return Display
        elif self.__display == 2:
            return ColorDisplay
        else:
            return CompactedDisplay

    """
    Sets the display method
    """
    def set_display(self, display):
        self.__display = display

    """
    Prints the assembly line to the console
    """
    def print_line(self):
        display = self.__get_display()
        for component in self.line:
            if component.set_display:
                component.set_display(display)
        for component in self.line:
            component.print()

    """
    Add package to start of line
    :param pkg_type type of package
    :param capacity max weight of package
    """
    def add_package(self, pkg_type, capacity):
        pkg = Package(pkg_type, capacity)
        if self.line[0].empty():
            self.line[0].update(pkg)

    """
    Updates line by 1 unit of time
    """
    def tick(self):
        pkg = None
        for index, component in enumerate (reversed(self.line)):
            i = len(self.line)- index
            pkg = component.update(None)
            if pkg and i < len(self.line) and self.line[i].empty():
                self.line[i].update(pkg)

    """
    Updates line by x units of time
    """
    def tick_x(self, x):
        for i in range(x -1):
            self.tick()
            self.print_line()
        self.tick()

    """
    Clear the track
    """
    def clear_track(self):
        self.line = []

    """
    Add track segment to end of line
    :param units: units of track to add
    """
    def add_track(self, units):
        for i in range(units):
            self.line.append(Track())

    """
    Adds station to end of line
    :param s_type: type of station to add
    :param fill_units: fill units of station
    :param pkg_weight: weight of max pkg at station
    :param fill_type: fill type of station
    """
    def add_station(self, s_type=0, fill_units= 0, pkg_weight =1, fill_type = 1):
        if fill_type == 1:
            sat = Station(fill_units, pkg_weight, s_type)
        elif fill_type == 2:
            sat = Station(fill_units, pkg_weight, s_type,fill )
        else: # fill_type == 3:
            sat = Station(fill_units, pkg_weight, s_type, type_fill)
        self.line.append(sat)