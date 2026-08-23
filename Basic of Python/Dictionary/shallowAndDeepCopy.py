# the shallow and deep Copy applyed on mutuable data types
# Shallow Copy
import copy
li = [1,2,3,[10,20,30] , 'hello']
print(li)

l1 = copy.copy(li)
print(l1)

#print(id(li))
#print(id(l1))
#print()

li[0] = 100
li[3][0] = 50
print(f"li --> {li}" , id(li))
print(f"l1 --> {l1}" , id(l1))
print()

# deep Copy : does not make the change effect to the copied list or dict

l2 = copy.deepcopy(li)
li[0] = 20
li[3][0] = 70
print(f"li --> {li}" , id(li))
print(f"l1 --> {l2}" , id(l2))
print()

d1 = {"id":1, "name":"john", "age":25, "marks" :{'eng' : 89.5,'maths' : 88.5, 'phy' : 65.4}}
d2 = copy.deepcopy(d1)
d1["name"] = "bob"
d1['marks']['maths'] = 90.2
print(f"d1 --> {d1}" , id(d1))
print(f"d1 --> {d2}" , id(d2))
