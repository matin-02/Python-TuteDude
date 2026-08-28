s1 = "Hello World"
for char in s1:
    print(char)
print("end of the loop")
print("-" * 100)

# for loop with the dict
emp_id = {
    "name": "John",
    "age": 0,
    "gender": "male",
        }
for i in emp_id:
    print(emp_id[i])

print("-" * 100)
for i in emp_id.items():
    print(i)

print("-" * 100)
for i in emp_id.values():
    print(i)

print("-" * 100)
for i in emp_id.keys():
    print(i)