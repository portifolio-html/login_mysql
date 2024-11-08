from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "teste"

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/acesso", methods=["POST"])
def acesso():

    email = request.form.get("user")
    print(email)

    return render_template("teste.html")


if __name__ in "__main___":
    app.run(debug=True)