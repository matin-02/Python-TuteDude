# dictionary : comma seperated key-value pairs enclosed within {}
# each key-value pair seperated by colon
# ex : {key1:value1 , key:value2}
# keys cannot be duplicate in the dict keys must be unique

groceries = {'milk' : 60 , 'bread' : 50 , 'butter' : 40 }
print(groceries)
print(type(groceries))
print()
print(len(groceries))
print()
# indexing in dict: it doesn't have indexing in dict
#print(groceries[0])

# to fetch the value of dict we have to use the key
print(groceries['milk'])

print()
# dict are mutuable
groceries['milk'] = 70
print(groceries)
print()

# updating the dict and adding new key-value pair

groceries['egg'] = 10 # adding the new key-value pair

groceries['milk'] = 100 # updating the existing value
print(groceries)
print()


