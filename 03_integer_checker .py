# funcion goes here

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

# Main routine goes here
age = int_check("Age ")

# Check that age is valid
    if age < 12:
        print("Sorry, you are too young for this movie ")
        continue
    if age > 130:
        print("That is very old, it looks like a mistake ")
        continue


