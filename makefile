# Makefile
# An Zhou, Mar 2024

# This driver script completes the analysis of ...
# This script takes no arguments.

# example usage:
# make all

# run entire analysis
all: all: results/laptop.dat reports/quarto_report.html

# data cleaning
results/laptop.dat : data/laptop.csv data_cleaning.py
	python script/data_cleaning.py
	    --input_file = data/laptop.csv \
        --output_file = results/laptop.dat

# download data
results/laptop.dat : data/laptop.csv download_data.py
	python script/download_data.py
	    --input_file = data/laptop.csv \
        --output_file = results/laptop.dat

# explanatory data analysis

# make the plot

# write the report

# render quarto report in HTML
reports/quarto_report.html: reports/quarto_report.qmd
	quarto render reports/quarto_report.qmd --to html --output-dir reports


clean-dats:
clean-all: 