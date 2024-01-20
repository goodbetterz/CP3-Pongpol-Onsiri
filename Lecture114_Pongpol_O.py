from currency_converter import CurrencyConverter
from datetime import date

print("Currency Converter and Compare Historical Result".center(66, "-"))

def currency_convert():
    currency_from = input("Enter currency you want to convert from : ").upper()
    currency_to = input("Enter currency you want to convert to : ").upper()
    amount = float(input("Enter amount you want to convert : "))

    present_result_converter = CurrencyConverter()
    present_result = round(present_result_converter.convert(amount, currency_from, currency_to), 2)
    print(f"Result : {amount} {currency_from} = {present_result} {currency_to}")

    print("------------------------------------------------------------")

    select = input("Would you like to compare to historical result ? (yes or no) : ").lower()
    if select == "yes":
        return compare_historical_result(currency_from, currency_to, amount, present_result)
    else:
        print("Thank you for using this program".center(66, "-"))
    
def compare_historical_result(currency_from, currency_to, amount, present_result):
    historical_year = int(input("Enter historical year you want to compare (2022-2023) : "))
    historical_month = int(input("Enter historical month you want to compare : "))
    historical_date = int(input("Enter historical date you want to compare : "))

    historical_day = date(historical_year, historical_month, historical_date)

    historical_result_converter = CurrencyConverter()
    historical_result = round(historical_result_converter.convert(amount, currency_from, currency_to, historical_day), 2)

    print("------------------------------------------------------------")

    print(f"Historical result ({historical_day}) : {amount} {currency_from} = {historical_result} {currency_to}")

    if present_result > historical_result:
        print(f"Present result is higher than historical result = {round((present_result - historical_result), 2)} {currency_to}")
        print("Thank you for using this program".center(66, "-"))
    elif present_result < historical_result:
        print(f"Present result is lower than histocical result = {round((historical_result - present_result), 2)} {currency_to}")
        print("Thank you for using this program".center(66, "-"))
    else:
        print("Present result is same as historical result")
        print("Thank you for using this program".center(66, "-"))

currency_convert()