# it should be first thing written in the function as documents
def func():
    """
    this is a docstring
    we are write a function does here
    :return:
    """
    return None

func()
print(help(func))

def divide(num1 , num2):

    """
    num1 : A number to be divided (Numerator)
    num2 : A number to be divided (Denominator)
    :return: float(if num2 is non-zero) or Str(if num2 is zero)
    """
    if num2 == 0:
        return "Cannot divide by zero"

    else:
        result = num1 / num2
        return result

help(divide)
print(divide(10,2))
print(divide(10,0))