from flask import Flask, request,render_template, url_for ,redirect
import businesslayer as bl

app = Flask(__name__)

#home page
@app.route("/")
def home():
    return render_template("index.html")

# function collects values from both the dropdowns and sends the values to "show_value" function in businesslayer.py file
# Now result contain final converted value, which is then send to index.html 
@app.route('/get_value', methods=['POST'])
def get_value():
    from_currency = str(request.form.get('fromcurrency'))
    to_currency = str(request.form.get('tocurrency'))
    amount = "1"
    min_val, max_val = bl.call_from_main(from_currency, to_currency, amount)
    return render_template('index.html', minimum = min_val, maximum = max_val)

if __name__ == "__main__":
    app.run(debug=True)