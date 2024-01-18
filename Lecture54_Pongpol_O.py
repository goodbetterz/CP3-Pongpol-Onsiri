def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Invalid username or password")
    
def showMenu():
    print("------Good Smile Shop------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print(vatCalculate(int(input("Price (THB) : "))))
    elif userSelected == 2:
        print(priceCalculate())

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat/100)
    return result

def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

login()