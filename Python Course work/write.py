'''
imprting operation to run the function present in the operation file
importing inbuilt datatime which gives us the value to date
and other necessary details if we need to acess such as second time, milisecond, minute 

'''


import datetime
import operation
"""
This function handles the overwrite of the dict values to the text file. It takes a dictonary and amend the deatils present in the dictonary to the product_list.txt

Parameters:
    Product_list (dict) is a list of dictonary that contains a key value pair of id and values. The value contain the product list as mentioned below:
    Each values conatins :
    -ProductName (String) The name of the product
    -ProductManufactoror (String) The naame of the manufactoror of the products
    -ProductQuantity (INteger) Its the no of quantity of the product we have in our store.
    -ProductPrice (Integer) It's the price of the the Product.
    -Countryof Origin (String ) Its the country where the products was made in
Returns None 
    This function retuns nothing it only writes in the text file.
"""
def append_product_list_to_file(dict_):
    #opens file in write mode
    file=open("Product_list.txt","w")
    
    for value in dict_.values():
        
        product_name = str(value["Product name"])
        product_manufacturer = str(value["Product Manufacturer"])
        product_quantity = str(value["Quantity"])            
        product_price = str(int(value["Price"]/2)) #dividing the quantity by 2 so the cost price is displayed in the text file.
        product_country = str(value["Country"])
        #write into the file 
        file.write(product_name+",")
        file.write(product_manufacturer+",")
        file.write(product_quantity+",")
        file.write(product_price+",")
        file.write(product_country)
        file.write("\n")
    
    file.close()     
            
"""
This functions take a list as a parameter and appends the file to the new producst that were sold by the user. This function appends the value to the existing file.
Parameters: 
    product_list is a list of new products which were entered by the user. The list contains the following items:
    -ProductName (String) The name of the product
    -ProductManufactoror (String) The naame of the manufactoror of the products
    -ProductQuantity (Integer) Its the no of quantity of the product we have in our store.
    -ProductPrice (Integer) It's the price of the the Product.
    -Countryof Origin (String ) Its the country where the products was made in

Returns 1
    This function returns 1 when the data has been added to  the text file.
"""
def append_file(product_list):
    file=open("Product_list.txt","a")
    for row in product_list:
        for value in row:
            file.write(str(value)+",")
        file.write("\n")
    file.close()
    return 1



"""
This functions take a name,address and a product_list as a parameter and generates invoice for the name and address of the user. The Product list contains the product which was sold to the customer 
and contains other deatils as well. this function also prints the invoice of the product sold to the customer which includes the price , name of the product quantity , date and at last discount as well.
This function also writes into the text file name buyinvioice.txt.The invoice I have generated  is wrriting into the file in the same function so this function handles 
two thing at the same time.This function also chekes for any free products the customer gets when he bought quantity form our store. so when we generae invoice the customer gets a discount worth the value 
of the free products that he/she buys from our store.This function also generates diferent invoice everytime this file is called.

Parameters:
    The parameters are name, address of the user and a 2d list which contains the following values.
    
    -ProductName (String) The name of the product
    -ProductManufactoror (String) The naame of the manufactoror of the products
    -ProductQuantity (Integer) Its the no of quantity of the product we have in our store.
    -ProductPrice (Integer) It's the price of the the Product.
    

Returns Nothing
   
"""

