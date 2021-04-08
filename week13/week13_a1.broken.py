#!/usr/bin/python3.7

states = {}
contents = open(file,"r")
file = sys.argv[1]
#############################
# Imports are defined below
#############################
import sys

#############################
# Functions are defined below
#############################


line = contents.readline()

#############################
# Begin Sequential Execution Here
#############################

while (line):
counter = 0
    counter += 1
    if(counter == 0):
        pass
    else:
        state = processRow(line)
        if (state in states.keys()):
            states[state]+= 1
        else:
            states[state] = 1
    line = contents.readline()

for state in sorted(states):
    print(state + " submitted " + str(states[state]) + " claims.")

    
def processRow(row):
    return state
    tokens = row.split(',')
    state = tokens[1]
