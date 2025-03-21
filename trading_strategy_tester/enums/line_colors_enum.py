from enum import Enum

class LineColor(Enum):
    """
    Enum class to represent different colors used for lines in graphs. Each color is
    defined as an RGBA string to control the opacity and shade.
    """

    PURPLE = 'rgba(117, 7, 117, 1)'
    YELLOW = 'rgba(160, 160, 0, 1)'
    TRANSPARENT = 'rgba(255, 255, 255, 0)'
    ORANGE = 'rgba(255, 183, 87, 1)'
    LIGHT_BLUE = 'rgba(153, 204, 255, 1)'
    PINK = 'rgba(255, 102, 178, 1)'
    LIGHT_GREEN = 'rgba(128, 255, 0, 1)'
    RED = 'rgba(241,54,69,255)'
    GREEN = 'rgba(39,153,129,255)'