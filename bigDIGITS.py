#!/usr/local/bin/python3
#shebang for mac osx
#!/usr/bin/env python3
#shebang for linux

#import std lib
import sys
#import 3rd party lib
#import usr lib
import ASCIIdigits

#global var

def main():
    try:
        NUMin = sys.argv[1];   #get first command line argument

        for i in NUMin:
            type(i);
            num = int(NUMin[i]);
            print(ASCIIdigits.digit[num]);

    except IndexError as e1:
        print("usage: bigDIGITS.py int");
    except ValueError as e2:
        print(e2, "in", digits);
    return;

if __name__ == "__main__":
    main();
