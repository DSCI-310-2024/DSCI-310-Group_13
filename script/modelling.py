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