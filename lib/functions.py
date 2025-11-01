#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(name):
    print(f"Hello, {name}!")
    pass

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass

def add(num1, num2):
    return num1+num2

sum_result=add(1+2)
print(sum_result)


pass

def halve(number):
    if isinstance (number (int , float)): 
        return number/ 2
    else:
        return None
    
    result1 =halve(4)
    print(result1)

    result2 = halve("two")
    print(result2)
    pass
