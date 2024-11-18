def choose_practicum():
    answer = input("What practicum would you like to sign up for? ")
    if answer == "costumes" or answer == "Costumes" or answer == "scenery" or answer == "Scenery" or answer == "lighting" or answer == "Lighting" or answer == "sound" or answer == "Sound":
        return answer
    else:
        print("Sorry, that is not a valid practicum. Your choices are costumes, scenery, lighting, or sound.")
        return choose_practicum()


def application():
    name = input("What is your name? ")
    practicum = choose_practicum()
    print(f"Congratulations, {name}, you are signed up for {practicum}!")

application()