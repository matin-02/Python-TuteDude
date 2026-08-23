# sets are mutuable
s1 = {1,2,3,4,5}
s1.add(6)
print(s1,type(s1))
print()

# frozen sets are immutable sets
fs1 = frozenset({1,2,3})
print(fs1,type(fs1))

# add and remove is not allowed but the union,difference and the intersection are allowed in the sets
fs2 = frozenset({4,5,6,1,2})
print(fs2,type(fs2))
print()

print("the union of the frozensets is : \n",fs1 | fs2)
print()
print("the intersection of the frozensets is : \n", fs1 & fs2)
print()
print("the difference of the frozensets is : \n", fs1 - fs2)
