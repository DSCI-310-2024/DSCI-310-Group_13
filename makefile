# Makefile
# An Zhou, Mar 2024

# This driver script completes the analysis of ...
# This script takes no arguments.

# example usage:
# make all

# run entire analysis
all: reports/quarto_report.html



# render quarto report in HTML
reports/quarto_report.html: reports/quarto_report.qmd
	quarto render reports/quarto_report.qmd \
        --to html \
        --output-dir reports

# make eda plots
#results/visualization : scripts/eda.py results/clean.csv
#	python scripts/plotcount.py \
		--input_file=results/isles.dat \
		--output_file=results/figure/isles.png


#clean-dats:
#clean-all: 