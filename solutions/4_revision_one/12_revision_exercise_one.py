if __name__ == "__main__":
    your_name = input("Please type in your name:")

    if your_name:
        your_colour = input("Hi " +  your_name + ", Please type your favourite colour:")

        if your_colour == "red" or your_colour == "blue":
            print(your_colour +"? Thats a snazzy colour")
        elif your_colour == "yellow" or your_colour == "green":
            print(your_colour + "? Thats a pretty awful colour to be honest...")
        else:
            print(your_colour + "? Sadly I don't think I've heard of that colour before")

        your_colour = "brown"

        if your_colour == "brown":
            number_one = input("Type a number:")
            number_two = input("Type another number:")

            if int(number_one) - int(number_two) > 0:
                print("Greater than zero!")

            if int(number_one) + int(number_two) < 20:
                print("Less than twenty!")
