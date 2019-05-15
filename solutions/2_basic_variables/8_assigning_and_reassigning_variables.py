if __name__ == "__main__":
    # part 1:
    price = 50
    amount = 4
    discount = price * 10 / 100
    result = price * amount
    print(result - discount)

    # part 2:
    ultimate_hero = "Spiderman"
    ultimate_villain = "Venom"
    showdown = ultimate_hero + " vs " + ultimate_villain
    print("Tonight live on UFC its " + showdown + "!")

    # part 3:
    ultimate_hero = "Batman"
    ultimate_villain = "Joker"
    print(ultimate_hero)
    print(ultimate_villain)

    # part 4:
    ultimate_hero = "Captain America"
    ultimate_villain = "Thanos"
    print(showdown)
    showdown =  ultimate_hero + " vs " + ultimate_villain
    print(showdown)

    # part 5:
    inflation = price * 5 / 100
    price += inflation
    amount -= 2
    new_result = price * amount
    print(new_result)
    result -= discount
    total = result + new_result
    print(total)
