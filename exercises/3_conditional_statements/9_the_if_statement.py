"""
Exercise 9 - The 'if' statement

In exercise 5 we used equality operators (such as '==' and '!=') to check if (or if not) certain
values were equal to each other. We also used the boolean alongside equality operators to check if a
value was equal to true or false.

We can take this concept of equality a step further in this exercise by using the equality of a value to
decide what the program does next. To do this we can use an 'if' conditional statement.
Here is the structure of an if statement and an explanation of how it works.

if <condition is met>:
    <then execute this code within this block here>

The statement checks if the if statements "condition" is met. If the condition is met then the code inside the
if statement block (signified by the indentation) is executed by the program. If the condition is not met the code
is ignored and the program continues.

Here are some simple examples to demonstrate how they can be used.

Example 1:

In Python certain data types such as strings that contain characters, positive numeric values
(both integers and floats) and True booleans always evaluate as true.

"cat" == True
1 == True
2.2 == True
True == True

We can write out an if statement so that if a variable is equal to True then the code in the if statement code block is
executed. In this case the print function will print the string to the console.

my_variable = True

if my_variable == True:
    print("Yay! The if statement executed my code!")

print("It's fun learning about Python!")

If we set the my_variable to equal False in the above example then only the second print statement will be executed.

Python also makes things simple for us. We don't actually need to explicitly use an equality operator to
check if my_variable is equal to True. We can simply write the following without the == True and it will
work the same way (and is best practice).

my_variable = True

if my_variable:
    print("Yay! The if statement executed my code!")

print("It's fun learning about Python!")

Example 2:

Conversely certain data types such as empty strings (quotes with nothing in them - ""), negative or zero numeric
values and False booleans always evaluate as false.

Lets repeat the same example but set my_variable to false and check that it is equal to false.

my_variable = False

if my_variable == False:
    print("Yay! The if statement executed my code!")

print("It's fun learning about Python!")

Like the first example there is a shorter best practice way of writing this statement without the equality operator.
We can use the "not" keyword to check if the value is equal to False.

my_variable = False

if not my_variable:
    print("Yay! The if statement executed my code!")

print("It's fun learning about Python!")

Example 3:

Like in exercise 5 we can use equality operators to check if two values are equal to each other within an
if statement with the equality operator:

my_string_one = "Hello!"
my_string_two = "Hello!"

if my_string_one == my_string_two:
    print("The strings are equal")

If we change the value of one of the variables to a different string and run the program again
the code block in the if statement will not run.

We can use the other equality operators such as not equal to (!=), greater than (>) or less than (<) as conditions
within our if statements as well!

In this exercise I would like you to:

PART 1:

1. Write a print function that prints ("I always get printed!") to the console.
2. Create a variable called mr_t and set it to True
3. Create an if statement that checks if mr_t is True
4. If mr_t is True then there should be a print function within the if statement code block
that prints ("I only get printed when Mr T lives!")
5. Set mr_t to False - how many and which print functions are executed?

PART 2:

1. Write a print function that prints ("I also always get printed!") to the console.
2. Create two variables - one called number_one that set to True and another called number_two that is set to False
3. Create an if statement that checks if number_one is set to True and prints "Oh yeah!" to the screen.
4. Create another if statement that checks if number_two is set to False and prints "Oh no!" to the screen.
5. Set number_one to False and number_two to True and run the program again. What gets printed?

PART 3:

1. Create four variables:
stringo - set to "I'm a string"
inty - set to 10
minus_inty - set to -10
stringo_the_second - set to "I'm a string"

2. Create an if statement that checks if stringo is equal to stringo_the_second
and prints "They're equal" to the console.

3. Create an if statement that checks if inty is not equal to minus_inty and prints "They're not equal" to the console.
"""

if __name__ == "__main__":
    pass
    # Part 1

    # Part 2

    # Part 3
