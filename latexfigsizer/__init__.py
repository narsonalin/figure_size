"""Define class Sizer and function latexFormatter"""

import math
from typing import Tuple


class LatexFigSizer:
    """
    This is a class to set figures dimensions to avoid scaling in LaTeX.

    On call, return the tuple fixing the dimensions of the figure in inches.

    Attributes:
        width (float): Document textwidth or columnwidth in pts
        fraction (float): Fraction of the defines with to occupy
        subplots (Tuple[float, float]): Tuple representing the grid of the created figures
        golden_ratio (float): Number representing the ratio between given width and computed height
    """

    def __init__(
        self,
        width: float = 455.24411,
        fraction: float = 1,
        subplots: Tuple[float, float] = (1, 1),
        golden_ratio: float = (math.sqrt(5) - 1) / 2,
    ) -> None:
        """
        Args:
            width (float): Document textwidth or columnwidth in pts
            fraction (float): Fraction of the defines with to occupy
            subplots (Tuple[float, float]): Tuple representing the grid of the created figures
            golden_ratio (float): Number representing the ratio between given width and computed height
        """
        self.width = width
        self.fraction = fraction
        self.subplots = subplots
        self.golden_ratio = golden_ratio

    def __call__(
        self,
        width: float = None,
        fraction: float = None,
        subplots: Tuple[float, float] = None,
        golden_ratio: float = None,
    ) -> Tuple[float, float]:
        """
        Args:
            width (float): Document textwidth or columnwidth in pts
            fraction (float): Fraction of the defines with to occupy
            subplots (Tuple[float, float]): Tuple representing the grid of the created figures
            golden_ratio (float): Number representing the ratio between given width and computed height
        """

        if width is None:
            width = self.width
        if fraction is None:
            fraction = self.fraction
        if subplots is None:
            subplots = self.subplots
        if golden_ratio is None:
            golden_ratio = self.golden_ratio

        # Width of figure (in pts)
        fig_width_pt = width * fraction

        # Convert from pt to inches
        inches_per_pt = 1 / 72.27

        # Figure width in inches
        fig_width_in = fig_width_pt * inches_per_pt

        # Figure height in inches
        fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

        return (fig_width_in, fig_height_in)


def latex_sciformatter(number: float) -> str:
    """
    Format float to scientific notation in Latex syntax.

    The first argument of the format gives the first significant digits of the
    number with the sign preserved and brought to a range between [1-10), The
    next argument gives the  numbers integer exponent of 10 Both the first and
    second arguments are formatted to display only 2 decimal places due to the
    lack of space.

    To call on each labels, use major_formatter = FuncFormatter(latex_sciformatter)

    Args:
        number (float): Float to be formated in a scientific format

    Returns:
        (string): Properly formatted string in a scientific format
    """
    stringified = r"$0$"
    if number != 0:
        significand = math.copysign(1, number) * 10 ** (
            -math.floor(math.log10(abs(number))) + math.log10(abs(number))
        )
        exponent = math.floor(math.log10(abs(number)))
        stringified = rf"${significand:.{5}}\times10^{{{exponent}}}$"

    return stringified
