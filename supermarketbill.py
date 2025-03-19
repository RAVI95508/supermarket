'supermarket dill'

import requests
def Bill_of_supermarket():
 url="http://demo8970206.mockable.io/supermarket"
 response=requests.get(url)
 print(response.status_code)
 if response.status_code==200:
      get_data=response.json()  
      option=int(input("For list of items press 1 and 0 of exit:"))
      if option==1:  
           products1=get_data["items"]
           print(products1)
           for i in range(len(products1)):
             inp1=int(input("if you want to buy press 1 or 2 for exit:"))           
             if inp1==2:
                return
             if inp1==1:
                print(products1)
                item=input("Enter the items :")
                if item in products1.keys():
                  print("ok we have that item")
                  qunatity=int(input("Enter the quantity:"))                                   
                  price=qunatity*(products1[item])
                  gst=5                                                                        
                  finalprice=gst+price 
                  print(f"you bill is,{finalprice}")                                                  
                else:
                   print("sorry you enter item is not available")              
             else:
                  print("sorry item is not available")       
                  inp=input(" can i bill:")  
                  if inp=="yes":
                    pass
                    if finalprice !=0:
                     bill+=finalprice
                     print(f"final bill is{bill}")
                     print("bill is print")
      else:
         print("wrong number")                       
Bill_of_supermarket()    
        