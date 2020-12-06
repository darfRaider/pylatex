from matplotlib import pyplot as plt
import numpy as np

class XYPlot:
  _x = None
  _y = None
  _axes = None
  #TODO : Add
  def __init__(self, x: [], y: [], axes = None):
    # Basic input check
    if len(x) != len(y):
      raise ValueError("Vectors must have same length.")
    if len(x) == 0 or len(y) == 0:
      raise ValueError("Vectors must contain some data.")
    # Check types
    xTypes = [type(d) in [int, float, np.float64] for d in x]
    yTypes = [type(y) in [int, float, np.float64] for y in y]

    if any(flag == False for flag in xTypes):
      raise TypeError("Elements must be of type int or float.")
    if any(flag == False for flag in yTypes):
      raise TypeError("Elements must be of type int or float.")
    self._x = x
    self._y = y
    self._axes = axes

  def plot(self):
    self._axes.plot(self._x, self._y)
    self._axes.set_title("XYPlot")

  def setXvalues(self, x: []):
    self._x = x


# xy = XYGraph([1,2,3],[3,4,2])