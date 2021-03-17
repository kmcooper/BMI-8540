# Name:         Kate Cooper
# Class:        BMI 8540, Spring 2021
# Assignment #: n/a, Hello World!
# Due date:     No submission
#
# Honor Pledge: On my honor as a student of the University of Nebraska at
#               Omaha, I have neither given nor received unauthorized help on
#               this programming assignment.
#
# NAME: Kate Cooper
# NUID: 123
# EMAIL: someemail@someemailservice.com
#
# Partners: NONE
#
# This program prints the classic "Hello world!" in the Python language.
# It does not take any input, but the output should print "Hello World!" 
# to standard out.

# A class is defined to provide organization and grouping to functions and data
# It requires no closure (no closed brackets or parentheses)
# Using a class is not required for your program to work 
# but is an example of good practice in Python programming.

class helloWorld:

    # A def main(): statement allows the user to import code into other Python
    # scripts later on.
    # It requires a closure statement (see below).
    # Using def main is not required for your program to work but 
    # is an example of good practice in Python programming.
    # In BIOI 3500, it is expected that you use def main().
    def main():
        print("Hello world!")   # Prints Hello World! to standard out            

    if __name__ == '__main__':
        main()
