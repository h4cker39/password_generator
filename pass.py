import argparse
import sys


def  lettersAndDigits():
    print( "letters And digits")

def  lettersDigitsAndCharacters():
     print("letters, digits and characters")

def  letters():
    print("only letters")

ap = argparse.ArgumentParser()
ap.add_argument("-d","--digit", required=False, help="-d for digits from 0-9")
ap.add_argument("-u","--unicode", required=False, help=" -u non alphabetical non digits")
ap.add_argument("-l","--letters", required=True, help="-l for only letters ")
ap.add_argument("-s","--size", required=True, help="-d for digits from 0-9")


args = ap.parse_args()
args2 = vars(ap.parse_args())
if(int(args.size) <= 6):
    print ("Size is required to be above 6 to be secure")
    exit
if(args.digit  and args.letters and args.unicode ):
    lettersDigitsAndCharacters()
elif(args.digit and args.letters):
    lettersAndDigits()
else:
    letters()
