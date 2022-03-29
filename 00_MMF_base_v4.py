# import statements
import re
import pandas

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

# Checks the number of tickets and warns user
def check_tickets(ticket_sold, ticket_limit):
    # Tells the user how many seats are left
    if ticket_sold < ticket_limit - 1:
        print("You have {} seats "
        "left".format(ticket_limit - ticket_sold))

    # Warns user that there is only ONE seat left
    else:
        print("***There is ONE seat left***")

# Gets ticket based on age
def get_ticket_price():
     # ask for age, check it's between 12 and 130
    age = int_check("What is your age? ")

    if age < 12:
        print("Sorry, you are too young for this movie ")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old, it looks like a mistake ")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5
    return ticket_price

# string checker
def string_checker(choice, options):

    for var_list in options:

        #if the snack is in one of the list , return full name
        if choice in var_list:

            # get full name of snack an put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        
        # if  the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is no OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

# Get snacks
def get_snack():
    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # Each item in valid snacks is a lit with
    # valid options for each snack <full name, letter code (a - e)
    # , and possible abbrevations>

    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&Ms", "M&M's", "m&m's", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "c"],
        ["water", "w", "d"],
        ["orange juice", "oj", "o", "juice", "e"]
    ]

    # valid options for yes / no questions
    yes_no = [
        ["yes", "y"],
        ["no", "n"]
    ]

    # holds snack order for a single user
    snack_order = []

    # ask user if they want a snack
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_checker(want_snack, yes_no)

    # If they say yes, ask what snacks they want (and add to our snack list)
    if check_snack == "Yes":

        desired_snack = ""
        while desired_snack != "xxx":

            snack_row = []

            # ask user for desired snack and put it in lowercase
            desired_snack = input("Snack: ").lower()

            if desired_snack == "xxx":
                break

            # if item has a number, separate it into two (number / item)
            if re.match(number_regex, desired_snack):
                amount = int(desired_snack[0])
                desired_snack = desired_snack[1:]

            else:
                amount = 1
                desired_snack = desired_snack


            # remove white space around snack
            desired_snack = desired_snack.strip()

            # check if snack is valid
            snack_choice = string_checker(desired_snack, valid_snacks)
        

            # check snack amount is valid (less than 5)
            if amount >= 5:
                print("Sorry - we have a four snack maximum ")
                snack_choice = "invalid choice"

            # add snack AND amount to list...
            
            snack_row.append(amount)
            snack_row.append(snack_choice)

            # give an error message if snack choice is invalid
            if snack_choice == "invalid choice":
                print("oops, please enter a valid option")
                print()

            # check that snack is not the exit code before adding
            if snack_choice != "xxx" and snack_choice != "invalid choice":
                snack_order.append(snack_row)

    return snack_order    


# ********** Main Routine ***********
# Set up dictionaires/listes needed to hold data

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# list of valid payment methods 
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]
# Initialise loop so that it runs at least onces
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# Initialise  lists (to make data-frame in due course)
all_names = []
all_tickets = []

# snack lists
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# store surcharge multiplier
surcharge_mult_list = []

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_mult_list
}


price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}

# Ask users if they have used the program before & show them how

# Loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:
   
      # check numbers of ticket limit has not been exceeded
    check_tickets(ticket_count, MAX_TICKETS)

    # **** Get details for each ticket **** 

    # Get name (can't be blank)
    name = not_blank("Name: ")
    print(name)

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # get ticket price based on age 
    ticket_price = get_ticket_price()
    # if age is invalid, restart loop (and get name again)
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # add name and ticket price to lists 
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Get snacks 
    snack_order = get_snack()   
    print("snack order", snack_order)

    # Assume no snacks...
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    # Get payment methiod, work out surcharge if necessary
    
    # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit) ").lower()
        how_pay = string_checker(how_pay, pay_method)

    
    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    surcharge_mult_list.append(surcharge_multiplier)
        
# End of ticket loop / snacks / payment loop

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# create dataframe and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called subtotal
# fill it price for snacks and ticket
movie_frame["Snacks"] = \
    movie_frame['Ticket'] + \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame["Sub Total"]=\
    movie_frame['Ticket'] + \
    movie_frame['Snacks']

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

# Shorten Column names
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                          'Pita Chips': 'Chips',
                                          'Surcharge_Multiplier': 'SM'})



# Set up columns to be printed
pandas.set_option('display.max_columns', None)

# Display number to 2dp
pandas.set_option('precision', 2)

print_all = input("Print all columns?? (y) for yes")
if print_all == "y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket', 'Sub Total',
                        'Surcharge', 'Total']])

print()
    
# Calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))


# Tell the user they have unsold tickets
if ticket_count == MAX_TICKETS:
    print("You have sold all the tickets!")
else:
    print("You have sold {} tickets. \n"
         "There are still {} places still available "
         .format(ticket_count, MAX_TICKETS - ticket_count))
    

    

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snakc price

    # ask for payment method (and apply surcharge if needed)


# Calculate total sales and profit

# Output data to text file