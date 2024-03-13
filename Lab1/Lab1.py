import sys
import time
from typing import TextIO
from Lab1.error_invalid_expression import ErrorInvalidExpression
from Lab1.postfix_converter import PostfixConverter
from Lab1.runtime_metric import RuntimeMetric
from Lab1.infix_converter import InfixConverter


def is_operator(char) -> bool:
    """
    Checks if a character is an operator. It also checks if there is a caret ^ character
    and replaces $ as an exponent

    Args:
        char (str): The character to be checked.

    Returns:
        bool: True if the character is an operator, False otherwise.
    """
    if char == '^':
        return True
    return char in ['+', '-', '*', '/', '$']


def is_empty_line(line):
    """
    Checks if a line is empty.

    :param line: The line to be checked.
    :return: True if the line is empty, False otherwise.
    """
    for char in line:
        if not char.isspace():
            return False
    return True


def is_valid_prefix(expression):
    """
    Validates a prefix expression.

    :param expression: The prefix expression to be validated.
    :return: True if the expression is valid.
    :raises ValueError: If the expression is not valid.
    """
    operands = 0
    operators = 0
    line_is_empty = '\n'
    # if there is no expression and only an empty line
    if expression == line_is_empty:
        return False
    # for each expression
    for char in expression:
        # check if is alphabetical or numeric skip, any spaces
        if (not char.isspace() and char.isalpha()) or (not char.isspace() and char.isnumeric()):
            # count operand
            operands += 1
        # otherwise if it is an operator, skip any spaces
        elif not char.isspace() and is_operator(char):
            #  count operator
            operators += 1
    #  if the operator is equals to the operands - 1
    #  First rule of a prefix expression
    if operators == operands - 1:
        # is a valid expression
        return True
    else:
        raise ValueError("The total number of operators should be one less than the number of operands: "
                         "{}".format(expression))


def process_files(input_file: TextIO, output_file: TextIO) -> None:
    """
    Processes prefix expressions from an input file and writes converted expressions to an output file.
    This function is the main function of the program, and it takes input and uses classes and functions
    in order to run the program as a whole.

    :param input_file: Input file containing prefix expressions.
    :param output_file: Output file to write converted expressions.
    """
    # Initialize empty list to store runtime metrics
    runtime_metrics = []
    start_time = 0

    # this variable will track how many conversions per file
    total_conversions = 0
    # counts number of error in the file
    total_errors = 0
    # Stores each line into next_line
    next_line = input_file.readline()
    file_size = len(next_line)  # approved by Mr. Almes

    # Iterates through the input file to process all lines.
    # use  pathlib path object replaces the Os file pass path lib path library.
    output_file.write('PREFIX TO POSTFIX CONVERSION\n')
    output_file.write('-----------------------------\n\n')
    # iterates through the file reading each line as long as there's character to read.
    while next_line is not None and next_line != "":
        start_time = time.time_ns()  # Measure start time
        try:
            # Validates the expression that is read by the program before moving on.
            is_valid = is_valid_prefix(next_line)

            # Checks for valid prefix expressions.
            if is_valid:
                # Initiates an instance of PostfixConverter class
                converter = PostfixConverter(next_line)
                converter.reverse()  # reverses the prefix expression
                postfix = converter.to_postfix()  # This converts the prefix to postfix
                output_file.write(f'This is the Original Prefix : {next_line} ')
                output_file.write(f'This is the converted Postfix Expression: {postfix}')
                total_conversions += 1

        except ValueError as e:  # calls Value error if expression is incorrect
            output_file.write(f'\n')
            total_errors += 1
            print(f'Your prefix expression "{next_line} is invalid: {e}', file=sys.stderr)
            output_file.write(f'Your prefix expression "{next_line} is invalid: {e}\n')

        except ErrorInvalidExpression as e:  # calls ErrorInvalidExpression if prefix expression is invalid
            output_file.write(f'\n')
            total_errors += 1
            print(f'Your prefix expression "{next_line} is invalid: {e}', file=sys.stderr)
            output_file.write(f'Your prefix expression "{next_line} is invalid: {e}\n')

        next_line = input_file.readline()
        output_file.write(f'\n')

    output_file.write(f'\n')
    print(f'Program Finished Running The total number of expression that ran without issues: {total_conversions}')
    print(f'Number of errors: {total_errors}')

    end_time = time.time_ns()  # Measure end time
    # Calculate duration in nanoseconds
    duration_ns = end_time - start_time
    # Create a RunTimeMetric object and append it to the list
    runtime_metrics.append(RuntimeMetric(size=file_size, time_ns=duration_ns))

    for metric in runtime_metrics:
        print(f'Metrics size: {metric.get_size()}\t\tmetrics runtime: {metric.get_runtime()}')



