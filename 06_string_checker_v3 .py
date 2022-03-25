

# Function goes here
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

    # if the snack is no OK - asl question again.
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

# valid snacks holds list of all snacks
# Each item in valid snacks is a lit with
# valid options for each snack <full name, letter code (a - e)
# , and possible abbrevations>

valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "c"],
    ["water", "w", "d"]
]

# loop three times to make testing quicker
for item in range(0, 6):

    #ask user for desired snack and put it in lowercase
    desired_snack = input("Snack: ").lower()

    # check if snack is valid
    snack_choice = string_checker(desired_snack, valid_snacks)
    print("Snack Choice: ", snack_choice)

    