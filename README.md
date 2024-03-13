# Lab1
## About The Project

This Lab1 is the result of the directions of the first Lab for Data Structures class. This Lab's 
purpose is to convert prefix expression into postfix expression. The program has some error handling 
like ValueError and the custom error ErrorInvalidExpression that inherits from the Exception class. 
see below for examples in how to set up your IDE and how to run the program in the command line.


## Running Lab 1

> NOTE: Your IDE may want to run this Lab as a script make sure you run it as a module. 

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m Lab1 -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m Lab1 <some_input_file> <some_output_file> postfix` 
   a. IE: `python -m Lab1 resources/input/in.txt output.txt postfix`

> NOTE:  For the enhance part of the Project run the program as below:

1. Follow steps 1 and two if you have not done so.
2. Run the program as a module: `python -m Lab1 -h`. This will print the help message.
3. Run the program as a module (with real inputs): `python -m Lab1 <some_input_file> <some_output_file> enhanced` 
   a. IE: `python -m Lab1 resources/input/in.txt output.txt enhanced`

Output will be written to the specified output file after processing the input file. The Default location were the 
output file will be might be different on your computer. I have set the output file to be located in the resources/input.

### Lab 1 Usage:

```commandline
usage: python -m [-h] in_file out_file {postfix,enhanced}

positional arguments:
  in_file             Input File Pathname
  out_file            Output File Pathname
  {postfix,enhanced}  Run enhanced or not

options:
  -h, --help          show this help message and exit
```

## Example

A code that runs well and comes back with some errors depending on the input will return the following
```
python.exe -m Lab1 in.txt out.txt postfix 
Drive:\Users\some_user\PycharmProjects\Lab1\resources\input\in.txt
Program Finished Running The total number of expression that ran without issues: 6
Number of errors: 1
Metrics size: 6		metrics runtime: 1040500
Your prefix expression "++ABC++DE
 is invalid: This is an incorrect Prefix Expression

Process finished with exit code 0
```
```
python.exe -m Lab1 in.txt out.txt postfix 
Drive:\Users\some_user\PycharmProjects\Lab1\resources\input\in.txt
Program Finished Running The total number of expression that ran without issues: 1
Number of errors: 2
Metrics size: 15		metrics runtime: 0
Your prefix expression "+ C * D - E / F 
 is invalid: The total number of operators should be one less than the number of operands: + C * D - E / F 

Your prefix expression "- G / H + I * J is invalid: The total number of operators should be one less than the number of operands: - G / H + I * J

Process finished with exit code 0
```
```
Drive:\Users\some_user\PycharmProjects\Lab1\.venv\Scripts\python.exe -m Lab1 in.txt out.txt enhanced
Drive:\Users\some_user\PycharmProjects\Lab1\resources\input\in.txt 
Program Finished Running The total number of expression that ran without issues: 1

Number of errors: 2

Metrics size: 15		metrics runtime: 0
Your prefix expression "+ C * D - E / F 
 is invalid: The total number of operators should be one less than the number of operands: + C * D - E / F 

Your prefix expression "- G / H + I * J is invalid: The total number of operators should be one less than the number of operands: - G / H + I * J

Process finished with exit code 0
```

### Project Layout

 Here is my 605.202.Lab1 example package explained.

* [Lab1/](.): The parent or "root" folder containing all the below files. 
    * [README.md](README.md):
      This file which explains how the program runs and any solutions should the program no run properly
    * [Lab1](Lab1): 
      This is a *module* in the *package*. were all the source code will be store.
      * [`__init__.py`](Lab1/__init__.py) 
        This is a very important file and is mostly blank The [__ini__.py] file, essentially, tells the IDE this folder
        within Lab1 makes Lab1 a package. In this program it will be used to facilitate access to 
        the process_files function or the enhanced_process_files function for other scripts.
      * [`__main__.py`](Lab1/__main__.py) 
        This file is the entrypoint to my program when ran as a program. It will just handle command line 
        arguments, similar to Java and C's main() functions. As well a call to the main function that will
        process_files(). Please note Enhancement Section. quick snipped. The enhancement I have chosen modifies the
        original process_files function to convert the prefix expression not only to postfix, but also converts it to
        infix and displays them into the output file.
      * `*.py` 
        These are python scripts that do the actual work. But the main function that process all the classes and methods
        through the different files will be process_files. which will be run in the [__main__.py]

### Python Basic Lab1 as requested by Lab1_project1

The Basic choice for this Lab1 will work as follows. You should be able to run the basic Lab1 program without 
problems giving you the basic information that was asked to us in the Lab1 project1, so the basic program will return 
an output file with the original prefix expression and the converted postfix expression, if there were any error
the error will show at the specific line in the order they were process inside in.txt file and will be outputted 
respectably in that order in the output file.



### Python Enhancement Lab1 By Albert Rojas De Jesus

The Enhancement will work as explained in "USAGE" .  if you run it the program will call the second function 
"enhance_process_files" this will override the original output file and create a new output file where the file 
is going to have more information about the processed prefix expression. The output file will display, 
the original prefix expression follow by the enhancement as shown below.

```
PREFIX TO INFIX AND POSTFIX CONVERSION
-----------------------------

This is the Original Prefix : + a b
This is the converted Infix Expression: (a+b)
This is the converted Postfix Expression: ab+
```



## Acknowledgements

* [`stacker.py`](Lab1/stacker.py) 
* [`runtime_metric`](Lab1/runtime_metric.py)
* [`Lab1.py`](Lab1/Lab1.py)

Credit must be given to this course Data Structures at Johns Hopkins EN.605.202.81.SP24 for the bases of the 
code listed below:
stacker class, runtime_metrics class , and process_files methods inside the [Lab1/Lab1.py].
although some of these code has been modified in order to adjust to the needs of my program they
were a great resource to use as the basis of my program. 

