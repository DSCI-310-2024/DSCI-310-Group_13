import pandas as pd
import numpy as np
import pytest
import sys
import os
"""
How to run test: pytest tests/test_data_cleaning.py
"""

# Adjust the path to include the src directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from function_data_cleaning import clean_and_save_data

def test_clean_and_save_data(tmp_path):
    # Sample data creation
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 10, 6, 7, 8, 900],
        'B': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
        'C': [2, 3, 4, 5, 6, 7, 8, 9, 10]
    })
    
    # Use pytest's tmp_path fixture to create a temporary CSV file
    temp_input_file = tmp_path / "input.csv"
    temp_output_base = tmp_path / "output"
    
    # Write sample data to temporary input file
    df.to_csv(temp_input_file, index=False)
    
    # Run the cleaning and splitting function
    clean_and_save_data(str(temp_input_file), str(temp_output_base))
    
    # Read the output files back in
    df_train = pd.read_csv(f"{temp_output_base}_train.csv")
    df_test = pd.read_csv(f"{temp_output_base}_test.csv")
    
    # Perform your assertions here
    assert not df_train.empty, "Training DataFrame should not be empty"
    assert not df_test.empty, "Test DataFrame should not be empty"
    assert 'A' in df_train.columns, "DataFrame should contain column 'A'"
    assert df_train['A'].max() < 900, "Outliers should have been removed from column 'A'"

def test_clean_and_save_data_no_nulls_duplicates():
    # Setup: Create a sample clean dataset
    sample_data = pd.DataFrame({
        'A': range(1, 6),
        'B': list('abcde')
    })
    input_path = '../data/raw/clean_sample.csv'
    output_path = '../data/processed/cleaned_output.csv'
    sample_data.to_csv(input_path, index=False)
    
    # Action: Run the cleaning function
    clean_and_save_data(input_path, output_path)
    
    # Assert: The output file exists and matches the input
    assert os.path.exists(output_path)
    output_data = pd.read_csv(output_path)
    assert output_data.equals(sample_data)



def test_read_save_data_with_empty_file():
    directory_path = '../DATA'
    empty_file_path = os.path.join(directory_path, 'empty.csv')
    
    # Ensure the directory exists
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    
    # Now attempt to create the file
    with open(empty_file_path, 'w') as f:
        pass

    empty_output_path = '../DATA/empty_output.csv'
    with pytest.raises(ValueError):  # Assuming your function raises ValueError for empty input
        clean_and_save_data(empty_file_path, empty_output_path)
    os.remove(empty_file_path)
