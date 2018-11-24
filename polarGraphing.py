import numpy as np
from numpy import cos, sin, tan, arccos, arcsin, arctan, pi
import matplotlib.pyplot as plt
import sys

# python -i polarGraphing.py 0 "2*pi" "1 + 2*cos(x)"

if sys.argv[1] == "-1" and sys.argv[2] == "-1":
    xmin=0
    xmax=2*pi
else:
    xmin=eval(sys.argv[1])
    xmax=eval(sys.argv[2])

def func(x):
    return eval(sys.argv[3])

n=1000
x=np.linspace(xmin, xmax, n)
y=func(x)
theta=[]
r=[]

pos=0

def updateDot(pos):
    global n, x, y, theta, r
    dot1.set_xdata(x[pos])
    dot1.set_ydata(y[pos])
    dot2.set_xdata(theta[pos])
    dot2.set_ydata(r[pos])
    fig.canvas.draw()

def press(event):
    global n, pos, x, y, theta, r
    if event.key == 'left':
        pos -= (int)(.01*n)
        if (pos < 0):
            pos = 0
        updateDot(pos)
    if event.key == 'right':
        pos += (int)(.01*n)
        if (pos >= n):
            pos = n-1
        updateDot(pos)
    if event.key == 'down':
        pos -= (int)(.1*n)
        if (pos < 0):
            pos = 0
        updateDot(pos)
    if event.key == 'up':
        pos += (int)(.1*n)
        if (pos >= n):
            pos = n-1
        updateDot(pos)
    if event.key == 'k':
        dpos = (int)(.03*n)
        while (1==1):
            pos += dpos
            if (pos >= n or pos < 0):
                dpos *= -1
            else:
                updateDot(pos)

for i in x:
    r.append(abs(func(i)))
    if func(i) < 0:
        theta.append(i+np.pi)
    else:
        theta.append(i)

fig = plt.figure()
fig.canvas.mpl_connect('key_press_event', press)

ax1 = fig.add_subplot(211)
ax1.plot(x,y)
dot1, = ax1.plot(x[pos], y[pos], 'ro')

ax2 = fig.add_subplot(212, projection='polar')
ax2.plot(theta,r)
dot2, = ax2.plot(theta[pos], r[pos], 'ro')

fig.show()
fig.savefig('plot.png')
