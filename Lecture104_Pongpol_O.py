class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to", self.name, self.lastName, "'s cart")

customer1 = Customer() # สร้าง object มาจาก Class Customer
customer1.name = "Chatchawan"
customer1.lastName = "Siri"
customer1.age = 26
customer1.addCart()

customer2 = Customer()
customer2.name = "Poonpon"
customer2.lastName = "Aba"
customer2.age = 22
customer2.addCart()

customer3 = Customer()
customer3.name = "Kittipong"
customer3.lastName = "Kongkong"
customer3.age = 21
customer3.addCart()

customer4 = Customer()
customer4.name = "Noppon"
customer4.lastName = "Chulalongkorn"
customer4.age = 20
customer4.addCart()