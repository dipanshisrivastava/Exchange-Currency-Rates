import requests

def show_value(from_currency, to_currency):    
    if(from_currency == 'Select' or to_currency == 'Select'):
        return 'Invalid input'
    if(from_currency != to_currency):
        amount = 1
        response = requests.get(
            f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
        ans = f"{response.json()['rates'][to_currency]}"
        return ans
    else:
        return 1
