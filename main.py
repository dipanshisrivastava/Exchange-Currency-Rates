from flask import Flask, request,render_template, url_for ,redirect
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/get_value', methods=['POST'])
def get_value():
    from_currency = str(request.form.get('fromcurrency'))
    to_currency = str(request.form.get('tocurrency'))
    print(from_currency)
    print(to_currency)
    if(from_currency == 'Select' or to_currency == 'Select'):
        return render_template('index.html', ans = 'Invalid input')
    if(from_currency != to_currency):
        amount = 1
        response = requests.get(
            f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
        ans = f"{response.json()['rates'][to_currency]}"
        print(ans)
        return render_template('index.html', ans = ans)
    else:
        return render_template('index.html', ans = 1)



# from_currency = str(
#     input("Enter in the currency you'd like to convert from: ")).upper()

# from_currency = str(
#     input("Enter in the currency you'd like to convert to: ")).upper()

# amount = 1

# response = requests.get(
#     f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

# print(
#     f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")

if __name__ == "__main__":
    app.run(debug=True)