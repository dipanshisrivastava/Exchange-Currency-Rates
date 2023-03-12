from flask import Flask, request,render_template, url_for ,redirect
import businesslayer as bl

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/get_value', methods=['POST'])
def get_value():
    from_currency = str(request.form.get('fromcurrency'))
    to_currency = str(request.form.get('tocurrency'))
    result = bl.show_value(from_currency, to_currency)
    return render_template('index.html', ans = result)

if __name__ == "__main__":
    app.run(debug=True)