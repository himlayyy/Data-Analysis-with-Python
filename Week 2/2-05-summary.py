#!usr/bin/env python3
"""
Part 1.

Create a function called summary that gets a filename as a parameter. The input file should contain a floating point
number on each line of the file. Make your function read these numbers and then return a triple containing the sum,
average, and standard deviation of these numbers for the file

The main function should call the function summary for each filename in the list sys.argv[1:] of command line
parameters. (Skip sys.argv[0] since it contains the name of the current program.)

Example of usage from the command line: python3 src/summary.py src/example.txt src/example2.txt

Print floating point numbers using six decimals precision. The output should look like this:

File: src/example.txt Sum: 51.400000 Average: 10.280000 Stddev: 8.904606
File: src/example2.txt Sum: 5446.200000 Average: 1815.400000 S
"""
import sys
import statistics


def summary(filename):
    with open(filename) as f:
        numbers = []
        for line in f:
            try:
                line = float(line)
                numbers.append(line)
            except ValueError:
                print(f"{line} not an int")
    mean = float(sum(numbers) / len(numbers))
    stdv = float(statistics.stdev(numbers))
    sums = float(sum(numbers))
    return sums, mean, stdv


def main(args):
    pass
    for arg in sys.argv[1:]:
        results = summary(arg)
        print(f"File: {arg} Sum: {results[0]:6f} Average: {results[1]:6f} Stddev: {results[2]:6f} ")


if __name__ == "__main__":
    main(sys.argv)
