# Makefile
# An Zhou, Mar 2024

# This driver script completes the analysis of ...
# This script takes no arguments.

# example usage:
# make all

# run entire analysis
<<<<<<< Updated upstream
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
=======
all: reports/quarto_report.html DATA/cleaned_data.csv DATA/downloaded.csv 

# data cleaning
DATA/cleaned_data.csv : DATA/laptop.csv script/cleaning.py
    python script/data_cleaning.py DATA/laptops.csv DATA/cleaned_data.csv

# download data
DATA/downloaded.csv : DATA/laptop.csv scriptdownload_data.py
    python script/download_data.py DATA/laptops.csv DATA/download.csv
>>>>>>> Stashed changes

# render quarto report in HTML
reports/quarto_report.html: reports/quarto_report.qmd
	quarto render reports/quarto_report.qmd --to html --output-dir reports


clean-dats:
clean-all: 