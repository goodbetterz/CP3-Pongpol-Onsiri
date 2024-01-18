systemMenu = {"Apple": 20, "Orange": 25, "Mango": 30, "Watermelon": 35}
menuList = []

def showBill():
    totalPrice = 0
    print("My Food".center(20, "-"))
    for name, price in menuList:
        print(name, price)
        totalPrice += price
    print("Total :", totalPrice)

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

showBill()