from regex import regex_katapenting, regex_kodekuliah, regex_tanggal, regex_topik, regex_lihattask
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
        return False
    
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
    return True

kalimat = "Tubes IF2211 dengan topik String Matching pada 27 April 2021"
task_baru = tambah_task(kalimat)
if task_baru:
    print("Task baru berhasil ditambahkan!")

kalimat = "Halo bot, tolong ingetin kalau ada kuis IF3110 topik Bab 2-3 pada 29 April 2021"
task_baru = tambah_task(kalimat)
if task_baru:
    print("Task baru berhasil ditambahkan!")
kalimat = "Halo bot, tolong ingetin kalau ada kuis IF2110 topik Bab 2-3 pada 25 Mei 2021"
task_baru = tambah_task(kalimat)

for i in temp_database:
    print(i)

def lihat_task(kalimat, database):
    text = kalimat.lower()
    a = text.split()
    #  MASIH PERLU PERBAIKAN, RADA ANEH
    keyword_seluruh = ["deadline", "sejauh", "ini", "dimiliki", "semua"]
    count = 0
    for pat in keyword_seluruh:
        for word in a:
            if (KMP(pat, word)):
                count += 1

    if (count > 3):
        for task in temp_database:
            print(task)
        print("LIHAT TASK END")
        return
    
    # Kemungkinan lain
    status, extract = regex_lihattask(text)
    task = regex_katapenting(text)
    end = False
    print(status)
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
                    print(deadline)
                    end = True
        else:
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (d1 <= dt and dt <= d2):
                    print("Berhasil euy!")
                    print(deadline)
                    end = True
        if (end):
            print("LIHAT TASK END")
            return

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
                    print(deadline)
                    end = True
        else:
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt >= now and dt <= then):
                    print(deadline)
                    end = True
        if (end):
            print("LIHAT TASK END")
            return

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
                    print(deadline)
                    end = True
        else:
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt >= now and dt <= then):
                    print(deadline)
                    end = True
        if (end):
            print("LIHAT TASK END")
            return

    elif (status[3]):   # hari ini
        now = datetime.date.today()
        if (task != ""):
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt == now and deadline[2]==task):
                    print(deadline)
                    end = True
        else:
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (dt == now):
                    print(deadline)
                    end = True
        if (end):
            print("LIHAT TASK END")
            return


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


# # print("\n\n========TES LIHAT TASK N Hari KE DEPAN===========")
# # lihat_task("Tampilkan semua deadline yang dimiliki sejauh ini", temp_database)
# # print("")
# # kalimat = "Apa saja deadline yang ada 10 hari ke depan nih bot?"
# # print(kalimat)
# # lihat_task(kalimat, temp_database)

print("\n\n========TES LIHAT TASK HARI INI===========")
lihat_task("Tampilkan semua deadline yang dimiliki sejauh ini", temp_database)
print("")
kalimat = "Apa saja deadline hari ini bot??"
print(kalimat)
lihat_task(kalimat, temp_database)



#BOT2
def lihat_deadline(kalimat, database):
    kode_kuliah = regex_kodekuliah(kalimat)
    for deadline in database:
        if (kode_kuliah == deadline[3]):
            print(deadline[1])

print("\n-----CEK lihat_deadline-------")
kalimat = "Deadline tugas IF2211 itu kapan?"
lihat_deadline(kalimat, temp_database)



def ubah_deadline(kalimat, database):
    Found = False
    text = kalimat.lower()
    for data in database:
        #bila ditemukan task dengan ID yang ada di database
        if (KMP("task "+str(data[0])+" ", text)):
            data[1] = regex_tanggal(kalimat)
            print("Deadline task " + str(data[0]) +" berhasil diubah")
            Found = True
            break
    if (not Found):
        print("Tidak terdapat task dengan ID tersebut")

print("\n-----CEK ubah_deadline-------")
print("Sebelum diubah")
print(temp_database)

kalimat = "Deadline task 1 diundur menjadi 28 mei 2024"
#print(kalimat)
ubah_deadline(kalimat, temp_database)

print("Setelah diubah")
print(temp_database)


def task_selesai(kalimat, database):
    Found = False
    #global temp_database
    text = kalimat.lower()
    for data in database:
        #bila ditemukan task dengan ID yang ada di database
        if (KMP("task "+str(data[0])+" ", text)):
            print("Deadline task " + str(data[0]) +" berhasil dihapus")
            #database.pop(database.index(data))
            del database[database.index(data)]
            Found = True
            break
    if (not Found):
        print("Tidak terdapat task dengan ID tersebut")

#ubah_deadline("tugas kuis tubes tucil", temp_database)
print("\n-----CEK task_selesai-------")
print("AWAL")
print(temp_database)
kalimat = "Saya sudah selesai mengerjakan task 1 "#masih masalah klo ga pake spasi diakhir
#print(kalimat)
task_selesai(kalimat, temp_database)
print("AKHIR")
print(temp_database)
