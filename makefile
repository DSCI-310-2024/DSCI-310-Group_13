# Makefile
# An Zhou, Mar 2024

# This driver script completes the analysis of ...
# This script takes no arguments.

# example usage:
# make all

# run entire analysis
# all: reports/quarto_report.html
all : results/visualization \
reports/quarto_report.pdf


# data cleaning
DATA/cleaned_data: DATA/laptops.csv script/data_cleaning.py
    python script/data_cleaning.py \
        --input_file=DATA/laptops.csv \
        --output_file=DATA/cleaned_data

# make eda plots
results/visualization : script/eda.py DATA/laptops.csv
    python script/eda.py DATA/laptops.csv 01 \
        --input_file=DATA/laptops/csv\
        --output_file=results/visualization

# #render quarto report in HTML
# reports/quarto_report.html: reports/quarto_report.qmd
# 	quarto render reports/quarto_report.qmd \
#         --to html \
#         --output-dir reports

# render quarto report in PDF
reports/quarto_report.pdf: reports/quarto_report.qmd
	quarto render reports/quarto_report.qmd \
        --to pdf \
        --output-dir reports

# 'make clean' will remove targeted files in clean:
# clean:
# 	rm -rf data/raw/raw_data.csv
# 	rm -rf data/processed/processed_data.csv
# 	rm -rf results/cross_validation_results.csv \
# 		results/crime_coefficients.csv\
# 		results/dummy_results.csv
# 	rm -rf results/time_period_plot.png \
# 		results/records_by_time_and_day_plot.png \
# 		results/coefficients_of_lr_model_plot.png
# 	rm -rf reports/quarto_reports.html \
# 		reports/quarto_reports.pdf