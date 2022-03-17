# import statements


# functions go here

# checks that response is not blank
def not_blank(question):
    valid = False


    while not valid:
        response = input(question)

# If name is not blank, program continues
        if response != "":
            return response

        # If name is blank, show error and repeat loop
        else:
            print ("Sorry - this can't be blank")

# checks that response is a number
def int_check(question):

    error = "Please enter a whole number that is higher that 11 and lower than 131"

    valid = False
    while not valid:

        # ask user for number and check if it is valid
        try:
            response = int(input(question)) 
            
            if response <= 0:  
                print(error)
            else:
                return response

        # if an integer is not entered, display an error message 
        except ValueError: 
            print(error)


# ********** Main Routine ***********


# Set up dictionaires/listes needed to hold data


# Ask users if they have used the program before & show them how

# Loop to get ticket details
# Initialise loop so that it runs at least onces
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
   
    # Tells the user how many seats are left
    if count < 4:
        print("You have {} seats "
        "left".format(MAX_TICKETS - count))

    # Warns user that there is only ONE seat left
    else:
        print("***There is ONE seat left***")
  

    # Get name (can't be blank)
    name = not_blank("Name: ")
    print(name)


    if name == "xxx":
        break

    # ask for age, check it's between 12 and 130
    age = int_check("What is your age? ")

    if age < 12:
        print("Sorry, you are too young for this movie ")
        continue
    elif age > 130:
        print("That is very old, it looks like a mistake ")
        continue

    count += 1

if count == MAX_TICKETS:
    print("You have sold all the tickets!")
else:
    print("You have sold {} tickets. \n"
         "There are still {} places still available "
         .format(count, MAX_TICKETS - count))
    

    

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snakc price

    # ask for payment method (and apply surcharge if needed)


# Calculate total sales and profit

# Output data to text file