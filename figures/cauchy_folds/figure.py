from matplotlib import pyplot


linecolor = ["r",
             "g",
             "b",
             "c",
             "m",
             "r",
             "g",
             "b",
             "c",
             "m",
             "y",
             "k",]
linestyle = ["-",
             "-",
             "-",
             "-",
             "-",
             "-",
             "-",
             "-",
             "-",
             "-",
             "-",
             "-"]

protein_g_data =[
[10,  1,   0,   0,       8 ,  2,   0 ,  0 ,      20  ,6  , 2 ,  0],
[13,  7,   5,   1,       12,  7,   5 ,  1 ,      17  ,14 , 8 ,  6],
[17,  3,   0,   0,       15,  6,   0 ,  0 ,      20  ,17 , 2 ,  0],
[14,  5,   3,   0,       14,  4,   3 ,  0 ,      20  ,15 , 4 ,  2],
[1 ,  0,   0,   0,       1 ,  1,   0 ,  0 ,      18  ,1  , 0 ,  0],
[7 ,  3,   0,   0,       8 ,  1,   0 ,  0 ,      20  ,7  , 1 ,  0],
[8 ,  3,   1,   0,       7 ,  2,   1 ,  0 ,      13  ,8  , 1 ,  1]]

labels = ["Gauss Fixed Sigma",
          "Cauchy Fixed Gamma",
          "Cauchy Variable Gamma",
          "Cauchy Variable Gamma*",
          "Square Well",
          "Marginalized Weight",
          "No CamShift/TorusCS"]

enhd_data = [
[14 , 4 ,  2,   0,       11,  6,   1,   0 ,      20,  20 , 17,  0],
[8  , 2 ,  0,   0,       4 ,  4,   1,   0 ,      12,  9  , 6 ,  0],
[2  , 0 ,  0,   0,       2 ,  1,   0,   0 ,      5 ,  3  , 3 ,  1],
[10 , 3 ,  0,   0,       12,  2,   0,   0 ,      20,  17 , 12,  0],
[0  , 0 ,  0,   0,       0 ,  0,   0,   0 ,      2 ,  0  , 0 ,  0],
[11 , 6 ,  4,   0,       9 ,  8,   3,   0 ,      17,  17 , 16,  0],
[0  , 0 ,  0,   0,       0 ,  0,   0,   0 ,      10,  2  , 1 ,  0]]




x_labels = [5.0, 3.0, 2.0, 1.0]
CM_TO_INCHES = 1.0/2.45

pyplot.rc('text', usetex=True)
pyplot.rc('font', **{'family': 'serif',
                         'serif': ['Computer Modern'],
                                              'size' : 12})

cm = pyplot.get_cmap('Accent')
pyplot.figure(figsize=[8,10])


NUM_COLORS = 7

for i in range(6):

    pyplot.subplot(321 + i)

    pyplot.xlim([0.5, 5.5])
    pyplot.ylim([0.0, 20])

    pyplot.grid(True)
    pyplot.xlabel("CA-RMSD [angstrom]")
    pyplot.ylabel("\# Threads")



    if i == 0:
        pyplot.title("(a) Protein G, Profasi + Camshift")
        for j, data in enumerate(protein_g_data):
            pyplot.plot(x_labels, data[:4],
                        color = cm(1.*j/NUM_COLORS),
                        marker = "o",
                        linestyle = linestyle[j],
                        label=labels[j])
        pyplot.legend(loc='center left',
                      bbox_to_anchor=(0.02, 1.8),
                      ncol=2)


    if i == 1:
        pyplot.title("(b) ENDH, Profasi + Camshift")
        for j, data in enumerate(enhd_data):
            pyplot.plot(x_labels, data[:4],
                        color = cm(1.*j/NUM_COLORS),
                        marker = "o",
                        linestyle = linestyle[j])

    if i == 2:
        pyplot.subplots_adjust(hspace = 0.4)
        pyplot.title("Protein G, E += Torus")
        for j, data in enumerate(protein_g_data):
            pyplot.plot(x_labels, data[4:8],
                        color = cm(1.*j/NUM_COLORS),
                        marker = "o",
                        linestyle = linestyle[j])

    if i == 3:
        pyplot.title("(c) ENHD, E += Torus")
        for j, data in enumerate(enhd_data):
            pyplot.plot(x_labels, data[4:8],
                        color = cm(1.*j/NUM_COLORS),
                        marker = "o",
                        linestyle = linestyle[j])

    if i == 4:
        pyplot.title("(c) Protein G, Min. RMSD")
        for j, data in enumerate(protein_g_data):
            pyplot.plot(x_labels, data[8:12],
                        color = cm(1.*j/NUM_COLORS),
                        marker = "o",
                        linestyle = linestyle[j])

    if i == 5:
        pyplot.title("(d) ENHD, Min. RMSD")
        for j, data in enumerate(enhd_data):
            pyplot.plot(x_labels, data[8:12],
                        color = cm(1.*j/NUM_COLORS),
                        marker = "o",
                        linestyle = linestyle[j])

pyplot.savefig("cauchy_folds.png",  bbox_inches='tight')
pyplot.savefig("cauchy_folds.pdf",  bbox_inches='tight')