def generate_buy_invoice(name,address,list_):
    #usesing dataand time function to get the data of transaction
    filename="BuyInvoice_"+name+"_"+address
    year=datetime.datetime.now().year
    month =datetime.datetime.now().month
    day=datetime.datetime.now().day
    Date=str(year)+ "|" + str(month) +"|"+ str(day) # string Contatination
    print(" ")
    
    print("Bill For")
    print(name)
    print(address)
    
    print(" "*117,"INV-2025")
    print(" "*60,"Invoice")
    print(" "*60,"We care Store ")
    print(" "*117,Date)
    print("-"*130)
    print(" ")
    
    print("Sn.\tName of Product\t\tProduct Manufacturer\t\tQuantity\tUnit Price\tFree Product\t\tTotal") 
    Sn=1 
    total=0
    total_discount=0
    grand_total=0
    
    #if user adds two same unit in different portion we merge them
    index = 0
    while index < len(list_):
        j = index + 1
        while j < len(list_):
            if list_[index][0] == list_[j][0] and list_[index][1] == list_[index][1]:
                list_[index][2] += list_[j][2]  # Merge quantity and puts them in one
                #deleting the array of particular quantity as they ordered the same value twice
                del list_[j]  
            else:
                j = j + 1
        index = index + 1
    #printting the invoioce in the sell by accesing particular value 
    for product in list_:
        
        product_name=product[0]
        product_manufacturer=product[1]
        product_quantity=product[2]
        product_price=product[3]
        #calling freeproduct function to check for any free products that the usergets after buying the products.
        free_product=operation.free_product(int(product_quantity))
        if  (free_product == 0) :
            discount=0
        else:
            discount = free_product * product_price
            
        sub_total_price=product_price*product_quantity
        total += sub_total_price
        total_discount = total_discount+discount
        if len(product_name) >= 15:
            print(Sn, "\t", product_name, "\t", product_manufacturer, "\t\t\t", product_quantity, "\t\t", "$", product_price, "\t\t", free_product, "\t\t", "$", sub_total_price)
        else:                
            print(Sn, "\t", product_name, "\t\t", product_manufacturer, "\t\t\t", product_quantity, "\t\t", "$", product_price, "\t\t\t", free_product, "\t\t", "$", sub_total_price)
            
        Sn= Sn+1
    
    grand_total= total-total_discount     
    print("-"*130)
    print(" "*100, "Sub Total:        ","$",total)
    print(" "*100,"-" *30)
    print(" "*100, "Discount:         ","$",total_discount)
    print(" "*100,"-" *30)
    print(" "*100, "Grand Total:      ","$",grand_total)
    
    
    #opening file in write mode
    file = open(filename, "w")
    file.write("Bill For\n")
    
    file.write(name + "\n")
    file.write(address+"\n")
    
    file.write(" " * 117 + "INV-2025\n")
    file.write(" " * 60 + "We Care Store\n")
    file.write(" " * 60 + "Invoice\n")
    file.write(" " * 117 + Date +"\n")
    file.write("-" * 130 + "\n")
    file.write("\n")
    file.write("Sn.\tName of Product\t\tProduct Manufacturer\t\tQuantity\tUnit Price\tFree Product\tTotal\n")
        
    Sn=1 
    for product in list_:
        #accesing the varaiables
        product_name=product[0]
        product_manufacturer=product[1]
        product_quantity=product[2]
        product_price=product[3]
        
        free_product=operation.free_product(product_quantity)
        if  (free_product == 0) :
            discount=0
        else:
            discount = free_product * product_price
            
        sub_total_price=product_price*product_quantity
        
         
        #converting the data into string as text file only accepts str value
        product_description = (str(Sn) + "\t" + product_name + "\t\t\t" + product_manufacturer + "\t\t\t\t" +str(product_quantity) + "\t\t\t\t" +"$ " + str(product_price) + "\t\t\t" + str(free_product) + "\t\t" +"$" + str(sub_total_price) + "\n")
        
        file.write(product_description)
        file.write("\n")

        Sn = Sn+1
        
    
    file.write("-" * 130 + "\n")
    file.write(" " * 100 + "Sub Total:        $" + str(total) + "\n")
    file.write(" " * 100 + "-" * 30 + "\n")
    file.write(" " * 100 + "Discount:         $" + str(discount) + "\n")
    file.write(" " * 100 + "-" * 30 + "\n")
    file.write(" " * 100 + "Grand Total:      $" + str(grand_total) + "\n")
    
    #close the file
    file.close()
   
   


 

