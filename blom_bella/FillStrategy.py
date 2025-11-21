
"""
Fills package and drops or kicks it
Increments the dropped count.
:param station: the station to fill
:type station: Station
:return: None or pkg
:type pkg: Package
"""
def fill(station, pkg): #GRADING: UPDATE_FILL
    pkg_held = pkg.curr_units()
    weight = station.get_weight()
    station_fill = station.get_fill()
    if  pkg.curr_units() < weight:
        if pkg_held <= pkg.get_capacity()+station_fill:
            pkg.fill(station_fill)
    if pkg.curr_units() < weight and pkg.curr_units() < pkg.get_capacity():
        station.add_pkg(None)
        return pkg
    station.add_pkg(None)
    station.drop()
    return None


"""
Fills according to type
:param station: the station to fill
:type station: Station
:return: None or pkg
:type pkg: Package
"""
def type_fill(station, pkg): # GRADING: UPDATE_TYPE
    if pkg.get_id() == station.get_id():
        return fill(station, pkg)
    else:
        station.add_pkg( None)
        return pkg