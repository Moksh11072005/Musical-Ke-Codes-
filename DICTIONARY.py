# DICTIONARY
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
print(dict1)
# ACCESSING THE ELEMENTS OF THE DICTIONARY
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
print(dict1['Mohan'])
print(dict1['Ram'])
print(dict1['Suhel'])
print(dict1['Sangeeta'])
# LOOPS
# for loop
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
for i in dict1:
    print(i, ":", dict1[i])

#
for key, value in dict1.items():
    print(key, ':', value)
# BUILT-IN FUNCTIONS
# 1 len()
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
print(len(dict1))
# 2 dict()---> creates a dictionary from a list of key and values
list = [('Mohan', 95), ('Ram', 89), ('Suhel', 92), ('Sangeeta', 85)]
print(dict(list))
# 3 keys()---> returns the keys in dictionary
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
print(dict1.keys())
# 4 values()---> returns the values in dictionary
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
print(dict1.values())
# 5 items()---> basically converts the dictionary into a tuple
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
print(dict1.items())
# 6 get()---> Returns the value corresponding to the key passed as the argument .If the key is not present in the dictionary it will return None
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
print(dict1.get('Sangeeta'))
# 7 update()--->appends the key-value pair in the end of the dictionary
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
dict2 = {'M': 5,
         'R': 9
         }
dict1.update(dict2)
print(dict1)
# 8 del()---> deletes the item of the respective key
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
del dict1['Ram']
print(dict1)
# 9 clear()---> deletes all the items of the dictionary
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
dict1.clear()
print(dict1)
# 10 dict.fromkeys()---> Creates a new Dictionary from a sequence containing all  the Keys and a common Value 
dict1=dict.fromkeys((1,2,3,4,5,6,7,8,9),100)
print(dict1)
# 11 setdefault()---> Inserts a new Key:Value Pair only if the Key doesn't already exist, else it returns the current Value of the Key 
# Case 1--->When the new entered key doesn't exist 
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
dict1.setdefault('Moksh',85)
print(dict1)
#Case 2 ---> When the Key already exist
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
dict1.setdefault("Mohan",90)
print(dict1)
# 12 copy()---> Creates a Copy the Dictionary
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
dict2=dict1.copy()         
print(dict2)
#13 pop()--->deletes the key:value pair from the dictionary via key entered
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
dict1.pop('Mohan')         
print(dict1)
# 14 popitem()---> prints and deletes the last element of the dictionary 
#Case 1---> when synatx is---> print(<Dictname>.popitem())
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
print(dict1.popitem())
#Case 2 ---> when synatx is --->
# <DictName>.popitem()
# print(DictName)
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
dict1.popitem()
print(dict1)
#15 sorted--->prints the sorted keys in the form of a list 
#Ascending--->
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
list1=sorted(dict1)
print(list1)
# Case 2 ---> Descending 
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
list1=sorted(dict1,reverse=True)
print(list1)
#16 sum()--->adds the keys of the dictionary 
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
# print(sum(dict1))   This will throw an error  as the key sare string that cannot be added 
dict2 = {1: 95,  
         2: 89,
         3: 92,
         4: 85
         }
print(sum(dict2))          
# 17 min() and max()--->returns the min or the max among the keys of the dictionary
dict1 = {'Mohan': 95,  # marks of 4 students
         'Ram': 89,
         'Suhel': 92,
         'Sangeeta': 85
         }
print(max(dict1))
print(min(dict1))
# QUESTIONS
# 1 Write a program to count the number of times a character appears in a given string.
st = 'mokshsharma'
dict = {}  # creates an empty dict
for character in st:
    if character in dict:  # if next character is already in the dict
        dict[character] += 1
    else:
        dict[character] = 1  # if character appears for the first time
for key in dict:
    print(key, ':', dict[key])
# 2 Write a function to convert a number entered number in to words


def convert(num):
    # numberNames is a dictionary of digits and corresponding number
    # names
    numberNames = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
                   5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}

    result = ''
    for ch in num:
        key = int(ch)  # converts character to integer
        value = numberNames[key]
        result = result + ' ' + value
        return result


num = input("Enter any number: ")  # number is stored as string
result = convert(num)
print("The number is:", num)
print("The numberName is:", result)

