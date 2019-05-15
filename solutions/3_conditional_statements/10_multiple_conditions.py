if __name__ == "__main__":
    # PART 1.
    tv_star = "Keifer Sutherland"
    music_star = "Trent Reznor"
    tv_show = "24"
    band = "Nine Inch Nails"

    if tv_star and music_star:
        print(tv_show)
        print(band)

    tv_star = ""

    if tv_star and music_star:
        print(tv_show)
        print(band)

    # PART 2.
    tv_star = "Keifer Sutherland"

    if tv_star == "Keifer Sutherland" or music_star == "Trent Reznor":
        print(tv_show)
        print(band)

    tv_star = "Peter Dinklage"

    if tv_star == "Keifer Sutherland" or music_star == "Trent Reznor":
        print(tv_show)
        print(band)

