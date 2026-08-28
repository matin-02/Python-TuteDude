# continue in loop
for i in range(11):
    if i % 3 == 0:
        continue

    print(i)
print('-' * 100)

# break in loop
for i in range(1,11):
    if i % 3 == 0:
        break
    print(i)