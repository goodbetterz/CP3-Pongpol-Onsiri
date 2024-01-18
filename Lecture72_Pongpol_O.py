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
        menuPrice = int(input("Please Enter Price : "))
        menuList.append([menuName, menuPrice])

showBill()