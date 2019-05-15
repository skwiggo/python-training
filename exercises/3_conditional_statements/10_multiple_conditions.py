"""
Exercise 10 - Multiple conditions

In the last exercise we learned how we can use if statements to decide based upon conditions what pieces of
code in our program should be executed. However we only dealt with single conditions. In this exercise we will look at
how we can expand the previous examples to cover cases where we want multiple conditions in a statement.

To cover multiple conditions in a single statement there are two new keywords we can use to help us - 'and' and 'or'.
Lets see by example how they can be used.

Example 1 - and:

We can use 'and' when we want two or more conditions to always be met. If any of the conditions are not
met the code inside the block is never executed. Take the below example which will execute if both variables are true.

my_variable = True
my_variable_2 = True

if my_variable and my_variable_two:
    print("Woohoo - all conditions met!")

However if we set one of the variables to false the code does not run.

Lets try a more complex example. In this example we check if two integers added make a specific number
and if two strings are not equal to each other. If all conditions are met the print function prints
the string to the console.

int_1 = 15
int_2 = 40

string_1 = "Dog!"
string_2 = "Cat!"

if int_1 + int_2 == 55 and string_1 != string_2:
    print("All conditions A OK!")

Example 2 - or:

We can use 'or' when have two or more conditions but we only care if any of the conditions are met.
If any of the conditions are met the code inside the block will be executed. Take the below example which
will execute if either variable is true.

my_variable = True
my_variable_2 = False

if my_variable or my_variable_two:
    print("Phew - a condition was met!")

Again lets see a more complex example (with three conditions!). If any of these conditions are
met the string is printed.

int_1 = 15
int_2 = 40

string_1 = "Dog!"
string_2 = "Cat!"

if int_1 == 40 or string_1 == "Dog!" or int_1 + int_2 == 39:
    print("At least one of those crazy conditions met!")

One condition (string_1 == "Dog!") is met so the string is printed to the screen.

NOTE: using lots and lots of conditions in one statement is bad practice. If your using more than three conditions
in an if statement your probably doing something wrong. Lots of conditions can quickly lead to code that
is difficult to read or even buggy code.

In this exercise I want you to:

PART 1:
1. Create four variables:
tv_star = "Keifer Sutherland"
music_star = "Trent Reznor"
tv_show = "24"
band = "Nine Inch Nails"

2. Create an if statement that checks if tv_star and music_star are both true
(in other words they are set to a string that isn't empty).
If they are print tv_show and band to the console.

3. Change tv_star to an empty string - what will be printed?

PART 2.
1. Use the same variables as above. Set tv_star back to "Keifer Sutherland".

2. Create an if statement that checks if tv_star equals "Keifer Sutherland" or music_star equals "Trent Reznor".
If either condition is met print tv_show and band to the console.

3. Change tv_star to "Peter Dinklage" - what will be printed?
"""

if __name__ == "__main__":
    pass
    # PART 1.


    # PART 2.


