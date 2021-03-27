#This script takes in command line arguments and then spits them out to the user!

#Import the sys command
import sys

# Determine the number of
# arguments
num_args = len(sys.argv) - 1

print("There are " + str(num_args) + " commandline arguments.")

if(num_args > 0):
    counter = 0
    for arg in sys.argv:
        if counter == 0:
            pass
        else:
            print("Argument " + str(counter) + " is " + arg)
        counter+=1
