# Algos-HW-2
## Student Info
Name: Asha Miller 
UFID: 2619-5990

## Running Instructions
Requires Python 3.13 or higher

Input files can be generated via the terminal by going to the data directory '../Algos-HW-2/data' and running the
command 'python generator.py <k> <m>' where k is the cache capacity and m is the number of requests.

To run the main program, go to the src directory in the terminal '../Algos-HW-2/src' and run the command
'python Caching.py <k> <m>' where k & m correspond to an existing input file in the form of '"{k}_{m}.in"'.

Output will take the form of an .out file with a filename corresponding to the .in file that Caching.py used.
'"{k}_{m}.out"'

## Assumptions
The program was build with the assumption that the input file will be formatted as specificed on the assignment page
'''
k m 
r1 r2 r3 ...rm
'''
It is also assumed that the integer IDs are all positive and that all IDs are separated by whitespace

## Written Component
Answers to the written component are in a PDF in the repository titled "PA2_Written".
