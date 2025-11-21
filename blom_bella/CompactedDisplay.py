from Display import Display

class CompactedDisplay(Display):
    def display(self, pkg, dropped = 0):
        start_str = super().display(pkg)
        i = 0
        while i < 5 and i < dropped : #GRADING: DISPLAY_COMPACT
            start_str += "⌧"
            i += 1
        if i < dropped :
          start_str += "(+"+ str (dropped - i) + ")"

        return start_str
