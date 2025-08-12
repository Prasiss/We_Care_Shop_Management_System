

import read
import write

'''
empty list to store the products which cane accessed by any function 
present in this file as well as other file fater importing operation

'''

def buy_product(id_,quantity,dict_):
    """
        This function handles the buy function. It takes a quntity, dictonary and id as a parameter. and checks for errors such as if product quantity is less than the desired quantity. 
        and handles the buy function. This function also ammeds the quantity by reducing the amount of quantity the customer requires.

        Parameters:
            id (Integer) is the id of the product that the customer wants to buy and quantity (Integer) is the amount of quantity that the customer wants. 
            Product_list (dict) is a list of dictonary that contains a key value pair of id and values. The value contain the product list as mentioned below:
            Each values conatins :
            -ProductName (String) The name of the product
            -ProductManufactoror (String) The naame of the manufactoror of the products
            -ProductQuantity (INteger) Its the no of quantity of the product we have in our store.
            -ProductPrice (Integer) It's the price of the the Product.
            -Countryof Origin (String ) Its the country where the products was made in
        Returns 0 Or dictonary

            This function retuns 0 if the qunatity asked by the customer is more than the quantity we have in our stock.
            Else this function retuns a dictonary of bought items by the customer which includes the following data:
            -ProductName (String) The name of the product
            -ProductManufactoror (String) The naame of the manufactoror of the products
            -ProductQuantity (Integer) the amount of quantity the customer wants to buy.
            -ProductPrice (Integer) It's the price of the the Product.
    """
    #array to storebought values only
    buy=[]
    
    #checking and returning if quantity to access is grator than stock quantity
    available_quantity=int(dict_[id_]["Quantity"]) 
    if (available_quantity < quantity):
        print("We have limited stock available. The maximum quantity is: ",available_quantity)
        return 0
    
    dict_[id_]["Quantity"] -= quantity
    buy=[dict_[id_]["Product name"],dict_[id_]["Product Manufacturer"],quantity,dict_[id_]["Price"]]
    
    #returns buy array consisting an array of product sold
    return buy




def sell_product(id_,quantity,product_dict_):
    """
        This function handles the sell function which includes increasing the quantity of the item that was sold to us by the seller. 
        Parameters: 
        Quantity(INteger) It id the amount of product sold to us by the seller 
        id(Integer) It is the id in which the  product deatils were saved  in the existing dictory of product deatils as a key vaule pairs.
        Product_dict (dict) is a list of dictonary that contains a key value pair of id and values. The value contain the product list as mentioned below:
            Each values conatins :
            -ProductName (String) The name of the product
            -ProductManufactoror (String) The naame of the manufactoror of the products
            -ProductQuantity (INteger) Its the no of quantity of the product we have in our store.
            -ProductPrice (Integer) It's the price of the the Product.
            -Countryof Origin (String ) Its the country where the products was made in
        Retuns 1    
            This function Return 1 when sucessfully executed. so if i is returned thwn we know that the ammendmenst have been done to the dictonary by increasing the quantity.

    """
    product_dict_[id_]["Quantity"] = product_dict_[id_]["Quantity"]+quantity
    
    return 1 #returns 1 if funtion operates properly
    
      
def sell_products(id_,soldproduct_list_,product_dict_):
    """
        This sell products function handles the sell  product that the seller sells to us. This function appends the dictonary as the seller sells us products of different name to our store.
        This function add the data to our exising dictonary with the help of id as a key and the list as the values.
        Parameters: 
            id(Integer) It is the id in which the new product deatils were going to be places in the existing dictory of product deatils as key vaule pairs.
            newproductlist_(list of new items) 
            dictonary of products(Dictonary) this dictonary contains the following values with a key from 1- 3 with values:
            Each values conatins :
                -ProductName (String) The name of the product
                -ProductManufactoror (String) The naame of the manufactoror of the products
                -ProductQuantity (INteger) Its the no of quantity of the product we have in our store.
                -ProductPrice (Integer) It's the price of the the Product.
                -Countryof Origin (String ) Its the country where the products was made in

        Retuns 1    
            This function Return 1 when sucessfully executed. so if i is returned thwn we know that the ammendmenst have been done to the dictonary.

    """
    #creates a new elemt in dictornary with new key value pairs.
    product_dict_[id_]={"Product name":soldproduct_list_[0],
                     "Product Manufacturer":soldproduct_list_[1],
                     "Quantity":soldproduct_list_[2],
                     "Price":(soldproduct_list_[3])*3,
                     "Country": (soldproduct_list_[4])
                }
    return 1
        


