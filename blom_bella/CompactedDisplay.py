from Display import Display
"""
Display class that prints station dropped packages
"""
class CompactedDisplay(Display):
    """
    Display method, colors string
    :param pkg: station package
    :type pkg: Package
    :param dropped: not used
    :return string, the string to display
    """
    def display(self, pkg, dropped = 0):
        start_str = super().display(pkg)
        i = 0
        while i < 5 and i < dropped : #GRADING: DISPLAY_COMPACT
            start_str += "⌧"
            i += 1
        if i < dropped :
          start_str += "(+"+ str (dropped - i) + ")"

        return start_str
