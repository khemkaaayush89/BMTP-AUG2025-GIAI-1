def add(a,b):
    """
     a function to add two values
    :param a: int value
    :param b: int value
    :return: s: sum of a and b
    """
    s = a + b
    return s

def subtract(a,b):
    """
     a function to subtract two values
    :param a:
    :param b:
    :return: s: subtraction of a and b
    """
    s = a - b
    return s

# print("I am outside main")

s = 4+7

my_string = "This is a string in api.py"


if __name__ == "__main__":
    print('I am in main function')
    addition = add(2,3)
    print(addition)
    addition = add(3, 6)
    print(addition)
    subtraction = subtract(7, 2)
    print(subtraction)