import sys
import os
import cPickle
import numpy

from matplotlib import pyplot
from matplotlib.colors import LogNorm
from matplotlib import cm


def load_pickle(filename):
    f = open(filename,"rb")
    p = cPickle.load(f)
    f.close()
    return(p)

TO_DEG = 180.0 / numpy.pi



colormaps = [cm.PuBu,
             cm.BuGn,
             cm.BuPu,
             cm.PuBuGn]


plot_data   = []
native_data = []

for arg in sys.argv:

    if ("native" in arg) and (".cpickle" in arg):
        native_data = load_pickle(arg)
        print arg, "native"
    elif ".cpickle" in arg:
        plot_data.append(load_pickle(arg))
        print arg, "plot"

length = len(native_data)

bin_no = 36
deg_range = [-180.0, 180.0]

max_exponent = 4.0 # E.g. max is 10^4.0
lvls = numpy.logspace(0.0, max_exponent, 20)

plots_per_row = len(sys.argv) - 2

residue_ids = range(0, len(native_data))
#residue_ids = range(0, 5)

pyplot.figure(figsize=(plots_per_row * 5, len(residue_ids) * 4))

length = len(residue_ids)
for plot_i, i in enumerate(residue_ids):

    for plot_j, output_data in enumerate(plot_data):


        pyplot.subplot(length, plots_per_row, plot_i * plots_per_row + plot_j + 1)

        x_vals = numpy.array(output_data[i]["phi"]) * TO_DEG
        y_vals = numpy.array(output_data[i]["psi"]) * TO_DEG

        H, xedges, yedges = numpy.histogram2d(y_vals, x_vals,
                range=[deg_range,deg_range], bins=(bin_no, bin_no))

        max_val =  numpy.amax(H)
        print "largest bin:", max_val, " Log:", numpy.log10(max_val)

        extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]

        pyplot.title("Residue " + str(i + 1))

        pyplot.contourf(H+1, extent=extent, zorder = -1,
                        cmap = colormaps[plot_j], norm = LogNorm(),
                        levels = lvls)



        pyplot.colorbar(ticks=numpy.logspace(0.0, max_exponent, 5))
        pyplot.xticks([-180.0, -120.0, -60.0, 0.0, 60.0, 120.0, 180.0])
        pyplot.yticks([-180.0, -120.0, -60.0, 0.0, 60.0, 120.0, 180.0])
        pyplot.grid(True)
        pyplot.axvline(x=0.0, ymin=-180.0, ymax=180.0, color="k")
        pyplot.axhline(y=0.0, xmin=-180.0, xmax=180.0, color="k")
        pyplot.xlim(deg_range)
        pyplot.ylim(deg_range)

        pyplot.plot(numpy.array(native_data[i]["phi"])*TO_DEG,
                    numpy.array(native_data[i]["psi"])*TO_DEG, "ro")



png_filename = "contour.png"
pyplot.savefig(png_filename)
os.system("convert -trim %s %s" % (png_filename, png_filename))

