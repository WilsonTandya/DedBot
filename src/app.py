from flask import Flask, render_template, request
# from regex import *
from bot import tambah_task, lihat_task, lihat_deadline, ubah_deadline, task_selesai

app = Flask(__name__)
app.secret_key = 'secret key'


@app.route("/")
def home():
    return ("HELLO WORLD!")

isichat = []
isichat.append("Halo Selamat Datang!")

from bot import temp_database
from bot import AUTO_INCREMENT


@app.route("/text", methods=["POST", "GET"])
def get_response():
    if request.method == "POST":
        global AUTO_INCREMENT
        userInput = request.form.get("saya")
        print(userInput)
        isichat.append(userInput)
        status_tambah, response_tambah = tambah_task(userInput, AUTO_INCREMENT)
        status_lihat, response_lihat, status_regex = lihat_task(userInput, temp_database)
        status_dl, response_dl = lihat_deadline(userInput, temp_database)
        status_ubah, response_ubah = ubah_deadline(userInput, temp_database)
        status_selesai, response_selesai = task_selesai(userInput, temp_database)
        
        print(temp_database)
        print("GW segini: " + str(AUTO_INCREMENT))
        
        if (status_tambah):
            isichat.append(response_tambah)
            AUTO_INCREMENT = AUTO_INCREMENT + 1
            with open("database.txt", "w+") as f:
                f.write(str(AUTO_INCREMENT))
                f.write("\n") 
                for items in temp_database:
                    for item in items:
                        a = str(item)
                        f.write(a + " ")
                    f.write("\n")
            return render_template("home.html", lendata=len(isichat), isichat = isichat)
            
        
        if (status_lihat):
            isichat.append(response_lihat)
            return render_template("home.html", lendata=len(isichat), isichat = isichat)

        
        if (status_dl):
            isichat.append(response_dl)
            return render_template("home.html", lendata=len(isichat), isichat = isichat)

        if (status_ubah):
            isichat.append(response_ubah)
            with open("database.txt", "w+") as f:
                f.write(str(AUTO_INCREMENT))
                f.write("\n") 
                for items in temp_database:
                    for item in items:
                        a = str(item)
                        f.write(a + " ")
                    f.write("\n")
            return render_template("home.html", lendata=len(isichat), isichat = isichat)

        if (status_selesai):
            isichat.append(response_selesai)
            with open("database.txt", "w+") as f:
                f.write(str(AUTO_INCREMENT))
                f.write("\n") 
                for items in temp_database:
                    for item in items:
                        a = str(item)
                        f.write(a + " ")
                    f.write("\n")
            return render_template("home.html", lendata=len(isichat), isichat = isichat)

        if (status_lihat == False):
            if (status_regex != []):
                if (status_regex[0] or status_regex[1] or status_regex[2] or status_regex[3]):
                    isichat.append("---Kosong---")
                    return render_template("home.html", lendata=len(isichat), isichat = isichat)


        if (status_ubah == False):
            if(response_ubah != ""):
                isichat.append(response_ubah) 
                return render_template("home.html", lendata=len(isichat), isichat = isichat)

        if (status_selesai == False):
            if (response_selesai != ""):
                isichat.append(response_selesai)
                return render_template("home.html", lendata=len(isichat), isichat = isichat)

        if(status_dl == False):
            if(response_dl != ""):
                isichat.append(response_dl)
                return render_template("home.html", lendata=len(isichat), isichat = isichat)

        isichat.append("Bot tidak mengenali pesanmu!")
        
        return render_template("home.html", lendata=len(isichat), isichat = isichat)
    
    else:
        print("TESTT")
        return render_template("home.html", lendata=len(isichat), isichat=isichat)



if __name__ == "__main__":
    app.run()