usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "good" and passwordInput == "1234":
    print("Welcome to Good Smile Shop !")
    print("----------------------------")
    print("1. Pepsi ", 15, "THB")
    print("2. Coffee", 65, "THB")
    print("3. Coke  ", 16, "THB")
    print("4. Mango ", 30, "THB")
    print("----------------------------")
    productSelected = int(input("Please select your product : "))
    if productSelected == 1:
        quatitySelected = int(input("Quantity : "))
        total = 15*quatitySelected
        print("Total :", total, "THB")
        print("------------Thank you------------")
    elif productSelected == 2:
        quatitySelected = int(input("Quantity : "))
        total = 65*quatitySelected
        print("Total :", total, "THB")
        print("------------Thank you------------")
    elif productSelected == 3:
        quatitySelected = int(input("Quantity : "))
        total = 16*quatitySelected
        print("Total :", total, "THB")
        print("------------Thank you------------")
    elif productSelected == 4:
        quatitySelected = int(input("Quantity : "))
        total = 30*quatitySelected
        print("Total :", total, "THB")
        print("------------Thank you------------")
    else:
        print("Invalid product")
else:
    print("Invalid username or password")
