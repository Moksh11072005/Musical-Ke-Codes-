# TUPLES
t2 = ()  # Empty Tuple
tuple1 = ("a", "b", "c", "d")
print(tuple1)
# tuples are immutable
t1 = (1,)  # to make a tuple with a single element use comma after the element
# operations
# 1 concatenation
tuple1 = ("a", "b", "c", "d")
tuple2 = ("b", "c", "d")
print(tuple1+tuple2)
# 2 repetition
tuple1 = ("a", "b", "c", "d")
print(tuple1*3)
# 3 membership
tuple1 = ("a", "b", "c", "d")
print("a" in tuple1)
# 4 slicing
tuple1 = ("a", "b", "c", "d")
print(tuple1[0:2])
# TRAVERSING A TUPLE
tuple1 = ("a", "b", "c", "d")
# for loop
for i in tuple1:
    print(i)
# while loop
i = 0
while i < len(tuple1):
    print(tuple1[i])
    i += 1
# range and len function
for i in range(len(tuple1)):
    print(tuple1[i])
# BUILT IN FUNCTIONS
# 1 len()
tuple1 = ("a", "b", "c", "d")
print(len(tuple1))
# 2 max()--->returns the element with max value
tuple1 = ("a", "b", "c", "d")
print(max(tuple1))
# 3 min()--->returns the element with min value
tuple1 = ("a", "b", "c", "d")
print(min(tuple1))
# 4 index()---> returns the index of the selected element
tuple1 = ("a", "b", "c", "d")
print(tuple1.index("a"))
# 5 sum()---> returns the sum of the elements of the tuple (only for integers)
tuple1 = (3, 2, 6, 4, 6)
print(sum(tuple1))
# 6 count()--->returns the number of the selected element repeated in a tuple
tuple1 = ("a", "b", "c", "a", "d")
print(tuple1.count("a"))
# 7 sorted()---> returns the sorted tuple
tuple1 = ("a", "b", "c", "d", "a")
print(sorted(tuple1))
# 8 tuple()---> creates a tuple
print(tuple('abc'))
# to make a single element tuple put , at the end of the element
# for example t=(170,)
t = 5, 6, 4, 2, 5, 7, 8, 5, 3
print(t)
# NOTE if the range is not completely given like [:] the complete tuple will be printed
# reverse
tuple1 = (1, 2, 34, 5)
print(tuple1[::-1])
