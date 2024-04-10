import argparse
import random
#Passsword Generator

letters="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
digits="0123456789"
characters="$%&*()!@#/;':"
ss = [letters,digits,characters]
s2 = [letters,digits]
s1 = [letters]
def  lettersDigitsAndCharacters(digit):
    password = ""
    #randomly select which one will go first 
    for i in range(int(digit)+1):
           index,number = random.choice(list(enumerate(ss)))
           r = ss[index]
           index,number = random.choice(list(enumerate(r)))
           sr = r[index]
           password += sr
    return password

def  lettersAndDigits(digit):
    password = ""
    #randomly select which one will go first 
    for i in range(int(digit)+1):
           index,number = random.choice(list(enumerate(s2)))
           r = s2[index]
           index,number = random.choice(list(enumerate(r)))
           sr = r[index]
           password += sr
    return password


def letters_d(digit):
    password = ""
    for i in range(int(digit)+1):
          index,number = random.choice(list(enumerate(s1)))
          rs = s2[index]
          index,number = random.choice(list(enumerate(rs)))
          sr = rs[index]
          password += sr
    return password

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
    print(lettersDigitsAndCharacters(args.size))
elif(args.digit and args.letters):
    print(lettersAndDigits(args.size))
elif(args.letters):
    print(letters_d(args.size))
