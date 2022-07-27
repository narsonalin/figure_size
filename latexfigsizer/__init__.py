import numpy as np
import matplotlib.pyplot as plt
from cycler import *
from matplotlib.ticker import FuncFormatter

__metaclass__ = type

width = 455.24411

def set_size( width, fraction=1, subplots=(1, 1), golden_ratio=0.6180339887498949 ):
    """
    Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float
            Document textwidth or columnwidth in pts
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
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


# scientific notation on each ticks
def sci_format( x ):
    """
    Format float to scientific notation in Latex syntax.
    Parameters
    ----------
    x: float
        Float to be formated

    Returns
    -------
    string
    """
    if x == 0:
        return r'$0$'
    return r'$%.5g\times10^{%.0f}$' % (np.sign(x)*10**(-np.floor(np.log10(abs(x)))+np.log10(abs(x))), np.floor(np.log10(abs(x))))
    #The first argument of the format gives the first significant digits of the number with the sign preserved and brought to a range between [1-10), The next argument gives the  numbers integer exponent of 10
    #Both the first and second arguments are formatted to display only 2 decimal places due to the lack of space.


major_formatter = FuncFormatter(sci_format)

