#!/bin/bash

pdflatex -interaction=nonstopmode $1.tex
makeglossaries $1
bibtex $1
pdflatex -interaction=nonstopmode $1.tex
pdflatex -interaction=nonstopmode $1.tex

### Move files to build 
mv $1.pdf build/$1.pdf
mv $1.log build/$1.log
mv $1.aux build/$1.aux
mv $1.bbl build/$1.bbl
mv $1.out build/$1.out
mv $1.toc build/$1.toc
mv $1.lof build/$1.lof
mv $1.lot build/$1.lot
mv $1.blg build/$1.blg
mv $1.acn build/
mv $1.acr build/
mv $1.ist build/
mv $1.alg build/
mv $1.glg build/
mv $1.glo build/
mv $1.gls build/
###
