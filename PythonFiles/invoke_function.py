import imp

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a function and call it when you need it. When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

print("Invoking function with mix of default args")
introduction_with_mix_of_default_args('James', last_name = "Doe")

print("Invoking function to get product of two numbers")
product_of_two_num(10,20)

print("Invoking function that adds all numbers")
add_all_nums(10,20,30,40)

print("Invoking function that doubles a number")
double(10)

print("Invoking function to compute the fibonacci sequence")
fib(21)

print("Invoking function to get the difference of two numbers")
subtract(20,10)

print("Invoking function to check if a number is a palindrome")
isPalindrome('scolding')
isPalindrome('racecar')

