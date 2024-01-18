def vatCalculate(price):
    vat = 7
    result = price + (price * vat/100)
    return result

priceInput = int(input("Price : "))
print(vatCalculate(priceInput))