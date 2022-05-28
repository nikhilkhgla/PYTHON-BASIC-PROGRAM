#  How to create a random string in python?
import random
import string
alphabets = string.ascii_lowercase + string.digits
string = ""
length=10
for number in range(length):
    string += random.choice(alphabets)
print(string)
