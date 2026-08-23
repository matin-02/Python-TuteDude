# sets are non-sequential collection of items
# comma seperated elements enclosed within {}
# indexing are not allowed and slicing are also not allowed as the sets are non-sequential collection of items
# different between list,tuple and set is that the set doesn't allow the duplicate values
# Python sets are similar to maths sets

s = {1,"python",2,"java"}
print(s)
print(type(s))
print()

# Length of the set
print(len(s))
print()

# duplicate are not allowed in set if set contain the duplicates than  it print only the 1st occurrance of the elements
s1 = {10,20,10,10,20}
print(s1)