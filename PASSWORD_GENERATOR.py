import random
import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
# print(symbols)
list1 = list(lowercase)+list(uppercase)+list(digits)+list(symbols)
list1.sort()
# print(list1)
a = []
plen = int(input("Enter Your Password length\n>>>"))
for i in range(plen):
    p = random.choice(list1)
    a.append(p)
print("".join(a))

