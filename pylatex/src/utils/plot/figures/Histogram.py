import numpy as np

class Histogram:
  _values = None
  _axes = None

  def __init__(self, values: [], names: [], axes):
    self._values = values
    self._names = names
    self._axes = axes
    self._h = None

  def plot(self):
    self._h = self._axes.hist(self._values,bins=np.arange(len(self._names)+1)-0.5, alpha=0.5, histtype='bar', ec='black')
    self._axes.set_title("Histogram")
    self.xTicks(self._names)
    # ax.set_xticklabels(self._data,rotation=45, rotation_mode="anchor", ha="right")
  
  def xTicks(self, names: []):
    self._axes.set_xticks(np.arange(len(names)))
    self._axes.set_xticklabels(names,rotation=45, rotation_mode="anchor", ha="right")
    