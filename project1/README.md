This program uses a divide and conquer algorithm to calculate the convex hull of a scatter plot then displays the scatter plot to the user.

Usage
Note: python represents your python 3 executable in path. This could be python, python3, or what ever the python.exe has been renamed to.

1. This execution assumes the scatter plot input file is name "input.csv".
python main.py

2. This execution takes the filename in as a parameter.
python main.py [filename]

Special considerations:
1. Currently, this does not account for multiple vertical points. It is assumed that the construction of a line from two points will always yield a slope that is not infinite.

