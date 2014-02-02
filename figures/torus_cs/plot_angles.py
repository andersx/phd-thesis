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


to_deg = 180.0 / numpy.pi

native_data = load_pickle("temp1.cpickle")
torus_cs_data = load_pickle("temp2.cpickle")
torus_data = load_pickle("temp3.cpickle")

output_data = torus_data


length = len(output_data)

width = 12
bin_no = 36

deg_range = [-180.0, 180.0]


max_exponent = 4.0 # E.g. max is 10^4.0

lvls = numpy.logspace(0.0, max_exponent, 20)

pyplot.figure(figsize=(4 * width, length/width * 4))
for i in range(length):


    pyplot.subplot(length/width+1, width, i + 1)

    x_vals = numpy.array(output_data[i]["phi"])*to_deg
    y_vals = numpy.array(output_data[i]["psi"])*to_deg

    H, xedges, yedges = numpy.histogram2d(y_vals, x_vals,
            range=[deg_range,deg_range], bins=(bin_no, bin_no))

    max_val =  numpy.amax(H)

    print "largest bin:", max_val, " Log:", numpy.log10(max_val)
    #H = numpy.log10(H+1.0)

    extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]

    pyplot.title("Residue " + str(i + 1))

    pyplot.contourf(H+1, extent=extent, zorder = -1,
                    cmap = cm.PuBu, norm = LogNorm(),
                    levels = lvls)

    pyplot.plot(numpy.array(native_data[i]["phi"])*to_deg,
               numpy.array(native_data[i]["psi"])*to_deg, "ro")

    pyplot.colorbar(ticks=lvls)
    pyplot.xlim(deg_range)
    pyplot.ylim(deg_range)


png_filename = "contour.png"
pyplot.savefig(png_filename)
os.system("convert -trim %s %s" % (png_filename, png_filename))

# #output_data = load_pickle("")
# output_data = load_pickle("torus_cs_hn.cpickle")
#
# for i in range(length):
#     pylab.subplot(length/width+1, width, i + 1)
#
#     pylab.plot(output_data[i]["phi"], output_data[i]["psi"], "k+")
#     pylab.xlim([-numpy.pi, numpy.pi])
#     pylab.ylim([-numpy.pi, numpy.pi])

# output_data = load_pickle("native.cpickle")
# 
# for i in range(length):
#     pylab.subplot(length/width+1, width, i + 1)
# 
#     pylab.plot(output_data[i]["phi"], output_data[i]["psi"], "ro")
#     pylab.xlim([-numpy.pi, numpy.pi])
#     pylab.ylim([-numpy.pi, numpy.pi])
# 
# pylab.savefig("torus_cs_density.pdf")



