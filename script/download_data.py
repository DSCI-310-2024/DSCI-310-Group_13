import click
from src.download_data import download_data


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
    try:
        # Open the input file and read its contents
        with open(input_path, 'r') as file:
            data = file.read()
        
        # Write the contents to the output file
        with open(output_path, 'w') as file:
            file.write(data)

        click.echo(f"File successfully copied from {input_path} to {output_path}")
    except Exception as e:
        click.echo(f"Failed to copy the file: {e}")

if __name__ == '__main__':
    download_data()
