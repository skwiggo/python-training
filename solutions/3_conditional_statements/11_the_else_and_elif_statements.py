
if __name__ == "__main__":
    # PART 1.
    my_string = "Hey stringy and "
    my_string_2 = "hey stringo."

    if my_string == my_string_2:
        print("They match!")
    else:
        print("They don't match")

    # PART 2.
    if my_string == my_string_2:
        print("They match!")
    elif my_string + my_string_2 == "Hey stringy and hey stringo.":
        print("They match when joined!")
    else:
        print("They don't match")
