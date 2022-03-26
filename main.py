from requests import get
from pprint import PrettyPrinter


BASE_URL = "https://free.currconv.com/"
API_KEY = "4958107eafdc0bf71c1f"

printer = PrettyPrinter()

def get_currencies():
    end_point = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + end_point
    data = get(url).json()["results"]

    data = list(data.items())
    data.sort()
    return data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency["currencyName"]
        _id = currency["id"]
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
    end_point = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + end_point
    data = get(url).json()

    if len(data) == 0:
        print("Invalid currencies")
        return

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")
    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount")
        return

    converted_amount = amount * rate

    print(f"{amount} {currency1} = {converted_amount} {currency2}")
    return converted_amount

def main():
    currencies = get_currencies()

    print("Welcome to the currency converter.\n")

    while True:
        print("Commands:")
        print("List - lists the different currencies.")
        print("Convert - convert from  one currency to another.")
        print("Rate - get the exchange rate of two currencies.")
        print("Q - to quit the app")
        command = input("\nEnter your command: ").lower()

        if command == "q":
            break

        elif command == "list":
            print_currencies(currencies)
            print("\n")

        elif command == "convert":
            currency1 = input("Input currency you want to convert: ").upper()
            amount = input("Input amount which you want to convert: ")
            currency2 = input("Input currency you want to get: ").upper()

            convert(currency1, currency2, amount)
            print("\n")

        elif command == "rate":
            currency1 = input("Input currency 1: ").upper()
            currency2 = input("Input currency 2: ").upper()
            exchange_rate(currency1, currency2)
            print("\n")

if __name__ == "__main__":
    main()
