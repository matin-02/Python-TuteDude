stud1 = {'maths':80.5, 'english':77.5, 'physics':77.5}
print(stud1)
print()
print(stud1['physics'])
print()
#print(stud1['chemistry'])

# get() :- is used fetch values if the key is not present in dict get not get the error we get none
print(stud1.get('physics'))
print(stud1.get('chemistry'))
print(stud1.get('chemistry', 70))

# Membership Operator :- in or
# the membership operator does not check for values it check for the keys
print('maths' in stud1)
print()

# update Method is used to update the dict with another dict or we can use to concatenate the dict
sem1 = {'maths':80.5, 'english':77.5}
sem2 = {'biology':80.5, 'physics':77.5}
sem1.update(sem2)
print(sem1)
print()

# when we update the dict if the value of another dict is present in the dict1 then the value at the key get updated
groceries1 = {'milk':100, 'bread' : 50, 'rice':90}
groceries2 = {'rice' : 110 , 'bread' : 60}
groceries1.update(groceries2)
print(groceries1)
print()

# pop() :- pop is used to delete the any key-value from the dict by giving the key
groceries1.pop('bread')
print(groceries1)
print()

# keys cannot be duplicate in the dict keys must be unique
groceries = {'milk':100, 'bread' : 50, 'rice':90, 'milk':65}
print(groceries)
print()