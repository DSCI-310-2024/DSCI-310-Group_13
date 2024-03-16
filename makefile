# Makefile
# An Zhou, Mar 2024

# This driver script completes the analysis of ...
# This script takes no arguments.

# example usage:
# make all

# run entire analysis
all: reports/quarto_report.html \
reports/quarto_report.pdf \
DATA/laptops.csv \
DATA/cleaned_data \
results/plots \
results/models

# data download
# download data
DATA/laptops.csv: script/download_data.py
	python script/download_data.py \
	DATA/laptops.csv \
	DATA/download.csv

# data cleaning
DATA/cleaned_data: DATA/laptops.csv script/data_cleaning.py
	python script/data_cleaning.py \
 	DATA/laptops.csv \
 	DATA/cleaned_data.csv

# plotting
results/plots: DATA/laptops.csv script/eda.py
	python script/eda.py \
 	DATA/laptops.csv \
	01

 
# modelling
results/models: DATA/laptops.csv script/modelling.py
	python script/modelling.py \
	DATA/laptops.csv \
	02

#render quarto report in HTML
reports/quarto_report.html: reports/quarto_report.qmd
	quarto render reports/quarto_report.qmd --to html --output-dir reports


# render quarto report in PDF
reports/quarto_report.pdf: reports/quarto_report.qmd
	quarto render reports/quarto_report.qmd --to pdf --output-dir reports