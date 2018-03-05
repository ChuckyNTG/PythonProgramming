import re

passwords = raw_input("Passwords:")
pstring = passwords.split(",")
for p in pstring:
    if re.search('^.*(?=.{6,12})(?=.*\d)(?=.*[a-zA-Z])(?=.*[$#@]).*$',p):
        print p


