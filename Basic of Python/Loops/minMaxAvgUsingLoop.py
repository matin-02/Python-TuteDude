# sum of all 11 player scores
scores = [2,45,67,10,4,8,14,5,8,7,5]
total = 0
for i in scores:
    total += i
print(f"Total of Scores is : {total}")
print('-' * 100)

# without using the for loop
total = sum(scores)
print(f'Total of Scores is : {total}')
print('-' * 100)

# Highest Score in List
highest = scores[0]

for i in scores:
    if i > highest:
        highest = i
print(f'Highest Score is : {highest}')
print('-' * 100)

# Lowest score in the list
lowest = scores[0]
for i in scores:
    if i < lowest:
        lowest = i
print(f'Lowest Score is : {lowest}')
print('-' * 100)

# Using Min and Max to find the highest and lowest score
low = min(scores)
high = max(scores)
print(f'Lowest Score is : {low}')
print('-' * 100)
print(f'Highest Score is : {high}')
print('-' * 100)


