import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import os

from imblearn.over_sampling import SMOTE

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, roc_curve, classification_report, accuracy_score, confusion_matrix, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC, LinearSVC
import statsmodels.api as sm

def modeling(input_file, figure_prefix):
    # Ensure the Visualizations directory exists
    results_dir = 'results'  # Directly in the project root
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # Read the data
    df = pd.read_csv(input_file)
    
    np.random.seed(987654321)

    price = df["Price"]
    num_samples = len(price)
    train_ratio = 0.7
    num_train_samples = int(train_ratio * num_samples)

    # Randomly select indices for the training set
    which_train = np.random.choice(range(num_samples), size=num_train_samples, replace=False)

    # Split the data into training and testing sets based on the selected indices
    train = df.iloc[which_train].copy()
    test = df.drop(which_train).copy()

    freq_ratio = train.apply(lambda x: x.value_counts().iloc[0] / x.value_counts().iloc[1] if len(x.value_counts()) > 1 else float('nan'))

    # Prepare the formula for only numeric variables
    formula = 'Price ~ Rating + num_cores + num_threads + ram_memory + primary_storage_capacity + secondary_storage_capacity + is_touch_screen + display_size + resolution_width + resolution_height' 
    # + C(brand) + C(Model) + C(processor_brand) + C(processor_tier) + C(primary_storage_type) + C(secondary_storage_type) + C(gpu_brand) + C(gpu_type) + C(OS) + C(year_of_warranty)'

    # Fit OLS model
    model = sm.formula.ols(formula=formula, data=train)
    price_lm = model.fit()

    # Visualize Coefficients

    coefficients = {
        'Intercept': -2406.9394,
        'is_touch_screen': 6.2640,
        'Rating': 13.6645,
        'num_cores': 76.4062,
        'num_threads': -30.0025,
        'ram_memory': 13.4003,
        'primary_storage_capacity': 0.5079,
        'secondary_storage_capacity': -0.6392,
        'display_size': 31.1784,
        'resolution_width': 0.3118,
        'resolution_height': 0.5292
    }

    plt.figure(figsize=(10, 6))
    plt.bar(coefficients.keys(), coefficients.values(), color='skyblue')
    plt.title('Coefficients of Independent Variables')
    plt.xlabel('Independent Variables')
    plt.ylabel('Coefficient Value')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    # Ensure the Visualisations directory exists
    results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'results')
    os.makedirs(results_dir, exist_ok=True)
    # Save the plot with an absolute path
    output_path = os.path.join(results_dir, f'{figure_prefix}_brand_distribution.png')
    plt.savefig(output_path)
    plt.close()

if __name__ == '__main__':
    modeling()
