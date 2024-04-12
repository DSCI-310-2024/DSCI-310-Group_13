"""
This script is designed to perform data modeling on a given dataset to predict laptop prices. It includes steps to split the data, train a regression model, evaluate its performance, and visualize the evaluation metrics.

Usage:
    Run the script with required arguments specifying the input file and a prefix for output files.
    Example:
        python modelling.py --input-file='path/to/dataset.csv' --figure-prefix='output_metrics'

Arguments:
    input_file: The path to the CSV file containing the dataset to model.
    figure_prefix: A prefix for naming output metric files, which will be saved in the 'results' directory.

The script outputs evaluation metrics and saves a plot of these metrics in the 'results' directory.
"""

import os
import sys

from pylaptoppred.model import split_data, train_model, evaluate_model, plot_metrics

import pandas as pd
import matplotlib.pyplot as plt

import click

@click.command()
@click.argument('input_file')
@click.argument('figure_prefix')

def modelling(input_file, figure_prefix):
    """
    Executes the modeling process on the specified dataset and outputs evaluation metrics and plots.
    
    Parameters:
        input_file (str): Path to the input CSV file.
        figure_prefix (str): Prefix used to name the output metric plot file.
    """
    # Ensure the results directory exists
    results_dir = 'results'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # Read the data
    df = pd.read_csv(input_file)

    # Define the target variable
    target = 'Price'
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(df, target, test_size=0.2, random_state=42)

    # Train the model
    trained_model = train_model(X_train, y_train)

    # Evaluate the model
    metrics = evaluate_model(trained_model, X_test, y_test)
    
    # Plot and save the evaluation metrics
    metrics_filename = f"{figure_prefix}_metrics.png"
    plot_metrics(metrics, metrics_filename, results_dir)

    print(f"Metrics plot saved to {os.path.join(results_dir, metrics_filename)}")
    print("Evaluation Metrics:", metrics)

if __name__ == '__main__':
    modelling()