import click
import os
import altair as alt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import altair_saver
import sys

from pylaptoppred import save_plot

@click.command()
@click.argument('input_file')
@click.argument('figure_prefix')
def eda(input_file, figure_prefix):
    # Ensure the Visualizations directory exists
    visualisations_dir = 'Visualisations'  # Directly in the project root
    if not os.path.exists(visualisations_dir):
        os.makedirs(visualisations_dir)



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
    output_path = os.path.join(visualisations_dir)
    plt_obj = plt.gcf()

    # CHANGE 1
    save_plot.save_plot(plt_obj, f'{figure_prefix}_brand_distribution.png', output_path)
    plt.close()
    print("success!\n")


    #second graph: price distributio plot
    df['Price'] = df['Price'].astype(int)

    # Create a histogram of laptop prices
    chart = alt.Chart(df).mark_bar(
        color='#7ca0ff',  # Bar color
        opacity=0.7       # Bar opacity
    ).encode(
        x=alt.X('Price:Q', bin=alt.Bin(maxbins=40), title='Price (USD)'),
        y=alt.Y('count()', title='Frequency'),
        tooltip=[alt.Tooltip('count()', title='Frequency'), alt.Tooltip('Price:Q', title='Price Range')]
    ).properties(
        title='Distribution of Laptop Prices',
        width=600,
        height=400
    )
    output_path = os.path.join(visualisations_dir)

    save_plot.save_plot(chart, f'{figure_prefix}_price_distribution.png', output_path)
    print("success! \n")

    # chart.save(output_path,scale_factor=2.0)

    #third chart
    plt.figure(figsize=(8,6))
    sns.barplot(data=df, x='processor_brand', y='Price')
    plt.title('Barplot b/w Price and processor_brand')
    # Save the plot with an absolute path
    output_path = os.path.join(visualisations_dir)

    plt_obj = plt.gcf()

    save_plot.save_plot(plt_obj, f'{figure_prefix}_Barplot_Price_processor_brand.png', output_path)
    plt.close()
    print("success! \n")

    #fourth plot
    plt.figure(figsize=(13,7))
    processor_tier_counts = categorical['processor_tier'].value_counts()
    axis = sns.barplot(x=processor_tier_counts.index, y=processor_tier_counts.values)
    axis.bar_label(axis.containers[0], fontsize=10)
    plt.xlabel('Processor type')
    plt.ylabel('Count')
    plt.title('Processor types')
    # Save the plot with an absolute path
    output_path = os.path.join(visualisations_dir, )

    plt_obj = plt.gcf()

    save_plot.save_plot(plt_obj, f'{figure_prefix}_processor_distribution.png', output_path)
    plt.close()
    print("success! \n")

    #fifth plot

    # Create a list of columns for which we want to create histograms
    columns = ['Rating', 'num_cores', 'num_threads', 'ram_memory', 
            'primary_storage_capacity', 'secondary_storage_capacity', 
            'display_size', 'resolution_width', 'resolution_height', 'Price']

    # Create a chart for each column and store them in a list
    charts = [
        alt.Chart(df).mark_bar().encode(
            x=alt.X(f'{col}:Q', bin=True),  # Q for quantitative data
            y=alt.Y('count()', title='Frequency'),
            tooltip=[alt.Tooltip(f'{col}:Q', title=col)]
        ).properties(
            title=f'Distribution of {col}',
            width=200,
            height=150
        )
        for col in columns
    ]

    # Combine charts into a grid layout
    chart_grid = alt.vconcat(*[
        alt.hconcat(*charts[i:i+3])  # 3 charts per row
        for i in range(0, len(charts), 3)
    ])

    output_path = os.path.join(visualisations_dir)


    save_plot.save_plot(chart_grid, f'{figure_prefix}_grid_1.png', output_path)
    print("success! \n")

    #sixth plot
        

    # Map columns to units for those that are quantitative
    units_mapping = {
        'brand': '',
        'Model': '',
        'Rating': 'Stars',
        'processor_brand': '',
        'processor_tier': '',
        'num_cores': 'Cores',
        'num_threads': 'Threads',
        'ram_memory': 'GB',
        'primary_storage_type': '',
        'primary_storage_capacity': 'GB',
        'secondary_storage_type': '',
        'secondary_storage_capacity': 'GB',
        'gpu_brand': '',
        'gpu_type': '',
        'is_touch_screen': '',
        'display_size': 'Inches',
        'resolution_width': 'Pixels',
        'resolution_height': 'Pixels',
        'OS': '',
        'year_of_warranty': 'Years',
        'Price': 'USD'
    }

    # Columns of interest
    columns = list(units_mapping.keys())

    # Define a color-blind-friendly "rainbow" palette
    colors = ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7', '#999999']
    # Ensure we have enough colors
    colors *= (len(columns) // len(colors) + 1)

    # Create charts
    charts = []
    for i, col in enumerate(columns):
        title = f'{col} ({units_mapping[col]})'  # Include units in title
        chart = alt.Chart(df).mark_bar(color=colors[i]).encode(
            x=alt.X(f'{col}:Q', bin=True, title=title),
            y=alt.Y('count()', title='Frequency'),
            tooltip=[alt.Tooltip(f'{col}:Q', title=col)]
        ).properties(
            width=180,
            height=140
        )
        charts.append(chart)

    # Combine charts into a grid layout without explicit titles
    chart_grid = alt.vconcat(*[
        alt.hconcat(*charts[i:i+3]) for i in range(0, len(charts), 3)
    ]).configure_axis(
        titleFontSize=12,
        labelFontSize=10
    )
    output_path = os.path.join(visualisations_dir)

    save_plot.save_plot(chart_grid,  f'{figure_prefix}_grid_2.png', output_path)
    print("success! \n")



if __name__ == '__main__':
    eda()