def enhance_process_files(input_txt_file: TextIO, output_txt_file: TextIO) -> None:
    """
    Processes prefix expressions, converts them to infix and postfix, and writes to an output file. This function
    is the optional main function of the program, and it takes input and uses classes and functions
    in order to run the program as a whole.

    :param input_txt_file: Input file containing prefix expressions.
    :param output_txt_file: Output file to write converted expressions.
    """
    # Initialize empty list to store runtime metrics
    runtime_metrics = []
    start_time = 0

    # this variable will track how many conversions per file
    total_number_conversions = 0
    # counts number of error in the file
    total_number_errors = 0
    # Stores each line into next Line
    next_file_line = input_txt_file.readline()
    file_size = len(next_file_line)  # approved by Mr. Almes

    # Iterates through the input file to process all lines.
    # use  pathlib path object replaces the Os file pass path lib path library
    output_txt_file.write('PREFIX TO INFIX AND POSTFIX CONVERSION\n')
    output_txt_file.write('-----------------------------\n\n')
    # iterates through the file reading each line as long as there's character to read.
    while next_file_line is not None and next_file_line != "":
        start_time = time.time_ns()  # Measure start time
        try:

            # Validates the expression that is read by the program before moving on.
            is_it_valid = is_valid_prefix(next_file_line)
            # Creates an instance of the class InfixConverter
            infix_expression = InfixConverter(next_file_line)

            # Checks for valid prefix expressions.
            if is_it_valid:
                # Reverses the instance of the Infix expression inside the infix class
                infix_expression.reverse()
                # Convert the prefix expression to Infix
                infix = infix_expression.to_infix()
                # Convert to Postfix
                postfix_converter = PostfixConverter(next_file_line)
                postfix_converter.reverse()  # reverses the prefix expression
                postfix_string = postfix_converter.to_postfix()  # converts the prefix to postfix

                # Outputs to the file
                output_txt_file.write(f'This is the Original Prefix : {next_file_line} ')
                output_txt_file.write(f'This is the converted Infix Expression: {infix}')
                output_txt_file.write(f'\n')
                output_txt_file.write(f'This is the converted Postfix Expression: {postfix_string}')
                output_txt_file.write(f'\n')
                # Counts the number of lines or expression that were converted
                total_number_conversions += 1

        except ValueError as e:  # Calls any error that were raise by invalid prefix expressions
            output_txt_file.write(f'\n')
            total_number_errors += 1  # counts error
            print(f'Your prefix expression "{next_file_line} is invalid: {e}', file=sys.stderr)
            output_txt_file.write(f'Your prefix expression "{next_file_line} is invalid: {e}\n')

        except ErrorInvalidExpression as e:  # Calls ErrorInvalidExpression if prefix expression is invalid
            output_txt_file.write(f'\n')
            total_number_errors += 1  # counts error
            print(f'Your prefix expression "{next_file_line} is invalid: {e}', file=sys.stderr)
            output_txt_file.write(f'Your prefix expression "{next_file_line} is invalid: {e}\n')

        next_file_line = input_txt_file.readline()
        output_txt_file.write(f'\n')

    output_txt_file.write(f'\n')
    print(f'Program Finished Running The total number of expression that '
          f'ran without issues: {total_number_conversions}\n')
    print(f'Number of errors: {total_number_errors}\n')

    end_time = time.time_ns()  # Measure end time
    # Calculate duration in nanoseconds
    duration_ns = end_time - start_time
    # Create a RunTimeMetric object and append it to the list
    runtime_metrics.append(RuntimeMetric(size=file_size, time_ns=duration_ns))

    for metric in runtime_metrics:
        print(f'Metrics size: {metric.get_size()}\t\tmetrics runtime: {metric.get_runtime()}')
