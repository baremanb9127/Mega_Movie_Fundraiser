# Start of loop

# Initialise loop so that it runs at least onces
Name = ""
Count = 0
MAX_TICKETS = 5

while Name != "xxx" and Count < MAX_TICKETS:
    print("You have {} seats "
        "left".format(MAX_TICKETS - Count))

    if Count < 4:
        print("You have {} seats "
            "left".format(MAX_TICKETS - Count))

        # Warns the user that theres one ticket left
    else:
        print("*** You have ONE seat left ***")

        # Get Details
        Name = input ("Name:  ")

        if Name == "xxx":
            break
                
        Count += 1
        print()

    if Count == MAX_TICKETS:
        print("You have sold all the tickets!")
    else:
        print("You have sold {} tickets. \n"
            "There are still {} places still available "
            .format(Count, MAX_TICKETS - Count))
    