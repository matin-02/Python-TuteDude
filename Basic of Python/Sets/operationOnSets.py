num = {1, 2, 3, 4, 5}

# Membership Operator :- in , not in
print(1 in num)
print(10 not in num)
print()
print(0 in num)
print(1 not in num)
print()

# concatenation :-
num2 = {6, 7, 8, 9, 10}
# print(num + num2) # are not allowed in set

# repetation are not allowed in set

# type conversion
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
s1 = set(t1)
print(s1)
print(type(s1))
print()

# sets are mutuable or immutable ?
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# add ():- add the elements in sets are index are not fixed
set1.add(11)
print(set1)
print()
# in set the when we add  the duplicate value we don't get the error but the value will get added in set
# as the set don't allows duplicate values
set1.add(10)
print(f"the duplicate value is not getting added : \n {set1}")
print()

# discard() :- is used to delete or remove the element from sets
# behaviour of the remove is it remove the element from the sets if the value if present in the sets
# throw the error if the value is not is present in sets
# discard() it will not throw the error the if the value is not present in the set
set1.discard(11)
print(f"after removing the element which is present in the sets : \n {set1}")
print()

set1.discard(12)
print(f"after removing the element which is not present in the set : \n{set1}")
print()


stud1 = {"English","Maths","Physics","Chemistry","CS"}
stud2 = {"English","Biology","Physics","Chemistry"}
stud3 = {"sanskrit" , "Maths" , "CS"}
print(stud1,type(stud1))
print(stud2,type(stud2))
print()

# common subject between stud1 and stud2 :-  we use intersection theory of maths on set
print(f"Common Subject between the students are using intersection : \n{stud1.intersection(stud2)}")
print(f"Common Subject between the students are using &  : \n{stud1 & stud2}")
print(f"Common Subject between the students are using intersection of Multipal sets : \n{stud1.intersection(stud2,stud3)}")
# this will provide the empty{} if the one of the set don't have common the elements
print()

# to find the all the subjects of the students :-  use the union operation
# we can use the union in the place of concatenation
print(f"All the Subjects of the Students using the union() : '\n{stud1.union(stud2,stud3)}")
print(f"All the Subjects of the Students using the | using Pipe  : '\n{stud1 | stud2 | stud3}")
print()
# finding the difference of the sets
days = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
weekends = {"Sat" , "Sun"}
# finding the elements which are Not in weekends
weekdays = days - weekends

print(f"the difference of the sets using - :-  \n{weekdays}")
print(f"the difference of the sets using difference() :-  \n{days.difference(weekends)}")
print()