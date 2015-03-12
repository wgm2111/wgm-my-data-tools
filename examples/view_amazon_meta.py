
# 
# me: Will Martin
# data: 3.12.2015
# license: BSD
# 

"""
Run this program to look ad the amazon-meta data interactively.
"""


# future
from __future__ import print_function, division

# standard
import os

# works on unix machines
FILENAME = os.path.abspath(r"../amazon-meta/amazon-meta.txt") 

# Parameters for the interactive prompt
PROMPT = "[amazon-meta] : "





# data printing routine
def print_till_blank(amfile):
    """
    Amazon data entry printer. 
      in: amazon-meta-file
      out: None
    """
    # print lines until a blank is found.
    while True:
        line = amfile.readline().strip()
        print(line)
        if line == "":
            break
    return None

# interactive data viewer
print("Running the interactive data viewer.\n", end='\n')


# open the amazon database 
with open(FILENAME, 'r') as amfile:

    # Print the header
    print_till_blank(amfile)
    print("\nKeep pressing enter to view data:")
    
    # start the propt
    while True:
        # Run the prompt 
        print(PROMPT, end="")
        ui = raw_input()
        if ui == "":
            print_till_blank(amfile)
        else:
            break
