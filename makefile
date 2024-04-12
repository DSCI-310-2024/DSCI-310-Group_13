# Makefile
# An Zhou, Mar 2024

# This driver script completes the analysis needed in the project report. 
# This script downloads data from local, clean the data and store the cleaned data sets in DATA.
# This script produces report in .html and .pdf, renders the figrues needed and stores them in correspondin folders.
# This script takes no arguments.

# example usage:
# make all

# run entire analysis
all: DATA/laptops.csv \
	DATA/cleaned_data \
	results/plots \
	results/models \
	reports/quarto_report.html \
	reports/quarto_report.pdf

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
	quarto render reports/quarto_report.qmd --to html


# render quarto report in PDF
reports/quarto_report.pdf: reports/quarto_report.qmd
	quarto render reports/quarto_report.qmd --to pdf`


# 'make clean' will remove targeted files in clean:
clean:
	rm -rf DATA/cleaned_data.csv_train.csv
	rm -rf DATA/cleaned_data.csv_test.csv
	rm -rf Visualisations/01_Barplot_Price_processor_brand.png \
		Visualisations/01_processor_distribution.png \
		Visualisations/01_brand_distribution.png \
		Visualisations/01_grid_1.png \
		Visualisations/01_grid_2.png \
		Visualisations/01_price_distribution.png
	rm -rf results/02_brand_distribution.png \
		results/02_summary_stats.png
	rm -rf reports/quarto_report.html\
		reports/quarto_report.pdf