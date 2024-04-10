# password_generator



Easy to use password generator just install python3 and below dependencies your ready to go

```
pip3 install argparse
```

```
pip3 install requirements.txt
```

# Usage
```
usage: pass.py [-h] [-d DIGIT] [-u UNICODE] -l LETTERS -s SIZE

optional arguments:
  -h, --help            show this help message and exit
  -d DIGIT, --digit DIGIT
                        -d for digits from 0-9
  -u UNICODE, --unicode UNICODE
                        -u non alphabetical non digits
  -l LETTERS, --letters LETTERS
                        -l for only letters
  -s SIZE, --size SIZE  -d for digits from 0-9
```


#Example:
Say i want to create a password with 9 characters with letters digits and non-alphabetical characters like %$# the command:

```
python3 pass.py -s 9 -d 1 -u 1 -l 1
```

-s 9 = Size nine characters
-d 1 = digits 0-9 true which stands for true=1
-l 1 = letters A-Z a-z which stands for true=1
-u 1 = Non alphabetical characters which stands for true=1

Output:
```
E$2h6$/2/E
```

#Example 2:
Say i want to create a password with 5 characters with letters and digits only:

```
python3 pass.py -s 5 -d 1 -l 1
```

-s 9 = Size five characters
-d 1 = digits 0-9 true which stands for true=1
-l 1 = letters A-Z a-z which stands for true=1

Output:

```
Size is required to be above 6 to be secure
3518E4
```

