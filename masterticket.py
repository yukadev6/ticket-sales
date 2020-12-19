SERVICE_CHARGE = 2

TICKET_PRICE = 10

tickets_remaining = 100  

# Create the claculate_price function. It takes number of tickets and returns 
#   number_of_tickets * TICKET_PRICE

def calculate_price(number_of_tickets):
    # Create a new constant for the 2 dollar service charge
    
    # Add the service charge to our result
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

# Run this code continuously until we run out of tickets
while tickets_remaining >=1:

    # Output how many tickets are remaining using the tickets_remaining variable
    
    print ("There are {} tickets remaining.".format(tickets_remaining))
    
    # Gather the users name and assign it to a new variable.
    
    name = input("What is your name?   ")
    
    # Prompt the user by name and ask how many tickets they would like
    
    number_of_tickets = input("{}, how many tickets would you like?  ".format(name))
    # Expect a ValueError to happen and handle it appropriately..remember to test it out!
    try:
        number_of_tickets = int(number_of_tickets)
        # Raise a ValueError if the request is for more tickets than are available 
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))    
    except ValueError as err:
        # Include the error text in the output
        print("Oh no! We ran into an issue. {}. Please try again.".format(err))
    else:   
    # Calculate the price (number of tickets they want multiplied by the price) and assign it to a variable
    
        amount_due = calculate_price(number_of_tickets)
        
        # Output the price to the scsreen
        
        print ("The total price is ${}.".format(amount_due)) 
        
        # Prompt user if they want to proceed. Y/N?
        
        confirmation = input("{}, would you like to proceed with this payment? Yes or No?  ".format(name))
        
        # If they want to proceed
        
            # print out to the screen "SOLD!" to confirm purchase
            # TODO: Gather credit card information and process it.
        if confirmation.lower() == "yes":
            print("SOLD!!")
            # and then subtract the tickets remaining by the number of tckets purchased
            tickets_remaining -= number_of_tickets
            
        #Otherwise....
            # Thank them by name
        else:
            print("Thank you anyways, {}.".format(name))
    
# Notify the user that the tickets are sold out
print("Sorry the tickets are all sold out!")