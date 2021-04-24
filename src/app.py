from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'secret key'


@app.route("/")
def home():
    return ("HELLO WORLD!")

isichat = []
isichat.append("Halo Selamat Datang!")
@app.route("/text", methods=["POST", "GET"])
def get_response():
    if request.method == "POST":
        userInput = request.form.get("saya")
        isichat.append(userInput)
        # Olah userInput pake fungsi chatbot nya
        isichat.append("Respons Chatbot!")
        # return hasil dari chatbotnya
    # userTxt = request.args.get("msg")
        return render_template("home.html", lendata=len(isichat), isichat = isichat)
    else:
        print("TESTT")
        return render_template("home.html", lendata=len(isichat), isichat=isichat)


if __name__ == "__main__":
    app.run()