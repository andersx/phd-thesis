#!/usr/bin/python

import sys
import string
from matplotlib import pyplot

lines = sys.stdin.readlines()


energies = []
rmsds = []
min_energy = 1000000000

for line in lines:

    if "sample" in line:

        energy = float(string.split(line)[-1])
        rmsd    = float(string.split(line)[-2])


        # print energy, rmsd

        if energy < min_energy:
            print line
            min_energy = energy

        energies.append(energy)
        rmsds.append(rmsd)

CM_TO_INCHES = 1.0/2.45
pyplot.rc('text', usetex=True)
pyplot.rc('font', **{'family': 'serif',
                     'serif': ['Computer Modern'],
                     'size' : 12})

pyplot.figure(figsize=[12*CM_TO_INCHES, 8* CM_TO_INCHES])

pyplot.xlabel("CA-RMSD [angstrom]")
pyplot.ylabel("Total Energy [kcal/mol]")
pyplot.ylim([243000,245500])
pyplot.xlim([2.0,4.0])
pyplot.grid(True)
pyplot.plot(rmsds, energies, "k.")
pyplot.savefig("savinase_refinement.pdf", bbox_inches='tight')



