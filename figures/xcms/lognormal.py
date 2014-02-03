import numpy
import pylab
import os

def lognormal(x, m, s):
    return 1.0/(x * numpy.sqrt(2.0 * numpy.pi * s**2.0)) * \
           numpy.exp( - (numpy.log(x) - m )**2.0 / (2 * s**2.0 ))

x = numpy.arange(0.01, 45.0, 0.01)

pylab.figure(figsize=(7,5))


sigma = 0.4
median = 14.0
mu = numpy.log(median)

dss = lognormal(x, mu, sigma)

sigma = 0.4
median = 6.4 / 11.0 * 14.0
mu = numpy.log(median)

dst = lognormal(x, mu, sigma)

sigma = 0.25
median = 4.7 / 11.0 * 14.0
mu = numpy.log(median)

edc = lognormal(x, mu, sigma)
#dss = dss /max(dss)
#dst = dst /max(dst)



data = numpy.array([[31 , 27 , 6.1 ,0.15],
                    [31 , 34 , 6.2 ,0.14],
                    [33 , 34 , 3.8 ,0.2 ],
                    [36 , 34 , 6.6 ,0.12],
                    [90 , 88 , 6.2 ,0.14],
                    [125, 107, 5.3 ,0.19],
                    [6  , 40 , 4.5 ,0.21],
                    [20 , 16 , 5.9 ,0.16],
                    [20 , 26 , 7.4 ,0.09],
                    [33 , 16 , 7   ,0.1 ],
                    [46 , 44 , 6.2 ,0.14],
                    [47 , 44 , 5.1 ,0.2 ],
                    [47 , 62 , 7.3 ,0.09],
                    [49 , 40 , 8.2 ,0.06],
                    [49 , 44 , 8.3 ,0.06],
                    [49 , 62 , 4.4 ,0.21],
                    [78 , 70 , 6.1 ,0.15],
                    [78 , 72 , 4.5 ,0.21],
                    [78 , 77 , 3.8 ,0.2 ],
                    [80 , 68 , 6.2 ,0.14],
                    [80 , 70 , 4.2 ,0.21],
                    [84 , 67 , 8.3 ,0.06],
                    [84 , 86 , 6   ,0.15],
                    [90 , 86 , 5   ,0.2 ],
                    [90 , 103, 4.6 ,0.21],
                    [121, 13 , 4.9 ,0.2 ]])

dist = data[:,2]


size = 6.5
ratio = 0.8
fig = pylab.figure(figsize=[size, size * ratio])
ax = fig.add_subplot(111)


pylab.hist(dist, normed=1, histtype='stepfilled', color = 'DarkSlateBlue', alpha=0.2, label="Observed EDC")
pylab.hist(dist, normed=1, histtype='step', color = 'DimGray')


#pylab.hist(dist, normed=1, label="Observed EDC")


pylab.plot(x, dss, label = r"DSS, 11 angstrom",  linestyle = "-", linewidth = 2, color='CornflowerBlue')
pylab.plot(x, dst, label = r"DST, 6.4 angstrom", linestyle = "-", linewidth = 2, color='Crimson')
pylab.plot(x, edc, label = r"EDC, 0 angstrom" , linestyle = "-", linewidth = 2, color='DarkOrchid')


pylab.rc('text', usetex=True)
pylab.rc('font', family='serif')



pylab.xlim([0.0, 30.0])
pylab.ylim([0.0, 0.5])
pylab.grid(True)

pylab.legend()
pylab.xlabel(r"$\mathrm{Ca-Ca\ Distance\ [angstrom]}$", fontsize=16)
pylab.ylabel(r"$\mathrm{Likelihood\ [a.u.]}$", fontsize=16)

ticks = [r"$%i$" % (k) for k in range(0,35,5)]

print ticks


pylab.xticks(range(0,35,5)  ,[r"$%i$" % (k) for k in range(0,35,5)], fontsize=16)
pylab.yticks(numpy.arange(0,0.6,0.1)  ,[r"$%3.1f$" % (k) for k in numpy.arange(0.0,0.6,0.1)], fontsize=16)

filename = "lognormal"
pylab.savefig(filename + "png")
pylab.savefig(filename)
os.system("pdfcrop " + filename + ".pdf " + filename + ".pdf > /dev/null")



