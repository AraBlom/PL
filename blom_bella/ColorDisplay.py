from Display import Display
from ColorText import ColorText

class ColorDisplay(Display):

    def display(self, pkg, dropped = 0):
        ans = super().display(pkg)
        if pkg and pkg._holding  + self._fill >= self._weight:
            ans = ColorText.fg.red + ans + ColorText.reset#GRADING: DISPLAY_COLOR
        elif pkg:
            ans = ColorText.fg.blue + ans + ColorText.reset
        return ans
