
import pylatex.src.utils.plot.figures.XYPlot as XYPlot
import pylatex.src.utils.plot.figures.Histogram as Histogram
import pylatex.src.utils.plot.figures.PieChart as PieChart
import pylatex.src.utils.plot.Plot as Plot

import matplotlib
matplotlib.use('Agg') # added this for windows
from matplotlib import pyplot as plt

import numpy as np
from subprocess import call
import os
### testimports
from random import randint

OUTPUT_DIRECTORY = "out"

# TODO: Remove following and add to Plot class
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})
## for Palatino and other serif fonts use:
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
})


x = np.arange(0,10,0.1)
y = x + 1
fig = plt.figure()
ax = fig.add_subplot(1,3,1)
XYPlot.XYPlot(x,y, ax).plot()

ax2 = fig.add_subplot(1,3,2)
data = [randint(0,10) for x in x]
hist, bins = np.histogram(data)
names = [str(x) for x in bins]
test = [str(int(x)) for x in bins]
h = Histogram.Histogram(data, test, ax2)

h.xTicks(test)

ax3 = fig.add_subplot(1,3,3)
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [0.25, 0.25, 0.1, 0.4]
PieChart.PieChart(labels, fracs, ax3).plot()


plt.savefig("%s/myPlot.svg" % OUTPUT_DIRECTORY)

if not os.path.exists(OUTPUT_DIRECTORY):
    os.mkdir(OUTPUT_DIRECTORY)
    
os.system("inkscape -D --export-pdf=%s/out.pdf --export-latex %s/myPlot.svg" % (OUTPUT_DIRECTORY, OUTPUT_DIRECTORY))
os.system("pdflatex ./pylatex/latex/report.tex -output-directory %s" % OUTPUT_DIRECTORY)
# os.system("pdflatex ./pylatex/latex/report.tex")
# TODO: check when has to rebuild references (build twice)
os.system("pdflatex ./pylatex/latex/report.tex -output-directory %s" % OUTPUT_DIRECTORY)
