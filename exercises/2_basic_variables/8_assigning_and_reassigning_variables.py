"""
Exercise 8 - Assigning (and reassigning) variables

If you can't see the power of variables just yet wait till you see what we do in this exercise!

We can actually assign variables to other variables...this is getting into some Inception style dream within
a dream logic now. However don't worry, there is method to the madness as we will see in this example:

Lets say we have two variables - number_one (3 - an integer) and number_two (4 - another integer).
We can add these two variables together to make the integer 7 and print it out to the console.

print(number_one + number_two) (outputs 7)

BUT what if we don't want to print out the output straight away. What if we want to use it later on in the program,
or use it multiple times?

You guessed it! We can assign the result of our addition of number_one and number_two to another variable
named number_three like so:

number_three = number_one + number_two

Now we can do what we like with the value of number three - we can print it
as it is or perform more calculations using it:

print(number_three) (outputs 7)
print(number_three + 3) (outputs 10)
print(number_three * number_three) (outputs 49)

We can do the same with strings:

string_one = "Mad"
string_two = "Max"

string_three = string_one + " " + string_two

print(string_three) (outputs "Mad Max")

Lets take the above example using strings again. Now say later on in your program you don't want the value of
string_three to be "Mad Max" anymore. Well we can SIMPLY reassign the variable to a different value!
Lets see how to do it:

string_three = "Top Gun"

print(string_three) (outputs "Top Gun")

Lets reassign it again - we can reassign as often as we like to keep updating the value of string_three:

string_three = "Braveheart"

print(string_three) (outputs "Braveheart")

As you can see - variable reassignment can be very powerful. However it can also cause confusion
if not kept track of properly. This is why naming variables sensibly is very important. In general these
are some good rules to follow when naming variables in Python:

1. All lower case
2. Words separated by underscores (e.g. number_one, charlie_sheen)
3. Avoid single letter variables as much as possible (a, b, c, x, y)
4. Make them clear and meaningful (e.g. saved_word rather than word or letter_to_remove rather than letter)
5. But not overly verbose either (e.g. saved_word_for_the_next_person_to_see_when_they_read_this_program is not cool)

As well as simple reassignment we can also update the value of a variable using some new assignment operators:

"+=" is probably the most common - it adds the value on the right hand side to the variable on the
left hand side and assigns that new value to the variable.

Example:

my_number = 50
my_number += 65
print(my_number) (outputs 115)

There are other operators "-=", "+=", "*=", "/=" that work the exact same way as the "+=" operator.

Examples:
my_number -= 20
print(my_number) (outputs 95)
my_number /= 5
print(my_number) (outputs 19)
my_number *= 2
print(my_number) (outputs 38)

Here are some tasks:

part 1:

1. Create a variable named price and set it to 50 (integer)
2. Create a variable named amount and set it to 4 (integer)
3. Create a variable named discount and set it to 10 percent of price (hint: price multiplied by 10 divided by 100)
3. Create a variable named result and set it to price multiplied by amount.
4. Print result minus discount to the console.

part 2:

1. Create a variable named ultimate_hero and set it to the name of your favourite superhero (string)
2. Create a variable named ultimate_villain and set it to the name of your favourite villain (string)
3. Create a variable named showdown and set it to this string using the
variables you created -"<ultimate_hero> vs <ultimate_villain>"
4. Print this string to the screen using the variable you created - "Tonight live on the UFC its <showdown>!"

part 3:
1. Reassign ultimate_hero and ultimate_villain to a different superhero and a different villain.
2. Print their values to the screen

part 4:
1. Reassign ultimate_hero and ultimate_villain to a different superhero and a different villain.
2. Print showdown to the screen - what happens?
3. Reassign showdown to this string using the variables you created -"<ultimate_hero> vs <ultimate_villain>"
4. Print showdown to the screen again - what happens this time?

part 5:
1. Create a variable called inflation and set it to be 5 percent of price - see part 1 question 3 for help:
2. Reassign price using the "+=" operator to set it equal to price add inflation
3. Reassign amount using the "-=" operator to set it equal to amount minus 2 (integer)
4. Create a variable called new_result and set it to price multiplied by amount and print it to the screen
5. Reassign result using the "-=" operator to set it equal to price minus discount
6. Create a new variable named total, set it to result add new_result and print the value to the screen.
"""
if __name__ == "__main__":
    # part 1:


    # part 2:


    # part 3:


    # part 4:


    # part 5:
    pass