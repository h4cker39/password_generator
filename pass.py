import argparse
import random
#Passsword Generator

letters="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
digits="0123456789"
characters="$%&*()!@#/;':"
ss = [letters,digits,characters]
def  lettersAndDigits(digit):
    password = ""
    #randomly select which one will go first 
    for i in range(int(digit)+1):
           index,number = random.choice(list(enumerate(ss)))
           r = ss[index]
           index,number = random.choice(list(enumerate(r)))
           sr = r[index]
           password += sr
    return password

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
    print(lettersAndDigits(args.size))
else:
    letters()
