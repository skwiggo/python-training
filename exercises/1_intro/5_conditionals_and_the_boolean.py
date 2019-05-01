# Exercise 5 - Conditionals and the boolean

# Often in programming languages we need to compare two or more values. We have already seen over the past few exercises
# that we can handle different types of data in Python such as strings, integers and floats.

# How do we compare two values to each other? In most programming languages
# including Python there is a data type for just that. The boolean is a data type used for evaluating
# whether a condition is true or false. It a condition is true the evaluation will return True,
# if not it will return False. (Note the capitalisation! Very important in Python).
# We will explore the boolean in more depth later on but for now lets just use it as a indication of
# how our comparisons are turning out.

# Comparing different values is usually done through what we call 'conditional operators' or 'conditionals'.
# These are operators much like the mathematical ones seen in the last exercise. We will go through each one below:

# 1. The equals conditional - "==" - used to compare the equality of two values.
# (e.g "duck" == "duck" will return True as both are strings with the same sequence of characters.)

# 2. The not equals conditional - "!=" - used to check if two values are not equal to each other.
# (e.g "duck" != "frog" will return True as whilst both are strings they do not contain the same sequence of
# characters as each other.)

# 3. The greater than conditional - ">" - used to check if the first value is greater than the second value.
# (e.g 6 > 3 will return True as both are integers and 6 is greater in value than 3)

# 4. The less than conditional - "<" - used to check if the first value is less than the second value.
# (e.g 21 < 30 will return True as both are integers and 21 is less in value than 30)

# 5. The greater than or equal to conditional - ">=" - used to check if the first value is greater
# than OR equal to the second value.
# (e.g 6 >= 3 will return True as both are integers and 6 is greater in value than 3,
# however 3 >= 3 will also return True as 3 and 3 are equal in value unlike 3 > 3 which will return False)

# 5. The less than or equal to conditional - "<=" - used to check if the first value is less
# than OR equal to the second value.
# (e.g 21 <= 30 will return True as both are integers and 21 is less in value than 30,
# however 21 <= 21 will also return True as 21 and 21 are equal in value unlike 3 < 3 which will return False)

# The practical importance of these comparisons will become clear in later exercises.
# Once we begin to put together the fundamentals of Python it will begin to make sense why we need
# to have a good understanding of the different types of data we can use.

# There is no coding in this exercise - instead we will look at a number of print statements using conditionals
# and we will guess whether each statement will return True or False. Don't worry too much about getting them all right
# - there are a few gotchas in Python and we will explain them whilst we go through the questions together.

print(2 == 2) # answer 1.
print(2 != 2) # answer 2.
print(2 > 1) # answer 3.
print(2 < 1) # answer 4.
print(1 >= 2) # answer 5.
print(1 <= 2) # answer 6.
print(1 == 1.0) # answer 7.
print("hello" == "hello") # answer 8.
print(1 == "1") # answer 9.