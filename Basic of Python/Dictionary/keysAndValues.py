#d1 = {[1,2,3] : 9, [1,2,1] : 4}
d1 = {"one":1, "two":2, "three":3}
print(d1)

# not allowed :- keys cannot be list, set, dict => mutuable datatypes
# allowed :- keys can be str, int, float, boolean, tuple => Immutable datatypes
# key of a dictionary can only be immutuable datatypes!!


# values can be any datatypes

stu1 = {"id":1, "name":"john", "age":25, "marks" :[89.5,88.5,65.4]}
print(stu1)
print(stu1['marks'][0])
print()

stu2 = {"id":1, "name":"john", "age":25, "marks" :{'eng' : 89.5,'maths' : 88.5, 'phy' : 65.4}}
print(stu2)
print(stu2['marks']['eng'])
print()

#fetch all the keys of the dict
# keys()
print(stu2.keys(), type(stu2.keys()))
print()

# fetching all the values of the dict
# values
print(stu2.values(), type(stu2.values()))
print()

# items():- it gives the key values pairs in tuples manner
print(stu2.items(), type(stu2.items()))
print()