import sys
import os
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.download_data import download_data

def test_download_data_data(tmpdir):
    input_path = os.path.join(tmpdir, 'input.txt')
    with open(input_path, 'w') as f:
        f.write('Sample data to copy.')

    output_path = os.path.join(tmpdir, 'output.txt')

    download_data(input_path, output_path)

    assert os.path.exists(output_path)
    with open(output_path, 'r') as f:
        assert f.read() == 'Sample data to copy.'

def test_download_data_empty_input(tmpdir):
    input_path = os.path.join(tmpdir, 'empty_input.txt')
    output_path = os.path.join(tmpdir, 'output.txt')

    open(input_path, 'a').close()

    download_data(input_path, output_path)

    assert os.path.exists(output_path)
    assert os.stat(output_path).st_size == 0
