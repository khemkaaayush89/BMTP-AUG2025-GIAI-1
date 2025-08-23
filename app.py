import  api
import main

# print("I am in App code")
# print("This is from api file - ", api.s)
print(api.my_string)

if __name__ == "__main__":
    print('I am in APP main block')
    addition = api.add(2,3)
    print(addition)
    addition = api.add(3, 6)
    print(addition)
    subtraction = api.subtract(7, 2)
    print(subtraction)