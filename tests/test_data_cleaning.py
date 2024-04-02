import pandas as pd
import numpy as np
from tempfile import NamedTemporaryFile
import pytest
from your_module_name import clean_and_save_data  # Adjust the import path based on your project structure

# Sample data for testing
@pytest.fixture
def sample_data():
    # Creating a simple DataFrame with some outliers and missing values
    data = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 10, 6, 7, 8, 900],
        'B': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
        'C': [2, 3, 4, 5, 6, 7, 8, 9, 10]
    })
    return data

# Test for correct cleaning and splitting
def test_clean_and_save_data(sample_data):
    with NamedTemporaryFile(delete=False, mode='w', newline='', suffix='.csv') as tmp:
        sample_data.to_csv(tmp.name, index=False)
        tmp_path = tmp.name.replace('.csv', '')  # Base path for output files

    # Run the data cleaning and splitting function
    train, test = clean_and_save_data(tmp.name, tmp_path)

    # Assertions
    assert isinstance(train, pd.DataFrame), "Training set should be a DataFrame"
    assert isinstance(test, pd.DataFrame), "Test set should be a DataFrame"
    assert not train.isnull().values.any(), "Training set should not have any null values"
    assert not test.isnull().values.any(), "Test set should not have any null values"
    assert 0 < len(train) < len(sample_data), "Training set should be smaller than the original dataset but not empty"
    assert 0 < len(test) < len(sample_data), "Test set should be smaller than the original dataset but not empty"

    # Check if outliers were removed correctly
    # Assuming column 'A' had outliers
    assert train['A'].max() < 900, "Outliers in column 'A' should have been removed"
    assert test['A'].max() < 900, "Outliers in column 'A' should have been removed"

# Ensure cleanup of temporary files if necessary
