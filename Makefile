THESIS=thesis
LATEX=pdflatex
BIBTEX=bibtex

all:
	${LATEX}  ${THESIS}.tex
	${BIBTEX} ${THESIS}.aux
	${LATEX}  ${THESIS}.tex
	${LATEX}  ${THESIS}.tex

clean:
	rm ${THESIS}.aux ${THESIS}.bbl ${THESIS}.blg ${THESIS}.out ${THESIS}.log tex/*.aux
