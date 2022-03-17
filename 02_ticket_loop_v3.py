# Start of loop

# Initialise loop so that it runs at least onces
Name = ""
Count = 0
MAX_TICKETS = 5

while Name != "xxx" and Count < MAX_TICKETS:
   
    # Tells the user how many seats are left
    if Count < 4:
        print("You have {} seats "
        "left".format(MAX_TICKETS - Count))

    # Warns user that there is only ONE seat left
    else:
        print("***There is ONE seat left***")
  

    # Get name (Can't be blank)
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
    