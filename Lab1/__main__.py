# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m proj0'. This file is NOT run during
# imports. This whole file is the java equivalent of:
# public static void main(string args[]), or c's int main();

# Generally used to process command line arguments and 'launch' the program
# Importing necessary modules
from pathlib import Path  # Path module for working with file paths
import argparse  # Module for parsing command-Line arguments

# Import functions from Lab1 package
from Lab1 import process_files
from Lab1.Lab1 import enhance_process_files

# Setting up argument parsing for command-line usage
arg_parser = argparse.ArgumentParser()  # Creating an ArgumentParser object
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")  # Adding argument for input file path
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")  # Adding argument for output file path
arg_parser.add_argument("enhanced", type=str, help="Run enhanced or not", choices=['postfix', 'enhanced'])
args = arg_parser.parse_args()  # Parsing command-line arguments

# Converting input and output file paths to Path objects for convenience
in_path = Path(args.in_file)  # Creating a Path object for input file
print(in_path.absolute())  # Printing the absolute path of the input file (for Grading)
out_path = Path(args.out_file)  # Creating a Path object for output file

user_choice = False  # Initializing a flag for user choice

# arg parser for user's choice
#  If user wants basic postfix conversion
if args.enhanced == 'postfix':
    with in_path.open('r') as input_file, out_path.open('w') as output_file:
        process_files(input_file, output_file)
# otherwise if user wants enhanced prefix to infix and postfix conversion
else:
    with in_path.open('r') as input_file, out_path.open('w') as output_file:
        enhance_process_files(input_file, output_file)  # Applying enhancement to file and writing to output file
