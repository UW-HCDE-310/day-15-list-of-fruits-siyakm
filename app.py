from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]
    #ORIGINAL
    #return render_template("index.html", fruits=fruits)

    #FRUITS THAT START WITH "O"
    # fruits = [fruit for fruit in fruits if fruit["name"].startswith("o")]
    # return render_template("index.html", fruits=fruits)

    #FRUITS THAT YOU HAVE MORE THAN 3 OF
    fruits = [fruit for fruit in fruits if fruit["quantity"] > 3]
    return render_template("index.html", fruits=fruits)