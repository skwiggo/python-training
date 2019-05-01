"""
Exercise 6 - Introduction to variables

With all these data types we have learnt about in the previous exercises we have learned how to create or "instantiate"
them. Whether it's a string by wrapping characters in quotes (e.g. "dog", "cat") or simply typing out
integers, floats and booleans (1, 1.5, True, False) we can easily create a new "instance" of each of these
objects whenever needed.

However - what if we keep using the same object over and over again in our programs? Surely there must be a way
we can use an object multiple times without having to create a new version of that object every time!

This is where we introduce a new concept - the variable. Variables are one of the most widely used
features of programming languages and open up a wide range of new possibilities that we can use in our programs.

What is a variable? Basically it is a tool that allows us to store and reference a data object within Python.
We can then recall the value of that object by using the referenced name we have given to the variable.

When we create a variable and reference a data type we call it "assigning" a variable. To do this we use an operator
called the "assignment operator". This operator is represented by an equals sign ("=").

It probably makes more sense to see an example:

variable = "Hello!"

^ The example above shows us assignment in action. We use the "=" to assign the value of the string "Hello!"
on the left hand side of the "=" to the reference my_variable on the right hand side of the "=".

What does this mean? Well it means if we use the print function with our variable as the parameter
- e.g. print(my_variable) - we should see the value of the variable output inside the console ("Hello!").

Whilst this might not seem to exciting right now in time we will see how powerful variables can be in the next lesson.

For this exercise I would like you to:

1. Create a variable named my_variable and set it's value to the string "Hello_"
2. Create a second variable named my_second_variable and set it's value to "World!"
3. Use print() to print the first variable to the console.
4. Use print() to print the second variable to the console.
5. Use print() to print both variables to the console - this is a bit trickier and leads in to
what we will do in the next lesson!
"""
if __name__ == "__main__":
    my_variable = "Hello_"
    my_second_variable = "World!"

    print(my_variable)
    print(my_second_variable)

    print(my_variable + my_second_variable)