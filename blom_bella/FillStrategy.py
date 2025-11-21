

def fill(station): #GRADING: UPDATE_FILL
    if station._package._holding < station._weight:
        if station._package._holding <= station._package._capacity+station._fill:
            station._package._holding += station._fill
    if station._package._holding < station._weight and station._package._holding < station._package._capacity:
        pkg = station._package
        station._package = None
        return(pkg)
    station._package = None
    station._dropped +=1
    return None



def type_fill(station): # GRADING: UPDATE_TYPE
    if station._package._id == station._id:
        return(fill(station))
    else:
        pkg = station._package
        station._package = None
        return(pkg)