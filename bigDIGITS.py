#!/usr/bin/env python3
# shebang for linux

#!/usr/local/bin/python3
# shebang for mac osx

#
# PROGRAM TITLE: bigDIGITS
# PROGRAM DESCRIPTION: prints ASCII art numerals representing numeric input
#

# import std lib
import sys

# import 3rd party lib

# import usr lib
import ASCIIdigits

# import debugger
import pdb

# global var

# start debugging
#pdb.set_trace()

#
# FUNCTION DESCRIPTION: main
#
# INPUTS: none
# OUTPUTS: none
#
def main():
    try:        
        NUMin = sys.argv[1];    #get first command line argument
        row = 0;
    
        while row < 3:
            line = "";          #reset line
            column = 0;
            
            while column < len(NUMin):      #for each digit in integer
                digit = int( NUMin[column] );
                BIGdigit = ASCIIdigits.digit[digit];
                line += BIGdigit[row] + " ";
                column += 1;
                
            print(line);
            row += 1;
            
    except IndexError as e1:
        print("usage: bigDIGITS.py integer");
    except ValueError as e2:
        print(e2, "in", NUMin);
    return;

# script autorun
if __name__ == "__main__":
    main();
