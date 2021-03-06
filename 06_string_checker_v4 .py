

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
        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

        # check if snack is valid
        snack_choice = string_checker(desired_snack, valid_snacks)
        print("Snack Choice: ", snack_choice)

        # add snack to list...

        #check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid_choice":
            snack_order.append(snack_choice)

# Show snack orders
print()
if len(snack_order) == 0:
    print("Snack Ordered: None")

else:
    print("Snacks Ordered: ")

    for item in snack_order:
        print(item)

