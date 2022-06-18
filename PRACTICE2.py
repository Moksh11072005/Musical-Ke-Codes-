import string
str1="Hello @#$$%world#@$"
str2=""
symbols = string.punctuation
for j in range (len(str1)):
    for i in str1:
        if i in symbols :
            pass
        else :
            print(str1[::-1])