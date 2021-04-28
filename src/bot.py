from regex import regex_katapenting, regex_kodekuliah, regex_tanggal, regex_topik, regex_lihattask, regex_get_nTask, regex_tugas
from KMP import KMP
from function import konvert_tanggal, data_db_to_String
import datetime

AUTO_INCREMENT = 0

temp_database = []

i = 0
with open("../test/database.txt", "r") as f:
    for deadline in f.readlines():
        if i==0 :
            AUTO_INCREMENT = int(deadline[0].rstrip("\n"))
            i += 1
        else:  
            tanggal = regex_tanggal(deadline)
            task = regex_katapenting(deadline)
            kode_kuliah = regex_kodekuliah(deadline)
            topik = regex_topik(deadline)
            new_data = []
            new_data.append(int(deadline.split(" ")[0]))
            new_data.append(tanggal)
            new_data.append(task)
            new_data.append(kode_kuliah)
            new_data.append(topik)
            temp_database.append(new_data)

def tambah_task(kalimat, AUTO_INCREMENT):
    # global AUTO_INCREMENT
    tanggal = regex_tanggal(kalimat)
    task = regex_katapenting(kalimat)
    kode_kuliah = regex_kodekuliah(kalimat)
    topik = regex_topik(kalimat)

    if (tanggal == "" or task == "" or kode_kuliah == "" or topik == ""):
        return False, ""
    
    # Kalimat valid, masukkan ke database
    ID = AUTO_INCREMENT + 1
    new_data = []
    new_data.append(ID)
    new_data.append(tanggal)
    new_data.append(task)
    new_data.append(kode_kuliah)
    new_data.append(topik)
    temp_database.append(new_data)
    # AUTO_INCREMENT += 1
    response = "[TASK BERHASIL DICATAT]\n"
    response += "(ID: " + str(ID) + ") - " + (tanggal.upper()) + " - " + task.upper() + " - " + kode_kuliah.upper() + " - " + topik.upper()
    response += "\n" 
    return True, response

def lihat_task(kalimat, database):
    response = ""
    if "deadline" not in kalimat.lower() :
        return False, response, []

    text = kalimat.lower()
    a = text.split()
    #  MASIH PERLU PERBAIKAN, RADA ANEH
    # Keywordnya adalah "semua [kata_penting] deadline yang dimiliki sejauh ini"
    keyword_seluruh = ["deadline", "semua", "dimiliki", "sejauh", "ini"]
    count = 0
    for pat in keyword_seluruh:
        for word in a:
            if (KMP(pat, word)):
                count += 1
    
    response += "[DAFTAR DEADLINE]\n"
    if (count >= 4):
        task = regex_katapenting(text)
        if (task != ""):
            for deadline in temp_database:
                if (deadline[2]==task):
                   response += data_db_to_String(deadline) + "\n"
        else:
            for deadline in temp_database:
                response += data_db_to_String(deadline) + "\n"
        return True, response, []
    
    # Kemungkinan lain
    status, extract = regex_lihattask(text)
    task = regex_katapenting(text)
    end = False
    # Periode tertentu Tgl1 <= tgl_deadline <= tgl2
    if (status[0]):
        extracted = extract[0].rsplit(" sampai ")
        tgl_awal = extracted[0]
        tgl_akhir = extracted[1]
        tahun1, bulan1, hari1 = konvert_tanggal(tgl_awal)
        tahun2, bulan2, hari2 = konvert_tanggal(tgl_akhir)
        
        d1 = datetime.date(tahun1, bulan1, hari1)
        d2 = datetime.date(tahun2, bulan2, hari2)

        if(task != ""):
            for deadline in temp_database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (d1 <= dt and dt <= d2 and deadline[2]==task):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        else:
            for deadline in temp_database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (d1 <= dt and dt <= d2):
                    response += data_db_to_String(deadline) + "\n"

                    end = True
        if (end):
            return True, response, status

    elif (status[1]):   # N minggu ke depan
        extracted = int(extract[1].rsplit(" ")[0])
        now = datetime.date.today()
        then = now + datetime.timedelta(days = extracted * 7)

        if (task != ""):
            for deadline in temp_database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt >= now and dt <= then and deadline[2]==task):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        else:
            for deadline in temp_database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt >= now and dt <= then):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        if (end):
            return True, response, status

    elif (status[2]):   # N hari ke depan
        extracted = int(extract[2].rsplit(" ")[0])
        now = datetime.date.today()
        then = now + datetime.timedelta(days = extracted)

        if (task != ""):
            for deadline in temp_database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt >= now and dt <= then and deadline[2]==task):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        else:
            for deadline in temp_database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt >= now and dt <= then):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        if (end):
            return True, response, status

    elif (status[3]):   # hari ini
        now = datetime.date.today()
        if (task != ""):

            for deadline in temp_database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt == now and deadline[2]==task):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        else:
            for deadline in temp_database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt == now):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        if (end):
            return True, response, status
    
    return False, "", status

