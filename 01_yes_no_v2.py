
show_instructions = ""
while show_instructions.lower() != "xxx" :
    # Ask the user if they have played before
    show_instructions = input("Have you played this game"
                              " before? ").lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If the answer is invalid, print an error

    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    if show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("program continues")

    else:
        print("Please answer yes / no")

    print ("You chose {}".format(show_instructions))