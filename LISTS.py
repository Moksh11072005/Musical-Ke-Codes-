# LIST
list1 = ["a", "b", "c", "d"]
for i in (list1):
    print(i)
# mutability of a list
list1 = ["a", "b", "c", "d"]
list1[0] = "b"
print(list1)
# operations===>
# concatenation
list1 = ["a", "b", "c", "d"]
list2 = ["e", "f", "g", "h"]
print(list1+list2)
# repetition
list1 = ["a"]
print(list1*4)
# membership
list1 = ["a", "b", "c", "d"]
print("b" in list1)
print("e" in list1)
# slicing
list1 = ["a", "b", "c", "d"]
print(list1[0:2])
# TRAVERSING A LIST(Accessing the elements of the list)
list1 = ["a", "b", "c", "d"]
# for loop
for i in list1:
    print(i)
# while loop
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
# range and len function
for i in range(len(list1)):
    print(list1[i])
# BUILT-IN FUNCTIONS
# 1 len()
list1 = ["a", "b", "c", "d"]
print(len(list1))
# 2 list()---> creates an empty list
list1 = ["a", "b", "c", "d"]
list2 = list()
print(list2)
# 3 list(strl)--->converts each character of a string in to a list
str1 = 'aeiou'
list3 = list(str1)
print(list3)
# 4 append()--->adds characters at the end of a list
list1 = ["a", "b", "c", "d"]
list1.append('e')
print(list1)
# 5 extend()---> basically adds two lists
list1 = ["a", "b", "c", "d"]
list1.extend(list3)
print(list1)
# 6 insert()---> inserts an element at a particular index
list1 = ["a", "b", "c", "d"]
list1.insert(2, 'x')
print(list1)
# 7 count()--->counts the number of times a character is repeated
list1 = ["a", "b", "c", "d"]
print(list1.count('a'))
# 8 index()---> prints the index of the selected character
list1 = ["a", "b", "c", "d"]
print(list1.index('a'))
# 9 remove()--->removes the selected element
list1 = ["a", "b", "c", "d"]
list1.remove('a')
print(list1)
# 10 reverse()
list1 = ["a", "b", "c", "d"]
list1.reverse()
print(list1)
# 11 sort()
# 11.1---> sorting in ascending order
list1 = ["e", "b", "c", "d"]
list1.sort()
print(list1)
# 11.2 sorting in descending order
list1 = ["e", "b", "c", "d"]
list1.sort(reverse=True)
print(list1)
# 12 sorted()--->creates a new list from the selected list arranged in sorted order
list1 = ["e", "b", "c", "d"]
list4 = sorted(list1)
print(list4)
# 13 min()--->Returns minimum or smallest element of the list
#   max()--->Returns maximum or largest element of the list
#   sum()--->Returns sum of the elements of the list
list1 = [34, 12, 63, 39, 92, 44]
print(min(list1))
print(max(list1))
print(sum(list1))
# 14 pop()--->removes the element via index input from the user
list1 = [3, 6, 5, 3, 6, 5, 3, 6, 5, 4, 4, 4, 4, 4]
list1.pop(6)
print(list1)
# 15 del()---> deletes with an index or range
list1 = [34, 12, 63, 39, 92, 44]
del list1[0:3]
print(list1)
# 16 copy()---> copies the list
list1 = [34, 12, 63, 39, 92, 44]
list0 = list1.copy()
print(list0)
# 17 join()--->joins the elements of the list with string
my_list = ["Hello", "Python"]
print("-".join(my_list))
