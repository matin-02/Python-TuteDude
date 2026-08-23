# append() :- add an item at the end of the list
li = [1,2,3,4,5,6,7]
li.append(8)
print(f"list the append method ,\nafter append the item at the end of the list : {li}")
print(" ")

# insert() :- add the element at the specific index
# syntax :- li.insert(index,item)
li.insert(0,0)
print(f"list the insert method ,\nafter insert the item at the specific index of the list : {li}")
print(" ")

# extend() :- extend also add the element at the end of the list,
# by using append we can add only one element at the end of the list,
# but with the help of extend() we can add the multiple values
# syntax: - li.extend([item1,item2,item3])
# must be in list otherwise throw error ex:- li.extend(item1,item2,item3) not allowed throws error
li.extend([9,10,11])
print(f"list the extend method ,\nafter extend the list : {li}")
print(" ")

# remove() :- remove the specific element form the list
# throws the error if the item is not present in list , element is not present in list
# the 1st occurrence of repeated item get removed
li.remove(0)
print(f"list the remove method ,\nafter removing the specific item from  the list : {li}")
print(" ")

# pop() :- it delete the element by index no.
# we can use the negative indexing to delete the element from the last
li.pop(1)
print(f"list the pop method ,\nafter pop from the specific index from the list : {li}")
print(" ")

li.pop(-1)
print(f"list the pop method ,\nafter pop with negative indexing from the list : {li}")

# reverse() :-it used to reverse the list
days_of_week = ["mon","tues","wed","thu","fri","sat","sun"]
days_of_week.reverse()
print(f"list the reverse method ,\nafter reversing the list : {days_of_week}")
print(" ")

# sort() :- it sort the list in order by deafult it sort the list in ASC order
l = [1,4,3,7,5,9,8,2,10]
l.sort()
print(f"list the sort method ,\nafter sortig the list in ascending order : {l}")
print(" ")
# for desc order
l.sort(reverse = True)
print(f"list the sort method ,\nafter sorting  the list in descending order : {l}")
print(" ")

# count() :- is used to count number time items occurred in list
l2 = [1,1,2,2,3,3,3,4,4,4,4,5,5,5,5,6,7,8,9]
print(f"list the count method ,\nafter count the list : {l2.count(5)}")
#numc = int(input("Enter the number you want to count: "))
#c = l2.count(numc)
#print(f"list the count method ,\nafter count the list : {c}")
print(" ")


# in :- is used to check the element present in list or not
print(2 in l2)
print(10 in l2)
print(" ")

# not in: return true if the item is not present in the list

# memebership operation

num = [1,2,3,4,5,6,6,7,8]
#Smallest Number
# min()
print(f"Smallest Number : {min(num)}")

#largest Number
#max()
print(f"Largest Number : {max(num)}")

# sum()
print(f"Sum of numbers : {sum(num)}")

