from Display import Display
from ColorText import ColorText

class ColorDisplay(Display):

    """
    Override of display method to display the station in color
    :param pkg: station package
    :type pkg: Package
    :param dropped: not used
    :return string, the string to display
    """
    def display(self, pkg, dropped = 0):
        ans = super().display(pkg)
        if pkg and pkg.curr_units()+ self._fill >= self._weight:
            ans = ColorText.fg.red + ans + ColorText.reset #GRADING: DISPLAY_COLOR
        elif pkg:
            ans = ColorText.fg.blue + ans + ColorText.reset
        return ans