def free_product(x):
    """ 
        This Free product function handles the free product that the customer gets when she/he gets if they buy more than 3 quantity.This funcion uses basic division to find the no of free products the customer gets when they buy products from our store.

        Parameters: This function takes a integer X as a parameter and does arthematic operation in it.
        X(Integer)
        Retuns Freeproducts(Integer) 
        This is the free products that the customer gets after buying more than 3 producst. If user buys less than 3 product the return value is zero.
    """
    
    if (x < 3):
        return 0
    else:
        free_product= x // 3 # divides and gives the quotient
    
    #returns free products if the customer buys more than 3 products
        return free_product




product_list=[]
def buy(dict_):
    """
        This buy function handles the buying of the products. It first takes the user input such as id and quantity and chekcs for any invalid entry and then displays a message for product 
        bougnt and askes for name and address if no other products are required to the customer. Then this function calls the append file and invoice generation function passing the required parameters. 
        Parameters: 
            dictonary of products(Dictonary) this dictonary contains the following values with a key from 1- 3 with values:
            Each values conatins :
                -ProductName (String) The name of the product
                -ProductManufactoror (String) The naame of the manufactoror of the products
                -ProductQuantity (INteger) Its the no of quantity of the product we have in our store.
                -ProductPrice (Integer) It's the price of the the Product.
                -Countryof Origin (String ) Its the country where the products was made in
        Return: Nothing
        But since return function is used it terminates this function and goes back to the loop which called this function.
        Raises: Value error
        If the user inputs invalid id or quantity less than 0 then it again asks for userinput. 
    """
    value = False
    while (value == False): #loop continus until the condition is true
        
        try:
            id_ = int(input("Enter the id of the product you wanna buy :  "))
            #if id is invalid calls the display function and lets the user choose from them
            if (id_ > len(dict_) or id_ <= 0):
                print("Invalid id")
                print("Choose id from below")
                read.display_value()
                continue
            quantity =int(input("Enter the quantity of the product you wanna buy:  "))
            if (quantity <= 0):
                print("Invalid quantity")
                continue
    
            value =True    
            
            #calls the buy function pasing the id quantity and dictonary containg the product descrption 
            buy_value=buy_product(id_,quantity,dict_)
            
            #checks for any error occured after the function was runed
            if buy_value == 0:
                
                value =False
                print("give new quantity") 
                continue
                    
            else:
                print("Product bought sucessfully")
                
                while (value == True):
                    #runs until the function is true terminates if false
                    try:
                        userinput = input("Do you want to Buy more? Yes/no: ").lower()
                        if (userinput == "yes") :          
                            product_list.append(buy_value.copy())
                            buy(read.store_value)
                            return
                               
                        elif(userinput == "no") :
                            product_list.append(buy_value.copy())
                            name= input("Enter a Name:  ")
                            address= input("Enter your Address:  ")
                            if (len(product_list) != 0 ):
                                write.append_product_list_to_file(read.store_value)
                                write.generate_buy_invoice(name,address,product_list)
                            else:
                                print("No product in the list.")
                                print("No invoice genegrated")
                            return
                            
                    except ValueError:
                        #handels invalid input and loops untill desired value is inputed from user
                        print("Input either yes or no ")
                return
        except ValueError:
            #handels invalid input and loops untill desired value is inputed from user
            print("Invalid input")

      

   
