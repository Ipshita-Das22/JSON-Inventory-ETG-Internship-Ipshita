import json

fd1= open("records.json","r")
text = fd1.read()
fd1.close()
inventory = json.loads(text)

fd2 = open("sales.json","r")
sale = fd2.read()
fd2.close()
sales = json.loads(sale)

user_choice = ""
while user_choice!='Q' and user_choice!='q':
    print("1. press 1 to Add items to Records")
    print("2. press 2 view items of Records")
    print("3. press 3 remove items of Records")
    print("4. press 4 to view the sales details")
    print("   press Q to exit :")
    user_choice=input("please enter your choice: ")

    if user_choice == '1':

        print("*************************")
        product = input("please enter the PRODUCT_I: ")
        name = input("please enter the NAME: ")
        brand = input("please enter the BRAND: ")
        stock = int(input("please enter the STOCK: "))
        quantity = input("please enter the QUANTITY: ")
        price = int(input("please enter the PRICE: "))

        inventory.update({product: {"name": name, "brand": brand, "stock": stock, "quantity": quantity, "price": price}})
        text1 = json.dumps(inventory)
        fd=open("records.json","w")
        fd.write(text)
        fd.close()
        print("ADDED SUCCESSFULLY")
        print("*************************")

    elif user_choice == '2':

        print("*************************")
        print(inventory)
        print("*************************")

    elif user_choice == '3':

        print("*************************")
        delete = input("Enter the product id to delete")
        if(delete in inventory.keys()):
            del inventory[delete]
        else:
            print("Please enter a valid PRODUCT_ID!!!")
        print("*************************")

    elif user_choice == '4':

        print("*************************")
        print(sales)
        print("*************************")

    elif user_choice == 'q' or user_choice=='Q':
        print("*************************")
        print("THANKYOU FOR USING THE SERVICE!!!!!!!")
        print("*************************")

    else:
        print("*************************")
        print("PLEASE ENTER VALID OPTION")
        print("*************************")