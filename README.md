# README #

### Configuration ###

You first need to know the the number of points in a textwidth of your latex document.
To do so, add 

    % return the textwidth in pts:
    \showthe\textwidth

to you main .tex file. It will stop and give you a number of points. Copy that in the width global variable of `figure_size/__init__.py` or give it to `set_size` every time you call it.
You can the comment out above line.



### Usage ###

    import matplotlib.pyplot as plt
    from figure_size import *

    fig, ((ax1, ax2)) = plt.subplots(1,2, figsize=set_size(width, subplots=(1,2)) )
    #or 
    fig, ((ax1, ax2)) = plt.subplots(1,2, figsize=set_size(523.5307, subplots=(1,2)) )

The ratio between figure height and width will automatically be set to the Golden ratio.
If you want to specify a different ratio, use the `golden_ratio` keyword:

    fig, ((ax1, ax2)) = plt.subplots(1,2, figsize=set_size(width, subplots=(1,2), golden_ratio=0.8) )

To ensure that the font size in your .tex file matches the oe of your figure, use the following configuration commands:

    params = {'text.usetex' : True,
          # Use 12pt font in plots, to match 12pt font in document (or use something else)
          "axes.labelsize": 12,
          "font.size"     : 12,
          # Make the legend/label fonts a little smaller
          "legend.fontsize": 11,
          "xtick.labelsize": 11,
          "ytick.labelsize": 11
          }
    plt.rcParams.update(params)