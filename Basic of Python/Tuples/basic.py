# Tuples :- A tuple in Python is a built-in data collection type used to
# store multiple items in a single variable.
# The defining characteristics of a tuple are that it is ordered,
# immutable (cannot be changed after creation), and allows duplicate values.

# we use the () to create the tuple or we use the construtor tuple()

a = tuple((1,2,3,4,5))
print(f"tuple using the constructor {type(a)}")
print()
b = (1,2,3,4,5,6,7,8,9,0)
print(f"Tuple using the () {type(b)}")

# use to len() to find the length of tuple

print(f"the lenght of the tupleb : {len(b)}")
print()

# Indexing in tuple
print(b[1])
print(b[-2])
print()

# when we assing the multiple values to the singal variable it is always a tuple
# ex :-
c = 10,20,30,40,50
print(type(c))