# range() :-  built in function is used to generate sequence of integer in a given interval
# Syntax :-
# range(start , stop , step) stop is not include

for i in range(1,20,1):
    print(i)
print("-" * 100)

# want to generate even number from 1 to 20
for i in range(0,21,2):
    print(i, end     = " , ")
print()
print("-" * 100)

# want to generate even number from 1 to 20 in reverse
for j in range(20,0,-2):
    print(j, end = " , ")
print()
print("-" * 100)

# countdown from 10 to 1 (1 include)
for i in range(10,0,-1):
    print(i)
print("Happy New Year!!")
print("-" * 100)

# start value is 0 by default
for i in range(5):
    print(i)
print("-" * 100)

# range function with the list
groceries = ["salt" , "milk" , "bread" , "eggs"]
for item in groceries:
    print(item , end = " , ")
print()
print("-" * 100)

# using the len to find the index
for index in range(len(groceries)):
    print(index , end = " , ")
print()
print("-" * 100)

# printing the values with the index
prof = [9,12,15,7,10]
for index in range(len(prof)):
    q = index + 1
    print(f"profit for quarter {q} is {prof[index]}")
print("-" * 100)