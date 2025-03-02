import crud

products = list()

products = crud.load_db()

while True:
    try:
        print("1.add product")
        print("2.find product")
        print("3.remove product")
        print("4.update product")
        print("5.save database")
        print("6.show database")
        print("7.exit")
        print("-----------------------")
        menu = int(input("what do you want to do :"))

        match menu:
            case 1:

                products = crud.add_product(products)
            case 2:

                crud.find_product(products)
            case 3:

                crud.remove_product(products)
            case 4:

                products = crud.update_product(products)
            case 5:

                crud.save_db(products)
            case 6:

                crud.show_db(products)
            case 7:

                print("exiting...")
                break

            case _:
                print("invalid input...\n")
    except:
        print("something went wrong, try again...\n")