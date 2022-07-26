import math
from typing import Tuple


class Sizer:
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
        golden_ratio: float = (1 + math.sqrt(5) / 2),
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

        width = width or self.width
        fraction = fraction or self.fraction
        subplots = subplots or self.subplots
        golden_ratio = golden_ratio or self.golden_ratio
        print(width)

        # Width of figure (in pts)
        fig_width_pt = width * fraction

        # Convert from pt to inches
        inches_per_pt = 1 / 72.27

        # Figure width in inches
        fig_width_in = fig_width_pt * inches_per_pt

        # Figure height in inches
        fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

        fig_dim = (fig_width_in, fig_height_in)

        return fig_dim


def latexFormatter(x):
    """
    Format float to scientific notation in Latex syntax.

    The first argument of the format gives the first significant digits of the
    number with the sign preserved and brought to a range between [1-10), The
    next argument gives the  numbers integer exponent of 10 Both the first and
    second arguments are formatted to display only 2 decimal places due to the
    lack of space.

    To call on each labels, use major_formatter = FuncFormatter(latexFormatter)

    Args:
        x (float): Float to be formated

    Returns:
        (string): Properly formatted string
    """
    if x == 0:
        return r"$0$"
    return r"$%.5g\times10^{%.0f}$" % (
        math.copysign(1, x)
        * 10 ** (-math.floor(math.log10(abs(x))) + math.log10(abs(x))),
        math.floor(math.log10(abs(x))),
    )