def lihat_deadline(kalimat, database):
    tugas = regex_tugas(kalimat)
    if (tugas == ""):
        return False, ""
    
    if ("deadline" not in kalimat.lower()):
        return False, ""
    
    pernahmasuk = False
    if ("kapan" in kalimat.lower()):
        response = ""
        kode_kuliah = regex_kodekuliah(kalimat)
        for deadline in temp_database:
            if (kode_kuliah == deadline[3] and (KMP(deadline[2], "tucil") or KMP(deadline[2], "tubes"))):
                response += "(ID: " + str(deadline[0]) + ") - " + deadline[1].upper() + "\n"
                pernahmasuk = True

        if pernahmasuk:
            return True, response
        else:
            return False, "Deadline tidak ditemukan!"
    
    return False, ""

def ubah_deadline(kalimat, database):
    if ("deadline" not in kalimat.lower()):
        return False, ""
    response = ""
    Found = False
    text = kalimat.lower().split(" ")
    keyword = ["deadline", "diundur", "diubah", "task", "menjadi"]
    count = 0
    for pat in keyword:
        for word in text:
            if (KMP(pat, word)):
                count += 1

    if (count < 4):
        return False, ""
    idx = regex_get_nTask(kalimat)
    if (idx < 1):
        return False, "ID tidak valid"
    for data in temp_database:
        #bila ditemukan task dengan ID yang ada di database
        if (KMP(str(idx), str(data[0]))):
            data[1] = regex_tanggal(kalimat)
            response += "Deadline task " + str(data[0]) +" berhasil diubah\n"
            Found = True
            return Found, response

    if (not Found):
        response += "Tidak terdapat task dengan ID tersebut"
        return Found, response

def task_selesai(kalimat, database):
    response = ""
    Found = False
    if "task" not in kalimat:
        return False, ""

    #global temp_database
    text = kalimat.lower().split(" ")
    keyword = ["sudah", "selesai", "mengerjakan", "kelar", "menyelesaikan"]
    count = 0
    for pat in keyword:
        for word in text:
            if (KMP(pat, word)):
                count += 1
    if (count < 3):
        return False, ""

    idx = regex_get_nTask(kalimat)
    if (idx < 1):
        response += "ID Task tidak valid!\n"
        return False, response

    # ID valid
    for data in temp_database:
        #bila ditemukan task dengan ID yang ada di database
        if (KMP(str(idx), str(data[0]))):
            response += "Deadline task " + str(data[0]) +" berhasil dihapus\n"
            #database.pop(database.index(data))
            del database[database.index(data)]
            Found = True
            return Found, response
        
    if (not Found):
        response += "Tidak terdapat task dengan ID tersebut"
        return Found, response

def help_bot(kalimat):
    txt = kalimat.lower().split(" ")
    response = "[Fitur]\n"
    response += "1. Melihat Daftar Task\n"
    response += "2. Menambahkan Task Baru\n"
    response += "3. Menampilkan Deadline Suatu Task\n"
    response += "4. Memperbaharui Task Tertentu\n"
    response += "5. Menandai bahwa suatu Task sudah selesai dikerjakan\n"
    response += "6. Menampilkan opsi help\n"
    response += "\n[Daftar Kata Penting]\n"
    response += "1. Kuis\n2. Ujian\n3. Tucil\n4. Tubes\n5. Praktikum\n"
    if "help" in txt:
        return True, response
    
    keyword = ["apa", "bisa", "dilakukan", "bot", "assistant"]
    count = 0
    for pat in keyword:
        for word in txt:
            if (KMP(pat, word)):
                count += 1
    if (count < 4):
        return False, ""
    
    return True, response


