from regex import regex_katapenting, regex_kodekuliah, regex_tanggal, regex_topik, regex_lihattask, regex_get_nTask, regex_tugas
from KMP import KMP
from function import *
import datetime

AUTO_INCREMENT = 1

temp_database = []

def tambah_task(kalimat):
    global AUTO_INCREMENT
    tanggal = regex_tanggal(kalimat)
    task = regex_katapenting(kalimat)
    kode_kuliah = regex_kodekuliah(kalimat)
    topik = regex_topik(kalimat)

    if (tanggal == "" or task == "" or kode_kuliah == "" or topik == ""):
        return False, ""
    
    # Kalimat valid, masukkan ke database
    ID = AUTO_INCREMENT
    new_data = []
    new_data.append(ID)
    new_data.append(tanggal)
    new_data.append(task)
    new_data.append(kode_kuliah)
    new_data.append(topik)
    temp_database.append(new_data)
    AUTO_INCREMENT += 1
    response = "[TASK BERHASIL DICATAT\n"
    response += "(ID: " + str(ID) + ") - " + (tanggal.upper()) + " - " + task.upper() + " - " + kode_kuliah.upper() + " - " + topik.upper()
    response += "\n" 
    return True, response

kalimat = "Tubes IF2211 dengan topik String Matching pada 27 April 2021"
task_baru, response = tambah_task(kalimat)
if task_baru:
    print("Task baru berhasil ditambahkan!")
    print(response)



kalimat = "Halo bot, tolong ingetin kalau ada kuis IF3110 topik Bab 2-3 pada 29 April 2021"
task_baru = tambah_task(kalimat)
if task_baru:
    print("Task baru berhasil ditambahkan!")
kalimat = "Halo bot, tolong ingetin kalau ada kuis IF2110 topik Bab 2-3 pada 25 Mei 2021"
task_baru = tambah_task(kalimat)

for i in temp_database:
    print(i)

def lihat_task(kalimat, database):
    response = ""
    if "deadline" not in kalimat :
        return False, response

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
    print(count)
    if (count > 4):
        task = regex_katapenting(text)
        if (task != ""):
            for deadline in temp_database:
                if (deadline[2]==task):
                   response += data_db_to_String(deadline) + "\n"
        else:
            for deadline in temp_database:
                response += data_db_to_String(deadline) + "\n"
        print("LIHAT TASK END")
        return True, response
    
    # Kemungkinan lain
    status, extract = regex_lihattask(text)
    task = regex_katapenting(text)
    end = False
    print(status)
    response += "[DAFTAR DEADLINE]\n"
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
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (d1 <= dt and dt <= d2 and deadline[2]==task):
                    print("Berhasil")
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        else:
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (d1 <= dt and dt <= d2):
                    print("Berhasil euy!")
                    response += data_db_to_String(deadline) + "\n"

                    end = True
        if (end):
            print("LIHAT TASK END")
            return True, response

    elif (status[1]):   # N minggu ke depan
        extracted = int(extract[1].rsplit(" ")[0])
        now = datetime.date.today()
        then = now + datetime.timedelta(days = extracted * 7)
        print("UHUYY")
        print(then)
        if (task != ""):
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt >= now and dt <= then and deadline[2]==task):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        else:
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt >= now and dt <= then):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        if (end):
            print("LIHAT TASK END")
            return True, response

    elif (status[2]):   # N hari ke depan
        extracted = int(extract[2].rsplit(" ")[0])
        print(extracted)
        now = datetime.date.today()
        then = now + datetime.timedelta(days = extracted)
        if (task != ""):
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt >= now and dt <= then and deadline[2]==task):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        else:
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt >= now and dt <= then):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        if (end):
            print("LIHAT TASK END")
            return True, response

    elif (status[3]):   # hari ini
        now = datetime.date.today()
        if (task != ""):
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt == now and deadline[2]==task):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        else:
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt == now):
                    response += data_db_to_String(deadline) + "\n"
                    end = True
        if (end):
            print("LIHAT TASK END")
            return True, response
    
    return False, ""