def generate_sell_invoice(name,list_):
    """
        This functions take a name and a product_list as a parameter and generates invoice for the name of the seller. The Product list contains the product which was sold to the us by the middle man. 
        and contains other deatils as well. This function also writes into the text file name sellinvioice.txt.The invoice I have generated  is wrriting into the file in the same function so this function handles 
        two thing at the same time.

    Parameters:
        The parameters are name of the seller and a 2d list which contains the following values.
        
        -ProductName (String) The name of the product
        -ProductManufactoror (String) The naame of the manufactoror of the products
        -ProductQuantity (Integer) Its the no of quantity of the product we have in our store.
        -ProductPrice (Integer) It's the price of the the Product.
        
    Returns: Nothing
        This function only writes into the file and print the invoice
    """
    
    filename="SellInvoice_"+name
    taxable_amount=0  
    year=datetime.datetime.now().year
    month =datetime.datetime.now().month
    day=datetime.datetime.now().day
    Date=str(year)+ "|" + str(month) +"|"+ str(day) #string Concatination
    
    #if user adds two same unit in different portion we merge them
    index = 0
    while index < len(list_):
        j = index + 1
        while j < len(list_):
            if list_[index][0] == list_[j][0] and list_[index][1] == list_[index][1]:
                list_[index][2] += list_[j][2]  # Merge quantity and puts them in one
                #deleting the array of particular quantity as they ordered the same value twice
                del list_[j]  
            else:
                j = j + 1
        index = index + 1
        
    #printing the invoice
    print("Bill For")
    print(name)
    
    print(" "*117,"INV-2025")
    print(" "*60,"We Care Store")
    print(" "*60,"Invoice")
    print(" "*117,Date)
    print("-"*130)
    print(" ")
    
    print("Sn.\tName of Product\t\tProduct Manufacturer\t\tQuantity\t\tUnit Price\tTotal") 
    Sn=1 
    
    for product in list_:
        #accesing the varaiables
        product_name=product[0]
        product_manufacturer=product[1]
        product_quantity=product[2]
        product_price=(product[3])/2
        
        sub_total_price=product_price*product_quantity
        taxable_amount = sub_total_price + taxable_amount

        print(Sn,"\t",product_name,"\t\t",product_manufacturer,"\t\t\t",product_quantity,"\t\t","$ ",product_price,"\t", "$",sub_total_price)
        Sn= Sn+1
        
    tax=taxable_amount * 0.13
    total=taxable_amount+tax        
    print("-"*130)
    print(" "*100, "Sub Total:      ","$",taxable_amount)
    print(" "*100,"-" *30)
        
    print(" "*100, "Tax:            ","$",tax)
    print(" "*100,"-" *30)
    print(" "*100, "Total:          ","$",total)
    
    #opening the file with the usersname and writting the invoice there
    file = open(filename, "w")
    file.write("Bill For\n")
    
    file.write(name + "\n")
    
    file.write(" " * 80 + "INV-2025\n")
    file.write(" " * 40 + "We Care Store\n")
    file.write(" " * 40 + "Invoice\n")
    file.write(" " * 80 + Date +"\n")
    file.write("-" * 90 + "\n")
    file.write("\n")
    file.write("Sn.\tName of Product\tProduct Manufacturer\tQuantity\tUnit Price\tTotal\n")
    file.write("-" * 90 + "\n")
    Sn=1 
    '''
    writting in the file in tha same format we printed the invoice
    so that there is only minimal difference in both of them.
    '''
    for product in list_:
        
        product_name=product[0]
        product_manufacturer=product[1]
        product_quantity=product[2]
        product_price=(product[3])/2
        
        sub_total_price=product_price*product_quantity
        taxable_amount = sub_total_price + taxable_amount  
        #converting the data into string as text file only accepts str value and aliging the values with the help to \t 
        product_description=(str(Sn)+"\t"+ product_name + "\t"+ product_manufacturer + "\t\t" + str(product_quantity) + "\t\t" + "$ " + str(product_price) + "\t" + "$" + str(sub_total_price) +"\n") 
        file.write("\n")
        file.write(product_description)
        
        Sn = Sn+1
    
    file.write("-" * 90 + "\n")
    file.write(" " * 60 + "Sub Total:      $" + str(taxable_amount) + "\n")
    file.write(" " * 60 + "-" * 30 + "\n")
    file.write(" " * 60 + "Tax:            $" + str(tax) + "\n")
    file.write(" " * 60 + "-" * 30 + "\n")
    file.write(" " * 60 + "Total:          $" + str(total) + "\n")

    #close the file
    file.close()
