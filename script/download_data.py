import click
import sys
import os


from pylaptoppred import copy_file


@click.command()
@click.argument('input_path')
@click.argument('output_path')
def download_data(input_path, output_path):
    """
    This script copies a file from the input path to the output path.

    Arguments:
    input_path -- Path of the file to be read.
    output_path -- Path where the file will be saved.
    """
    copy_file.copy_file(input_path, output_path)

if __name__ == '__main__':
    download_data()
