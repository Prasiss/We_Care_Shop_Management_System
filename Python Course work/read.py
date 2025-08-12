
#open the file  to read the text
file=open("Product_list.txt","r")

#reads thefile line by line
lines=file.readlines()
file.close()

#empty dictonary
store_value={}

for i in range(len(lines)):
    
    #replaces the space with null string
    values = lines[i].replace("\n","")
    
    #splits the data present in the array values with ','
    
    row_value = values.split(",")
    store_value[i+1] ={"Product name":row_value[0],
                     "Product Manufacturer":row_value[1],
                     "Quantity":int(row_value[2]),
                     "Price":int(row_value[3])*2,
                     "Country": (row_value[4])
    }
    

def display_value():
    """
        This function displays the products present in the text file in a tabluar form and ensure its readable format.
        Parameters Nothing
        Return Nothing
        But prints the data present in the store_value dictonary
        Raises: Nothing
    """
    #table heading
    print("SN\tProduct Name\t\tProduct Manufacturer\t\tQuantity\tPrice\t\tCountry")
    print("-" * 110)
    
    '''
    using the foreach loop in 2d ductonary to access the values presnt in that list
    and printing them in a tabular format
    
    '''
    for key in store_value.keys():
        id_=int(key)
        product_name=store_value[key]["Product name"]  
        Product_manufacturer=store_value[key]["Product Manufacturer"]
        Quantity=store_value[key]["Quantity"]
        price=store_value[key]["Price"]
        Country=store_value[key]["Country"]
        if (len(product_name) >= 15):
            print(id_,"\t",product_name,"\t",Product_manufacturer,"\t\t\t",Quantity,"\t\t",price,"\t\t",Country )
        else:
            print(id_,"\t",product_name,"\t\t",Product_manufacturer,"\t\t\t",Quantity,"\t\t",price,"\t\t",Country )
            
    
    print("-" * 110)
