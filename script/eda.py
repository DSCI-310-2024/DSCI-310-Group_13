import click
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from altair_saver import save
import os

@click.command()
@click.argument('input_file')
@click.argument('figure_prefix')
def eda(input_file, figure_prefix):
    # Ensure the Visualizations directory exists
    visualizations_dir = 'Visualizations'  # Directly in the project root
    if not os.path.exists(visualizations_dir):
        os.makedirs(visualizations_dir)

    # Read the data
    df = pd.read_csv(input_file)
    
    #first graph: brand distribution
    categorical = df.select_dtypes(include=['object'])
    plt.figure(figsize=(13,7))
    brand_counts = categorical.brand.value_counts()
    axis = sns.barplot(x=brand_counts.index, y=brand_counts.values)
    axis.bar_label(axis.containers[0], fontsize=7)
    plt.xlabel('Brand')
    plt.ylabel('Count')
    plt.title('Brand distribution')
    plt.xticks(rotation=45)
    # Ensure the Visualisations directory exists
    visualisations_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Visualisations')
    os.makedirs(visualisations_dir, exist_ok=True)

    # Save the plot with an absolute path
    output_path = os.path.join(visualisations_dir, f'{figure_prefix}_brand_distribution.png')
    plt.savefig(output_path)
    plt.close()

if __name__ == '__main__':
    eda()
