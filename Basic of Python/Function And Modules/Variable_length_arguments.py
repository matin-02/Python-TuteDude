# *args :- variable length positional arguments it takes 0 or more value(0 to n)
# we can take any number of arguments using the *args

def add(*args):
    print(type(args))
    return sum(args)

ad = add(5,5,5)
print(ad)

def Student_deatils(sid,sname,*marks):
    if len(marks) ==  0:
        print(f" The Name Of Student is : {sname} \n The Student Id is : {sid} \n Not Attend the Exam")

    else:
        percent = sum(marks) / len(marks)
        print(f" The Name Of Student is : {sname} \n The Student Id is : {sid} \n The Percentage is : {percent}%")


Student_deatils(101, "John", 85, 95, 75, 88, 90)
Student_deatils(102, "Mark")
print("=" * 100)


# **kwargs :- Variable length keyword arguments
# it should be last argument in the function

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

func(x = 10 , y= 20)
func()

def std(sid , sname , *extra , **marks ):
    if len(marks) == 0:
        print(f"The Student {sname} with the {sid} Was Not Attended exam")

    else:
        percent = sum(marks.values()) / len(marks)
        print(f" The Name Of Student is : {sname} \n The Student Id is : {sid} \n The Percentage is : {percent}%")

    print(f" {sname} does {extra}")

std(101, "John" ,"Cricket" , "Football" , sub1 = 95 , sub2 = 90 , sub3 = 80 , sub4 = 90)