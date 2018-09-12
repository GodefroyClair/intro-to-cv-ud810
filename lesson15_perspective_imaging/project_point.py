import unittest

import numpy as np

# Project a point from 3D to 2D using a matrix operation


# Given: Point p in 3-space [x y z], and focal length f
# Return: Location of projected point on 2D image plane [u v]
def projectPoint(p, f):
    # TODO: Define and apply projection matrix
    A = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1/f, 0]])
    pHomog = np.append(p, 1)  # .reshape(-1, 1)
    print("p homogeneous: " + str(pHomog))
    pProj = A.dot(pHomog)
    print("p proj: " + str(pProj))
    pImg = f / p[2] * pProj
    return pImg[0:2]


# Test: Given point and focal length (units: mm)
p = np.array([200, 100, 50])
f = 50
# print(projectPoint(p, f))

try:
    np.testing.assert_array_equal(projectPoint(p, f), p[0:2])
except AssertionError as err:
    res = False
    print(err)
try:
    np.testing.assert_array_equal(projectPoint(p, 100), np.array([400, 200]))
except AssertionError as err:
    res = False
    print(err)
