#!/usr/bin/python

import sys
import os
import string

import numpy as np

from matplotlib import pyplot

CM_TO_INCHES = 1.0/2.45

pyplot.rc('text', usetex=True)
pyplot.rc('font', **{'family': 'serif',
                     'serif': ['Computer Modern'],
                     'size' : 12})

# Set size on paper:                Width            Height
pyplot.rcParams['figure.figsize'] = 8*CM_TO_INCHES*1.3, 6*CM_TO_INCHES*1.3

lines = sys.stdin.readlines()

max_e = 9999999999


if len(sys.argv) > 1:
    max_e = float(sys.argv[1])
    print "Max E is set to:", max_e


energies = []
rmsds = []

min_energy = 1000000.0

for line in lines:

    if "sample" in line:

        mc_energy   = float(string.split(line)[1])

        rmsd        = float(string.split(line)[-2])

        #  profasi     = float(string.split(line)[-4]) + \
        #                float(string.split(line)[-5]) + \
        #                float(string.split(line)[-6]) + \
        #                float(string.split(line)[-7]) + \
        #                float(string.split(line)[-8]) + \
        #                float(string.split(line)[-9]) + \
        #                float(string.split(line)[-10])

        torus_energy = float(string.split(line)[-1])

        energy = (mc_energy + torus_energy)/1.67

        if energy < min_energy:
            print line
            min_energy = energy

        if energy < max_e:
            energies.append(energy)
            rmsds.append(rmsd)


pyplot.figure
pyplot.ylabel(r'Profasi + TorusDBN-CS Energy [kcal/mol]')
pyplot.xlabel(r'CA-RMSD [\AA]')

pyplot.grid(True)
pyplot.plot(rmsds, energies, "k.")
pyplot.savefig("temp.png", dpi=200 , bbox_inches='tight')

# filename = "temp.pdf"
# pyplot.savefig(filename)
# os.system("pdfcrop %s %s" % (filename, filename))



