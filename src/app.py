'''
Tugas Besar 3 IF2211 Strategi Algoritma
Deadline Chatbot implemented with KMP String Matching Algorithm and Regular Expression
Created by:
            Rizky Anggita S Siregar     13519132
            Wilson Tandya               13519209

April 28, 2021

Institut Teknologi Bandung
2021
'''
from flask import Flask, render_template, request
from bot import tambah_task, lihat_task, lihat_deadline, ubah_deadline, task_selesai, temp_database, AUTO_INCREMENT, help_bot

app = Flask(__name__)
app.secret_key = 'secret key'


@app.route("/")
def home():
    return render_template("landing.html")

isichat = []
isichat.append("Halo Selamat Datang!")


@app.route("/dedbot", methods=["POST", "GET"])
def get_response():
    if request.method == "POST":
        global AUTO_INCREMENT
        userInput = request.form.get("userInput")
        isichat.append(userInput)
        status_tambah, response_tambah = tambah_task(userInput, AUTO_INCREMENT)
        status_lihat, response_lihat, status_regex = lihat_task(userInput, temp_database)
        status_dl, response_dl = lihat_deadline(userInput, temp_database)
        status_ubah, response_ubah = ubah_deadline(userInput, temp_database)
        status_selesai, response_selesai = task_selesai(userInput, temp_database)
        status_help, response_help = help_bot(userInput)
        
        if (status_tambah):
            isichat.append(response_tambah)
            AUTO_INCREMENT = AUTO_INCREMENT + 1
            with open("../test/database.txt", "w+") as f:
                f.write(str(AUTO_INCREMENT))
                f.write("\n") 
                for items in temp_database:
                    for item in items:
                        a = str(item)
                        f.write(a + " ")
                    f.write("\n")
            return render_template("dedbot.html", lendata=len(isichat), isichat = isichat)
            
        
        if (status_lihat):
            isichat.append(response_lihat)
            return render_template("dedbot.html", lendata=len(isichat), isichat = isichat)

        
        if (status_dl):
            isichat.append(response_dl)
            return render_template("dedbot.html", lendata=len(isichat), isichat = isichat)

        if (status_ubah):
            isichat.append(response_ubah)
            with open("../test/database.txt", "w+") as f:
                f.write(str(AUTO_INCREMENT))
                f.write("\n") 
                for items in temp_database:
                    for item in items:
                        a = str(item)
                        f.write(a + " ")
                    f.write("\n")
            return render_template("dedbot.html", lendata=len(isichat), isichat = isichat)

        if (status_selesai):
            isichat.append(response_selesai)
            with open("../test/database.txt", "w+") as f:
                f.write(str(AUTO_INCREMENT))
                f.write("\n") 
                for items in temp_database:
                    for item in items:
                        a = str(item)
                        f.write(a + " ")
                    f.write("\n")
            return render_template("dedbot.html", lendata=len(isichat), isichat = isichat)

        if (status_help):
            isichat.append(response_help)
            return render_template("dedbot.html", lendata=len(isichat), isichat = isichat)
        
        if (status_lihat == False):
            if (status_regex != []):
                if (status_regex[0] or status_regex[1] or status_regex[2] or status_regex[3]):
                    isichat.append("---Kosong---")
                    return render_template("dedbot.html", lendata=len(isichat), isichat = isichat)


        if (status_ubah == False):
            if(response_ubah != ""):
                isichat.append(response_ubah) 
                return render_template("dedbot.html", lendata=len(isichat), isichat = isichat)

        if (status_selesai == False):
            if (response_selesai != ""):
                isichat.append(response_selesai)
                return render_template("dedbot.html", lendata=len(isichat), isichat = isichat)

        if(status_dl == False):
            if(response_dl != ""):
                isichat.append(response_dl)
                return render_template("dedbot.html", lendata=len(isichat), isichat = isichat)

        isichat.append("Bot tidak mengenali pesanmu!")
        return render_template("dedbot.html", lendata=len(isichat), isichat = isichat)
    
    else:
        return render_template("dedbot.html", lendata=len(isichat), isichat=isichat)



if __name__ == "__main__":
    app.run()