# Functions go here 

print("Your name?")

def not_blank(question):
    valid = False


    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print ("Sorry - this can't be blank")

    
# Main Routine Goes Here
name = not_blank("Name: ")
print(name)
