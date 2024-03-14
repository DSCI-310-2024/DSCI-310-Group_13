import click
import requests
from shutil import copyfile
import os

@click.command()
@click.argument('input_path')
@click.argument('output_path')
def download_and_save(input_path, output_path):
    """
    This script downloads a file from a given URL or copies a file from a local path
    and saves it to a new location with a specified filename.

    Arguments:
    input_path -- The URL or local path to the file to be downloaded or copied.
    output_path -- The path and filename where the file will be saved.
    """
    if input_path.startswith('http://') or input_path.startswith('https://'):
        # Handle URL download
        try:
            response = requests.get(input_path)
            response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
            with open(output_path, 'wb') as f:
                f.write(response.content)
            click.echo(f"File downloaded and saved to {output_path}")
        except requests.exceptions.RequestException as e:
            click.echo(f"Failed to download the file: {e}")
    else:
        # Handle local file copy
        if os.path.isfile(input_path):
            try:
                copyfile(input_path, output_path)
                click.echo(f"File copied to {output_path}")
            except IOError as e:
                click.echo(f"Failed to copy the file: {e}")
        else:
            click.echo("The input path does not exist or is not a file.")

if __name__ == '__main__':
    download_and_save()
