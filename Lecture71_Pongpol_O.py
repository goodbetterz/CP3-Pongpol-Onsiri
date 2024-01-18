menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("My Food".center(20, "-"))
    for i in range(len(menuList)):
        print(menuList[i], priceList[i])
        totalPrice += priceList[i]
    print("Total :", totalPrice)

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Please Enter Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()