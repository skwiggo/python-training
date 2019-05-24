"""
Exercise 12 - Revision 1 - lets make a program with input()!

In this exercise we will consolidate some of the things we have learned over the previous 11 exercises such as
variables, operators and conditional statements.

We are going to create a simple application that will take some information that you have input and
print that information out to the console.

To do this we are going to learn a new in built Python tool - the input function. We can use this function
to prompt a user of our application to type in a value. We can then capture that value as a variable and
use it in our program!

The syntax for input is this:

input("Prompt for the user to type some text:")

The string prompt in the parentheses will be displayed for the user in the console and will indicate what
they should type. For example - "Please enter a name:"

There is a catch to input - it only works with strings by default! This is a problem if we want to do
mathematical operations with integers. However there is a way round this. If we set a variable to input
we can then convert the string to an integer using another handy built in function - int().
This function takes a data type and converts (or casts) it to a string. We will learn more about
type conversion later on.

This is an example of us converting the string we save as your_number using input to an integer using int() and
then doing a mathematical calculation:

your_number = input("Please enter a number:")

if int(your_number) + 2 == 3:
    print("Yay it equalled 3!")

This exercise is best done as a pair with your programming buddy, they will help guide you though the steps.

1. Create a variable called your_name and set it equal to input() with a prompt of "Please type in your name:"

2. Check if your_name is equal to true using an if statement. The next set of code will go in this code block.

3. Create another variable called your_colour and set it equal to input()
with the prompt of "Hi <enter_your_name_here>, Please type your favourite colour:" replacing <your_name_here>
with the variable your_name.

4. Create an if statement that checks if your colour is equal to "red" or "blue" and if it is
prints "<your_colour_here>? Thats a snazzy colour". Replace <your colour_here> with the variable your_colour.

5. Create an elif clause to the if statement that checks if your colour is equal to "yellow" or "green" and if it is
prints "<your_colour_here>? Thats a pretty awful colour to be honest...". Replace <your colour_here> with
the variable your_colour.

6. Create an else clause for the if statement that prints
"<your_colour_here>? Sadly I don't think I've heard of that colour before".

7. Set your_colour to equal "brown"

8. Create an if statement that checks if your_colour is equal to "brown". The next set of code will go
in this code block.

9. Create a variable named number_one and set it to equal input() with the prompt "Please enter a number:"

10. Create another variable named number_two and set it to equal input with the prompt "Please enter another number:"

11. Create an if statement that checks if number_one - number_two is greater than 0 and
print out "Greater than zero!" if True. REMEMBER TO USE INT() TO CONVERT THE STRINGS TO INTEGERS.

12. Finally, create an if statement that checks if number_one + number_two is less than 20 and
print out "Less than twenty!" if True. REMEMBER TO USE INT() TO CONVERT THE STRINGS TO INTEGERS.

"""
if __name__ == "__main__":
    pass
