# Functions go here 

print("Your name?")

def not_blank(question , error_message):
    valid = False


    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print (error_message)

    
# Main Routine Goes Here
name = not_blank("Name: " , "Sorry - this can't be blank, " 
"Please enter a name.")
print(name)


