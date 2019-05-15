if __name__ == "__main__":
    # Part 1
    print("I always get printed!")

    mr_t = True

    if mr_t:
        print("I only get printed when Mr T lives")

    mr_t = False

    print("I always get printed!")

    if mr_t:
        print("I only get printed when Mr T lives")

    # Part 2
    print("I also always get printed!")

    number_one = True
    number_two = False

    if number_one:
        print("Oh yeah!")

    if not number_two:
        print("Oh no!")

    number_one = False
    number_two = True

    if number_one:
        print("Oh yeah!")

    if not number_two:
        print("Oh no!")

    # Part 3

    stringo = "A string"
    stringo_the_second = "A string"
    inty = 10
    minus_inty = -10

    if stringo == stringo_the_second:
        print("They're equal")

    if inty != minus_inty:
        print("They're not equal")
