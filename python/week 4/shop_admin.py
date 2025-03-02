apple = {"name" : "apple" , "price" : 12000 , "inventory" : 50}
orange = {"name" : "orange" , "price" : 15000 , "inventory" : 30}
potato = {"name" : "potato" , "price" : 11000 , "inventory" : 40}
banana = {"name" : "banana" , "price" : 20000 , "inventory" : 10}
mango = {"name" : "mango" , "price" : 30000 , "inventory" : 5}
pineapple = {"name" : "pineapple" , "price" : 25000 , "inventory" : 5}
products = [ apple , orange  , potato  , banana  , mango  , pineapple ]

def add():
    name = input("enter the name of product : ")
    price = int(input("enter the price of product : "))
    inventory = int(input("enter the existing count of product : "))
    globals()[name] = {"name" : name, "price" : price , "inventory" : inventory}
    products.append(globals()[name])

def search():
    searchDic = input("enter the item you looking for : ")
    for product in products:
        if product["name"] == searchDic :
            print(f'''the product found and the info is :
name : {product["name"]} price : {product["price"]} and the inventory has {product["inventory"]} of them ''')
            break
        else:
            print("did not found")
        
def delete():
    deleteDic = input("which product do you want to delete : ")
    for product in products:
        if product["name"] == deleteDic :
            products.remove(product)
            print("now the item seccessfully deleted")
            break

def change():
    changeDic = input("which product do you want to change : ")
    for product in products:
        if product["name"] == changeDic :
            print("if do you want to change any value enter the new value else enter the previos value")
            Nname = input(f"now the name of the product is {product["name"]} ")
            product["name"] = Nname
            Nprice = int(input(f"now the price of the product is {product["price"]} "))
            product["price"] = Nprice
            Ninventory = int(input(f"now the existing count of the product is {product["inventory"]} "))
            product["inventory"] = Ninventory

flag = True
while(flag):
    #print(f"in this shop we have {products}")
    print("----------------------------------------------------")
    print('''1. add a new product
2. searching for a product
3. delete a existing product
4. changing the values of a product
5. Exit ''')
    menu = int (input("what do you want to do ? "))
    print("----------------------------------------------------")

    if menu == 1:
        add()
    elif menu == 2 : 
        search()
    elif menu == 3:
        delete()
    elif menu == 4:
        change()
    elif menu == 5 :
        flag = False
    else :
        print("try again")