# # print("\n-----TES LIHAT TASK PERIODE TERTENTU-------")
# # kalimat = "Apa saja yang tubes antara tanggal 02 april 2021 sampai 22 april 2021"
# # print(kalimat)
# # lihat_task(kalimat, temp_database)


# # print("\n\n========TES LIHAT TASK N MINGGU KE DEPAN===========")
# # lihat_task("Tampilkan semua deadline yang dimiliki sejauh ini", temp_database)
# # print("")
# # kalimat = "Apa saja deadline yang ada 3 minggu ke depan nih bot?"
# # print(kalimat)
# # lihat_task(kalimat, temp_database)


print("\n\n========TES LIHAT TASK N Hari KE DEPAN===========")
lihat_task("Tampilkan semua deadline yang dimiliki sejauh ini", temp_database)
print("")
kalimat = "Apa saja deadline yang ada 10 hari ke depan nih bot?"
print(kalimat)
status, response = lihat_task(kalimat, temp_database)
print(response)

print("\n\n========TES LIHAT TASK HARI INI===========")
a, b = lihat_task("Tampilkan semua deadline yang dimiliki sejauh ini", temp_database)
print("")
print(b)
kalimat = "Apa saja tugas hihi deadline hari ini?"
print(kalimat)
sukses, response = lihat_task(kalimat, temp_database)
print(response)

for i in temp_database:
    print(i)


print("")
kalimat = "Apa saja tugas hihi deadline hari ini?"
print(kalimat)
sukses = lihat_task(kalimat, temp_database)
print(sukses)

for i in temp_database:
    print(i)



#BOT2
def lihat_deadline(kalimat, database):
    tugas = regex_tugas(kalimat)
    if (tugas == ""):
        return False, ""
    
    if ("deadline" not in kalimat.lower()):
        return False, ""
    
    if ("kapan" in kalimat.lower()):
        response = ""
        kode_kuliah = regex_kodekuliah(kalimat)
        for deadline in database:
            if (kode_kuliah == deadline[3] and (KMP(deadline[2], "tucil") or KMP(deadline[2], "tubes"))):
                response += "(ID: " + str(deadline[0]) + ") - " + deadline[1].upper() + "\n"
        return True, response
    
    return False, ""

print("\n-----CEK lihat_deadline-------")
kalimat = "Deadline tugas IF2211 itu kapan?"
stat, response = lihat_deadline(kalimat, temp_database)
print(response)



def ubah_deadline(kalimat, database):
    response = ""
    Found = False
    text = kalimat.lower().split(" ")
    keyword = ["deadline", "diundur", "diubah", "task", "menjadi"]
    count = 0
    for pat in keyword:
        for word in text:
            if (KMP(pat, word)):
                count += 1
    print(count)
    if (count < 4):
        return False
    idx = regex_get_nTask(kalimat)
    if (idx < 1):
        print("ID tidak valid")
        return False, ""
    for data in database:
        #bila ditemukan task dengan ID yang ada di database
        if (KMP(str(idx), str(data[0]))):
            data[1] = regex_tanggal(kalimat)
            response += "Deadline task " + str(data[0]) +" berhasil diubah\n"
            Found = True
            return Found, response

    if (not Found):
        response += "Tidak terdapat task dengan ID tersebut"
        return Found, response

print("\n-----CEK ubah_deadline-------")
print("Sebelum diubah")
print(temp_database)

kalimat = "Deadline task 3 diundur menjadi 28 mei 2024"
#print(kalimat)
status, response = ubah_deadline(kalimat, temp_database)
print(response)

print("Setelah diubah")
print(temp_database)


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
    for data in database:
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

# ubah_deadline("tugas kuis tubes tucil", temp_database)
print("\n-----CEK task_selesai-------")
print("AWAL")
for i in temp_database:
    print(i)
kalimat = "Gue sudah kelar nih mengerjakan task 3"#masih masalah klo ga pake spasi diakhir
#print(kalimat)
task_selesai(kalimat, temp_database)
print("AKHIR")
for i in temp_database:
    print(i)
