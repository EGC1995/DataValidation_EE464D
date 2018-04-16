import pandas as pd
import sys
import matplotlib.pyplot as plt


'''
This script serves the purpose of being able to plug in a json file and plot it with the choice of either
a histogram/bar chart or line chart, depending on what the user wants to see, against time. This will help
give a better sense of data validation by inspection to see if two charts match rather than having to do the
meticulous task of comparing individual points one by one.
'''

# grab command line arguments
dataFile = sys.argv[1]
chartType = sys.argv[2]

# plotting logic below
