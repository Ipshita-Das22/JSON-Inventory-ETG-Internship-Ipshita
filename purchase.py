#importing the json inventory elements
import json

#this is importing the inventory record
fd=open("records.json","r")
text = fd.read()
fd.close()

#importing the sales file
sj = open("sales.json","r")
rw = sj.read()
sj.close()

#converting sj file into dictionary
sjd = json.loads(rw)

#this is the inventory dictionary converted from string to dictionary
inventory = json.loads(text)

#list for collecting the items purchased
quan = []

#list for the products that are less in the inventory
order_prod = []

#variable for calculation of total
total = 0

#printing the inventory for proper view of products
print(text)
print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")


terminate = ""
#loop for taking n number of order until user wants
while terminate != 'N' and terminate != 'n':
    prod = input("Please Enter Product id: ")

    #now chwcking the conditions where the demanded quantity is available or not!
    if prod in inventory.keys(): #finding the product id in dictionary
            item_qty = int(input("Enter The Quantity: ")) #taking quantity for product
            if int(inventory[prod]["stock"]) >= item_qty:
                print(inventory[prod])
                purchase_data = [prod, inventory[prod]["name"], inventory[prod]["brand"], item_qty, int(inventory[prod]["price"]*item_qty)]
                quan.append(purchase_data)

            elif int(inventory[prod]["stock"]) <= 10:
                order_prod.append([prod,inventory[prod]["name"],inventory[prod]["brand"]])

            else:
                print("Entered amount of quantity is NOT available!!! we have", inventory[prod]["stock"],"available")

    else:
        print("Please Enter A Valid Product ID: ")

    terminate = input("DO YOU WANT TO PURCHASE MORE ITEMS : Y for YES and N for NO ")

#printing the bill
print("########################################################")
print("THANKYOU FOR PURCHASING PRODUCTS")
print("********************************************************")
print("your products are:")
print("prod id, ","  name, ","  brand  ,","   quantity, ", "  price")
print("--------------------------------------------------------")
#printing the products purchased and calculating total
for i in quan:
    print(i)
    total+= i[4]

print("********************************************************")
discount = input("Any sale !!... Y for YES and N for NO... ")

if discount == 'Y' or discount =='y':
    dis_amount = int(input("Enter the OFF Percent in number.. "))
    new_price = total - ((dis_amount/100)*total)
    print("TOTAL BILL: ", new_price,"*********")
else:
    print("TOTAL BILL: ",total,"*********")
print("########################################################")
print("Thankyou visit again!!!!!")

#now again updating the stocks that are purchased
for i in quan:
    inventory[str(i[0])]["stock"]-= i[3]
print(inventory)

new_inventory = json.dumps(inventory)
fd1= open("records.json","w")
fd1.write(new_inventory)
fd1.close()
print("inventory updated!!!!")



#Now after the successful purchasing we are creating sales.json which will keep a record of the sales made!!

for i in range(0,len(quan)):
    if quan[i][0] in sjd.keys():
        s={quan[i][0]:{"name":quan[i][1],"total_product_selled":sjd[quan[i][0]][ "total_product_selled"]+quan[i][3],"total_cost":sjd[quan[i][0]]["total_cost"]+quan[i][4]}}
        sjd.update(s)
    else:
        s = {quan[i][0]: {"name": quan[i][1], "total_product_selled": quan[i][3], "total_cost": quan[i][4]}}
        sjd.update(s)
netsale = json.dumps(sjd)

sa = open("sales.json","w")
sa.write(netsale)
sa.close()
