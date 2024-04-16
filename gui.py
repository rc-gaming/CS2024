import mysql.connector
import time


def curdate():
    date = str(time.localtime()[0]) + "-" + str(time.localtime()[1]) + "-" + str(time.localtime()[2])
    return date


obj = mysql.connector.connect(host="sql6.freesqldatabase.com", user="sql6699260", password="bXU4sMhC8x", database="sql6699260")
curobj = obj.cursor()


def category():
    print("****Categories available are:**** \n")
    a = "select distinct CATEGORY from main_table"
    curobj.execute(a)
    fetch = curobj.fetchall()
    for i in fetch:
        print(i[0])
    print("\n")
    inpCategory = input("Enter your category: ")
    print("\n")
    print("We have the following ", inpCategory, ":")
    print("\n")
    b = "select PRODUCT_NAME,PRICE from main_table where CATEGORY='{}'".format(inpCategory)
    curobj.execute(b)
    fetch = curobj.fetchall()
    for i in fetch:
        print(i[0], "~~~~~~~~~~~", "PRICE: ", i[1])

    print("~~~~~~~~~~~~~~~~~X~~~~~~~~~~~~~~~~~")


def product():
    a = "select PRODUCT_NAME,PRICE from main_table"
    curobj.execute(a)
    fetch = curobj.fetchall()
    obj.commit()

    for i in fetch:
        print(i[0], "~~~~~~~~~~~", "PRICE: ", i[1])

    print("~~~~~~~~~~~~~~~~~X~~~~~~~~~~~~~~~~~")


def brand():
    print("********** Brands available are : *********\n ")
    a = "SELECT DISTINCT brand_name from main_table"
    curobj.execute(a)
    fetch = curobj.fetchall()
    for i in fetch:
        print(i[0])
    print('\n')
    inpBrand = input("What brand are you looking for ?")
    print('\n')
    print("We have the following products available from", inpBrand, ":")
    print('\n')
    b = "select PRODUCT_NAME , PRICE from main_table where BRAND_NAME = '{}'".format(inpBrand)
    curobj.execute(b)
    fetch = curobj.fetchall()
    for i in fetch:
        print(i[0], "~~~~~~~~~~", "PRICE :", i[1])


print("~~~~~~~~~~~~~~~~~~~~X~~~~~~~~~~~~~~~~~~~~")


def order():
    inpContact = int(input("Enter your 10-digit phone number: "))
    inpOrder = input("What do you want to order? ")
    qty = "select QUANTITY from main_table where PRODUCT_NAME='{}'".format(inpOrder)
    curobj.execute(qty)
    fetch = curobj.fetchall()
    if fetch == 0:
        print("OUT OF STOCK!!!")
    else:
        product_id = "select PRODUCT_ID from main_table where PRODUCT_NAME='{}'".format(inpOrder)
        curobj.execute(product_id)
        fetch1 = curobj.fetchall()
    # For subtracting from main table:
    a = "update main_table set QUANTITY = QUANTITY-{} where PRODUCT_NAME='{}'".format(1, inpOrder)
    curobj.execute(a)

    obj.commit()
    # For adding details into order table:
    c = "insert into order_table(PRODUCT_ID,PRODUCT_NAME,CONTACT_DETAILS_OF_CUSTOMER, DATE_OF_DISPATCH) values({},'{}',{},'{}')".format(
        fetch[0][0], inpOrder, inpContact, curdate())
    curobj.execute(c)
    obj.commit()
    print("Your order has been placed.")


while True:
    print("WELCOME TO E-SHOP :) \n")
    print("Press 1 if you are looking for a category. ")
    print("Press 2 if you are looking for a product. ")
    print("Press 3 if you are looking for a brand. ")
    print("Press 4 if you want to place an order. \n")

    inpint = int(input("Enter your number: "))
    print("\n")
    if inpint == 1:
        category()
    elif inpint == 2:
        product()
    elif inpint == 3:
        brand()
    elif inpint == 4:
        order()
    else:
        print("ERROR!!!")
        print("Check your number.")
