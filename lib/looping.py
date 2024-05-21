#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while i>0 :
        print(i)
        i -= 1
        print("Happy New Year!")
        
def square_integers(int_list):
    # code goes here!                                       
       squared_list = [x ** 2 for x in int_list]
       return squared_list

# trying it out
input_list = [1, 2, 3, 4, 5]
result = square_integers(input_list)
print(result)  


def fizzbuzz():
    # code goes here!
      # Iterate from 1 to 100
    for i in range(1, 101):
        # Check if the number is divisible by both 3 and 5 first, as it's the most specific condition
        #if you divide this number(i) is the reminder equal to zeroo?? if yess print
        if i % 3 == 0 and i % 5 == 0: 
            print("FizzBuzz")
        # Check if the number is divisible by 3
        elif i % 3 == 0:
            print("Fizz")
        # Check if the number is divisible by 5
        elif i % 5 == 0:
            print("Buzz")
        # If none of the above conditions are met, simply print the number
        else:
            print(i)
