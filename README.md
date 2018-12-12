# Polar-Graphing

This little program adds the capability of graphing negative radii through matplotlib's polar graphing implementation.

Usage:
```
python -i polarGraphing.py "xmin" "xmax" "r(x)"
```

To step through the graph, use the 'j' and 'k' keys, forward and backward respectively. Bigger steps are achieved through 'J' and 'K'. Also, pressing 'l' loops through the graph forwards and backwards until stopped. To exit the loop, send an interrupt command, Ctrl-C (SIGINT).

Example:
```
python -i polarGraphing.py 0 "2*pi" "1 + 2*cos(x)"
```

![alt text](plot.png?raw=true "Example plot")

Functions included by default are {cos, sin, tan, arccos, arcsin, arctan}. Any additional functions included in the numpy package may be accessed with prefix "np."
