import click
import os


def copy_file(input_path, output_path):
    """This function copy a file from the input path to the output path.

    Args:
        input_path (str): Path of the file to be read.
        output_path (str): Path where the file will be saved.
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


def copy_file_command(input_path, output_path):
    """Command to copy a file from the input path to the output path.

    Args:
        input_path (str): Path of the file to be read.
        output_path (str): Path where the file will be saved.
    """
    copy_file(input_path, output_path)


if __name__ == '__main__':
    copy_file_command()
