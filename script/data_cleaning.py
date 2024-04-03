import click
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from function_data_cleaning import clean_and_save_data_f



@click.command()
@click.argument('input_file')
@click.argument('output_file')
def clean_and_save_data(input_file, output_file):
    """
    This script reads data from a specified input file, performs data cleaning by removing outliers using the IQR method on numeric columns,
    drops duplicate rows, handles missing values by dropping rows with missing data, and saves the cleaned data to a specified output file.

    Arguments:
    input_file -- Path/filename of the data to be read in.
    output_file -- Path/filename where the cleaned/processed data will be saved.
    """
    # Call the function from function.py
    df_train, df_test = clean_and_save_data_f(input_file, output_file)
    
    click.echo(f"Data cleaned and saved to {output_file}_train.csv and {output_file}_test.csv")

if __name__ == '__main__':
    clean_and_save_data()
