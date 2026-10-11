def add(a,b):
    return a+b

# Positional Arguments - passing the arguments in order of their position
# ex :-
result = add(1,2)
print(result)

# 2. Default arguments :- assing the value at the function declaration
# The Non-default arguments should not follow default arguments
def add(a,b = 10):
    return a+b

result = add(10, 5)
print(result)
res2 = add(10)
print(res2)

#def add(a,b = 10 , c): this is not allowed

def add(a , b = 10 , c =10):
    print(f"a : {a} , b : {b} , c : {c}")
    return a+b+c

# Keyword Arguments :- passing the value during the function call
res3 = add(10 , c = 50)
print(res3)
res4 = add(10,c=20 , b = 2)
print(res4)