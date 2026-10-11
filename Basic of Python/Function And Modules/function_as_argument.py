#  In Python, we can pass a functions argument of another function

def add(num):
    return num + 1

def square(number):
    return number ** 2

print(square(5))

num = int(input("enter a number : "))
res1 = add(num)
res2 = square(res1)
res3 = square(add(num))
print(res2)
print("the res 3 is : ", res3)

# date time modules
import datetime as dt
t = dt.time(8, 43 ,51)

