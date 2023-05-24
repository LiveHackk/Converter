import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://uzraudziba.bank.lv/en/market/convert?amount={amount}&from={from_currency}&to={to_currency}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        converted_amount = data["converted_amount"]
        print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
    else:
        print("Error converting currency.")

convert_currency(200, "USD", "EUR")

convert_currency(100, "GBP", "USD")
