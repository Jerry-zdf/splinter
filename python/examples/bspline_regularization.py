# This file is part of the SPLINTER library.
# Copyright (C) 2012 Bjarne Grimstad (bjarne.grimstad@gmail.com).
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Add the SPLINTER directory to the search path, so we can include it
import numpy as np
import matplotlib.pyplot as plt
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import splinterpy

# Only for dev purposes
import os.path
if os.path.isdir("/home/bjarne/"):
    splinterpy.load("/home/bjarne/Code/C++/splinter/build/release/libsplinter-4-0.so")
elif os.path.isdir("/home/anders/"):
    splinterpy.load("/home/anders/SPLINTER/build/debug/libsplinter-4-0.so")


# Example with one variable
def f1(x):
    return -1. + 2*x + 0.1*(x**2) + 10*np.random.random()

n = 10
x = np.linspace(0, 10, n)
y = [f1(xi) for xi in x]

# Cubic B-spline that interpolates the data (note that NONE is the default smoothing setting)
b1 = splinterpy.BSplineBuilder(1, 1).fit(x, y, smoothing=splinterpy.BSplineBuilder.Smoothing.NONE)

# Cubic B-spline with regularization
b2 = splinterpy.BSplineBuilder(1, 1).fit(x, y, smoothing=splinterpy.BSplineBuilder.Smoothing.IDENTITY, alpha=0.1)

# Cubic P-spline
b3 = splinterpy.BSplineBuilder(1, 1).fit(x, y, smoothing=splinterpy.BSplineBuilder.Smoothing.PSPLINE, alpha=0.1)

nd = 1000
xd = np.linspace(0, 10, nd)
yd1 = [b1.eval(xi) for xi in xd]
yd2 = [b2.eval(xi) for xi in xd]
yd3 = [b3.eval(xi) for xi in xd]

# Plot results
plt.plot(x, y, '*', label='Data points')
plt.plot(xd, yd1, label='Interpolating B-spline')
plt.plot(xd, yd2, '--', label='Regularized B-spline')
plt.plot(xd, yd3, '-.', label='P-spline')
plt.legend(loc='upper left')
plt.show()
