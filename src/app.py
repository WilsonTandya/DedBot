from flask import Flask, render_template, request
from regex import *

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


temp_database = []
def tambah_task(kalimat):
    tanggal = regex_tanggal(kalimat)
    task = regex_katapenting(kalimat)
    kode_kuliah = regex_kodekuliah(kalimat)
    topik = regex_topik(kalimat)

    if (tanggal == "" or task == "" or kode_kuliah == "" or topik == ""):
        return False
    
    # Kalimat valid, masukkan ke database
    ID = len(temp_database+1)
    new_data = []
    new_data.append("ID:" + ID)
    new_data.append(tanggal)
    new_data.append(task)
    new_data.append(kode_kuliah)
    new_data.append(topik)
    temp_database.append(tambah_task)
    return True

if __name__ == "__main__":
    app.run()