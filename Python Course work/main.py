import read
import operation



def user_input():
    '''
    this functions takes no parameters but when called this function it asks for user input and calls respective functions when user inputs valid number.
    Parameters None
    Returns None 
    This function calls the other function present in operations
    Raises: 
    Value Error:
    If user inputs invalid entry such as number different than metiond then loops through the function again and again untill desired input is typed by the user.
    eg; user inputs 6 then 
    loops run untill 1/2/3/4 is typed.
    '''
    check_value=False
    print("Welcome To We care Shop")
    print("Where you get all the Skin care Products")
    #loop runs untill valid input is given by the user
    while(check_value == False):
        try:
            print("Press 1 to sell     ")
            print("Press 2 to restock  ")
            print("Press 3 to display  ")
            print("Press 4 to exit     ")
            
            num=int(input("Enter a number: "))
            
            if (num == 1):
                #calls the buy funcion passing the storevalue dictonary as parameter
                operation.buy(read.store_value)
                check_value = False
                
            elif (num == 2):
                
                #calls the buy funcion passing the storevalue dictonary as parameter
                operation.sell(read.store_value)
                check_value =False
                
                
            elif (num == 3):
                
                #calls the display funcion and again repeats the loop
                read.display_value()
                check_value=False
                
            elif(num == 4):
                
                #exits the program as break is use for that
                check_value =True
                break
            
            else:
                check_value=False
                print("choose between 1-3")
                
        except ValueError:
            #handles the errror input and repetas until valid number is given
            print("Invalid input \n Choose betwwen 1-3      ")

#calling the user_input method
user_input()
                
  