sold_list=[]
#sell function
def sell(dict_):
    """
        This sell function handles the restocking of the products. It first takes the user input and cheks foe valid entry or not then according to the input it ask for inputs such as id and quantity and chekcs for any invalid entry and then displays a message for product 
        sold  and askes for name if no other products are required to the customer. Else if new products are added then this function ask for the inforamtion of the product.Then this function calls the append file and invoice generation function passing the required parameters. 
        Parameters: 
            dictonary of products(Dictonary) this dictonary contains the following values with a key from 1- 3 with values:
            Each values conatins :
                -ProductName (String) The name of the product
                -ProductManufactoror (String) The naame of the manufactoror of the products
                -ProductQuantity (INteger) Its the no of quantity of the product we have in our store.
                -ProductPrice (Integer) It's the price of the the Product.
                -Countryof Origin (String ) Its the country where the products was made in
        Return: Nothing
            But since return function is used it terminates this function and goes back to the loop which called this function.
        Raises: Value error
            If the user inputs invalid id or quantity less than 0 then it again asks for userinput. 
    """
    value = False
    while (value == False):
    #loop continus until the condition is true
        try:
            print("Enter 1 to sell new Products")
            print("Enter 2 to sell old products")
            print("Enter 3 to Return")
            user_value=int(input("Enter a number: "))
            if (user_value == 2):
                try:
                    id_ = int(input("Enter the id of the product you want to sell: "))
                    
                    if (id_ > len(dict_) or id_ <= 0):
                        
                        print("Invalid id")
                        print("Choose id from below")
                        
                        #displayes the product list and asks for id again
                        read.display_value()
                        continue
                    
                    quantity =int(input("Enter the quantity of the product you want to sell: "))
                    
                    if (quantity <= 0):
                        print("Invalid quantity")
                        continue
                    
                    value =True
                    
                    #calls the sell product function and passes dfferent paramenter as value
                    sell_value=sell_product(id_,quantity,dict_)
                    
                    if sell_value == 1:
                        print("Product sold")
                        
                        #stores the sold products which will be useful while generating invoice
                        sold_item=[dict_[id_]["Product name"],dict_[id_]["Product Manufacturer"],quantity,dict_[id_]["Price"]]
                        
                        #copies the content and immediately appends in the product_list
                        sold_list.append(sold_item.copy())
                        
                        while True:
                            #loops run untill false is obtained
                            userinput = input("Do you want to Sell more? Yes/no: ").lower()
                            
                            if userinput == "yes":
                                sell(read.store_value) 
                                break
                            
                            elif userinput == "no":
                                
                                name = input("Enter your name: ")
                                
                                #passes the parameters to generate sell invoice
                                write.generate_sell_invoice(name, sold_list)
                                write.append_product_list_to_file(read.store_value)
                                return
                                
                            else:
                            #handels invalid input and loops untill yes or no is wriiten from user 
                                print("Invalid input. Please enter 'yes' or 'no'")
                            
                except ValueError:
                    #handels invalid input and loops untill desired value is inputed from user
                    print("Invalid input recorded")
            elif(user_value == 1):
                
                #user inputs new product deatails
                id_=len(dict_)+1
                product_name=input("Enter product name: ")
                product_manufacotor=input("Enter product manufactoror: ")
                product_quantity=int(input("Enter product quantity: "))
                product_pricer=int(input("Enter product Cost Price: "))
                product_origin=input("Enter the country of origin: ")
                
                '''
                Stores the input into a list and passes the list as parameter
                to the sell producst function which appends the file and displays if any error is occured or if product is sold.
                '''
                new_product=[product_name,product_manufacotor,product_quantity,product_pricer*2,product_origin]
                sell_values=sell_products(id_,new_product,dict_)
                
                if sell_values == 1:
                    print("Product sold")
                    
                    #copies the content and immediately appends in the product_list 
                    sold_list.append(new_product.copy())
                    value=True
                    while (value == True):
                        userinput = input("Do you want to Sell more? Yes/no ").lower()
                        
                        if userinput == "yes":
                            sell(read.store_value) 
                            break
                        elif userinput == "no":
                            
                            name = input("Enter your name: ")
                            #calls the generate invoive function passing the name and product list as parameter
                            write.generate_sell_invoice(name, sold_list)
                            file_value=write.append_file(sold_list)
                            
                            if file_value == 1:
                                print("File has been apended with necessary changes")
                                return

                        else:
                            #handels invalid input and loops untill yes or no is wriiten from user
                            print("Invalid input. Please enter 'yes' or 'no' ")
            elif(user_value == 3):
                return
            else:
                print("invalid input")   
            
        except ValueError:
        #handels invalid input and loops untill desired value is inputed from user
            print("Invalid input")
