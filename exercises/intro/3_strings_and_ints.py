# Exercise 3: Strings and ints

# You have probably noticed that to print words to the screen we wrap them in speech/quotation marks ("" or '').

# We call this construct a "string" in most programming languages. We can wrap any text or number
# in quotes to create a string - e.g. "dog", "cat", "dwarf" etc.

# A string is a sequence of alphanumeric characters (from Wikipedia). In Python strings are one of
# the most important types of object we can use. Later on we will find out much more about how we can
# use and manipulate strings in many interesting and useful ways to solve problems.

# Strings are often used to represent words (but not always!) - if we want to do mathematical operations
# we must use another type of object that represents a number. To do this we simply
# type a number with no quotation marks e.g. 1, 22, 3330. This object is called an integer (or int for short)

# In this exercise we will use print() to print some integers and strings out to the screen
# and observe how they behave differently from each other.

# In this exercise I would like you to:

# 1. Print the word "Dog" to the screen.
# 2. Print the integer 1 to the screen.
# 3. Print 1 as a string to the screen.
# 4. Add 1 and 1 together and print to the screen - ask your buddy if unsure.
# 5. Add "1" and "1" together and print to the screen - ask your buddy if unsure.
# 6. Add 1 and "1" together and print to the screen - ask your buddy if unsure.

if __name__ == "__main__":
    # 1.
    print("dog")
    print("That was a string we printed to the screen!")

    # 2.
    print(1)
    print("That was an integer we printed to the screen!")

    # 3.
    print("1")
    print("But confusingly - that '1' is a string we just printed to the screen")

    # 4.
    print(1 + 1)
    print("We added two integers together and printed the result to the screen!")

    # 5.
    print("1" + "1")
    print("Look what happens when we add two strings together and print to the screen in comparison!")

    print("Lets see what happens when we try to add a string and an integer together.")

    # 6.
    print(1 + "1")
