#!/usr/bin/env python3
"""
Cookie Clicker Alpha problem
for Google Code Jam 2014
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/dashboard?c=2974486

Author: 
  Tasos Sangiotis
  (tsagi)

Language:
  Python 3(.4)

Date:
  April, 2015

Usage:
  python3 main.py input_file
"""


import sys
import argparse
# modules I've written:
from helpful import *


_program_description = \
'''
Introduction

Cookie Clicker is a Javascript game by Orteil, where players click on a picture 
of a giant cookie. Clicking on the giant cookie gives them cookies. 
They can spend those cookies to buy buildings. 
Those buildings help them get even more cookies. 
Like this problem, the game is very cookie-focused. 
This problem has a similar idea, but it does not assume you have played Cookie Clicker. 
Please don't go play it now: it might be a long time before you come back.

Problem

In this problem, you start with 0 cookies. 
You gain cookies at a rate of 2 cookies per second, by clicking on a giant cookie. 
Any time you have at least C cookies, you can buy a cookie farm. Every time you 
buy a cookie farm, it costs you C cookies and gives you an extra F cookies per second.

Once you have X cookies that you haven't spent on farms, you win! 
Figure out how long it will take you to win if you use the best possible strategy.

Example

Suppose C=500.0, F=4.0 and X=2000.0. Here's how the best possible strategy plays out:

You start with 0 cookies, but producing 2 cookies per second.
After 250 seconds, you will have C=500 cookies and can buy a farm that 
produces F=4 cookies per second.
After buying the farm, you have 0 cookies, and your total cookie production 
is 6 cookies per second.
The next farm will cost 500 cookies, which you can buy after 
about 83.3333333 seconds.
After buying your second farm, you have 0 cookies, and your total cookie 
production is 10 cookies per second.
Another farm will cost 500 cookies, which you can buy after 50 seconds.
After buying your third farm, you have 0 cookies, and your total cookie 
production is 14 cookies per second.
Another farm would cost 500 cookies, but it actually makes sense not to buy it: 
instead you can just wait until you have X=2000 cookies, which takes about 142.8571429 seconds.
Total time: 250 + 83.3333333 + 50 + 142.8571429 = 526.1904762 seconds.
Notice that you get cookies continuously: 
so 0.1 seconds after the game starts you'll have 0.2 cookies, and π seconds after 
the game starts you'll have 2π cookies.
'''


_input_file_description = \
'''
Input

The first line of the input gives the number of test cases, 
T. T lines follow. Each line contains three space-separated real-valued numbers: 
C, F and X, whose meanings are described earlier in the problem statement.

C, F and X will each consist of at least 1 digit followed by 1 decimal point 
followed by from 1 to 5 digits. There will be no leading zeroes.

Output

For each test case, output one line containing "Case #x: y", 
where x is the test case number (starting from 1) and y is the minimum number 
of seconds it takes before you can have X delicious cookies.

We recommend outputting y to 7 decimal places, but it is not required. 
y will be considered correct if it is close enough to the correct number: 
within an absolute or relative error of 10-6. See the FAQ for an explanation of 
what that means, and what formats of real numbers we accept.


Input:
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

Output:
Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762
'''


def parse_args():
    """
    Parse the command line arguments and return them in a namespace.
    """
    parser = argparse.ArgumentParser(description=_program_description)
    parser.add_argument('input_file', help=_input_file_description)
    #parser.add_argument('-v', '--verbose', action='store_true', 
    #                    default=False, help='show progress')
    args = parser.parse_args()
    return args


def main(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        num = read_int(file)
        for i in range(0,num):
          seconds = 0.0
          production = 2.0
          case = read_list_of_float(file)
          c = case[0]
          f = case[1]
          x = case[2]
          if (c >= x):
            print("Case #%d: %.7f" % (i+1, x/production))
          else:
            seconds = 0.0

            while((x/production) > (c/production) + (x/(production + f))):
              seconds += c/production
              production += f
            print ("Case #%d: %.7f" % (i+1, seconds+(x/production)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
