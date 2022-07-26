# LaTeXfigsizer
Make some figures in LaTeX more easily ?

## Configuration

You first need to know the the number of points in a textwidth of your latex
document. To do so, add in your TeX document:

```latex
% return the textwidth in pts:
\showthe\textwidth
```

## Usage

Define a sizer object corresponding to your defaults need, and call while
creating your figure. You can modify the value on the fly. See second example.

```python
import matplotlib.pyplot as plt
from laTeXfigsizer import *

sizer = Sizer(
    width=455.24411,
    fraction=1,
    subplots=(1, 1),
    golden_ratio=(1 + math.sqrt(5) / 2),
)

fig, ax = plt.subplots(1, 2, figsize=sizer())

# or

fig, ax = plt.subplots(1, 2, figsize=sizer(523.5307, subplots=(1, 2)))
```

The ratio between figure height and width will automatically be set to the Golden ratio.
If you want to specify a different ratio, use the `golden_ratio` keyword:

```python
fig, ax = plt.subplots(1, 2, figsize=sizer(subplots=(1, 2), golden_ratio=0.8))
```

To ensure that the font size in your .tex file matches the of of your figure,
use the following configuration commands using `rcParams`:

```python
params = {
    'text.usetex': True,
    # Use 12pt font in plots, to match 12pt font in document (or use something
    # else)
    "axes.labelsize": 12,
    "font.size": 12,
    # Make the legend/label fonts a little smaller
    "legend.fontsize": 11,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11
}

plt.rcParams.update(params)
```
