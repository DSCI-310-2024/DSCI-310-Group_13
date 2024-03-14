import click
import pandas as pd
import numpy as np

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
    # Read the data
    df = pd.read_csv(input_file)

    # Basic data cleaning
    # Drop rows where any data is missing
    df_cleaned = df.dropna()

    # Drop duplicate rows, keep the first occurrence
    df_cleaned = df_cleaned.drop_duplicates()

    # Removing outliers using the IQR method, but only for numeric columns
    numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns
    Q1 = df_cleaned[numeric_cols].quantile(0.25)
    Q3 = df_cleaned[numeric_cols].quantile(0.75)
    IQR = Q3 - Q1

    # Define a mask to filter out outliers only for numeric columns
    filter = ~((df_cleaned[numeric_cols] < (Q1 - 1.5 * IQR)) | (df_cleaned[numeric_cols] > (Q3 + 1.5 * IQR))).any(axis=1)
    df_final = df_cleaned[filter]

    # Save the cleaned data
    df_final.to_csv(output_file, index=False)

    click.echo(f"Data cleaned and saved to {output_file}")

if __name__ == '__main__':
    clean_and_save_data()
