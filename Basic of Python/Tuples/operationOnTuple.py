# concatenation of tuple :- we can concatenate the  tuples using "+"
stud1 = (1001,"Jonh")
stud2 = (78.5,86.3,95.4,45)
stud = stud1 + stud2
print(stud)
print()

# repetation of tuple :- we use astrick to repeate the tuple values

t1 = ("class 5", 5000)
print(t1 * 5)
print()

# membership operator on tuple :- in and not in
print(1001 in stud1)
print(87 in stud2)
print()
print(99 not in stud2)
print(1001 not in stud1)
print()

# count() in tuple :- is used to count the specific element in the tuple
t2 = (11,2,2,2,3,4,5,6,6,6,6,7,7,7,7,7,7,)
print(t2.count(7))
print()

# index() :- is used to get the index 1st occurrance of specific value in the tuple
print(t2.index(3))
print()

# min() :- is used to find the minimum value in the tuple
print(min(t2))
print()

#max() :- is used to find the maximum value from the tuple
print(max(t2))
print()