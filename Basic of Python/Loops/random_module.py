# this modules it used to get random int,float in the program

import random

# random() :- retruns random float between 0.0 and 1.0(excluded)
print(random.random())
print(random.random())

print('_' * 100)
# randint(a,b) :- returns random integer between a and b (both include)

print(random.randint(10,15))
print(random.randint(10,15))
print('_' * 100)

nums = [10,1,2,5,19,9]
# choice(sequence) :- returns a random item from the sequence
print(random.choice(nums))
print('_' * 100)

# suffle(sequence) :- returns the elements shuffled in random order
random.shuffle(nums)
print(nums)