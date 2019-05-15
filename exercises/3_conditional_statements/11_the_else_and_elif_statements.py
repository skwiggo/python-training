"""
Exercise 11 - The 'else' and 'elif' statements

We've seen how we can execute code conditionally using if. However, what can we do if we want to execute some code
when an if condition is not met.

Luckily we can achieve the above using the 'else' statement. Else is an addition to the if statement - if the conditions
within the if are not met, the code within the else block is executed instead. An if with an else clause
uses this structure:

if <condition is met>:
    <then execute this code within this block here>
else:
    <if the condition is not met execute this block here>

Else always has to be used with an if statement, it can never be used by itself.

Lets see an example using the card game Blackjack:

We initialise a variable to an integer and check if it is equal to 21. If it is we print "Blackjack!",
if not we print ("Bust!").

my_value = 21

if my_value == 21:
    print("Blackjack!")
else:
    print("Bust!")

Another (more complicated example) with multiple conditions using an 'or' clause:

another_value = 40
a_sum = 10 + 31

if another_value == 40 or a_sum == 40:
    print("At least one condition matches!")
else:
    print("No conditions match...")

What happens if we want to use multiple conditions to execute different blocks of code. For instance
we could have a program that checks to see if a variable is equal to "Hello!" - if it is we print the variable,
if not we print "No match" using the else clause.

What if we also want the program to print a different string if the variable is equal to "Sausages"?

Most programming languages allow us to combine else and if together to fulfil this requirement. Python is slightly
different to other languages in that it has a keyword 'elif" that combines else and if together to
achieve the exact same thing. This is how an if statement with elif clause is structured.

if <condition is met>:
    <execute this code block>
elif <this condition is met>:
    <execute this code block instead>

Like else, elif can only be used alongside an if statement. If the condition in the if is met, the code will never make
it to the elif so even if the elif is also satisfied it won't run.

We can also combine else with elif too:

if <condition is met>:
    <execute this code block>
elif <this condition is met>:
    <execute this code block instead>
else:
    <if none of the above conditions are met execute this block here>

Lets see some examples:

Here's the first blackjack example again but expanded with elif. Now we only print "Bust" if my_value is not equal
to or less than 21 which is closer to the real life game.

my_value = 21

if my_value == 21:
    print("Blackjack!")
elif my_value < 21:
    print("Oops, undershot it!")
else:
    print("Bust!")

Another more complicated example with multiple conditions:

another_value = 40
a_sum = 10 + 31

if another_value == 40 and a_sum == 40:
    print("Both conditions match!")
elif another_value == 41 or a_sum == 41:
    print("One condition matches!")
else:
    print("No conditions match...")

We see in this example that we first check if both variables are equal to 40. If not we move onto the elif and check
if at least one condition is equal to 41. If not we execute what is in the else clause.

In this exercise I would like you to:

PART 1:
1. Create two variables:
my_string = "Hey stringy and "
my_string_2 = "hey stringo."

2. Create an if statement with an else clause to check if the variables are equal to each other.
    If they are - print "They match!" to the console.
    Else if they don't print "They don't match" to the console.
3. What does the program print to the screen?

PART 2:

1. Using the same variables as before...
2. Create an if statement with elif and else clauses.
    If the strings match print "They match!" to the console.
    Else if they strings match "Hey stringy and hey stringo." when added together print "They match when joined!"
    to the console.
    Else if they don't match at all print "They don't match" to the console.
3. What does the program print to the screen?
"""

if __name__ == "__main__":
    pass
    # PART 1.


    # PART 2.
