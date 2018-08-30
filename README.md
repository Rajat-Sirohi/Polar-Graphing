# Polar-Graphing

This little program adds the capability of graphing negative radii through matplotlib's polar graphing implementation.

Usage:
```
python -i polarGraphing.py "xmin" "xmax" "r(x)"
```

Example:
```
python -i polarGraphing.py 0 "2*pi" "1 + 2*cos(x)"
```

![alt text](plot.png?raw=true "Example plot")

Functions included by default are {cos, sin, tan, arccos, arcsin, arctan}. Any additional functions included in the numpy package may be accessed with prefix "np."
