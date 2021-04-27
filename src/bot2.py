from regex import regex_katapenting, regex_kodekuliah, regex_tanggal, regex_topik, regex_lihattask
from KMP import KMP
from function import *
import datetime

temp_database = []
def tambah_task(kalimat):
    tanggal = regex_tanggal(kalimat)
    task = regex_katapenting(kalimat)
    kode_kuliah = regex_kodekuliah(kalimat)
    topik = regex_topik(kalimat)

    if (tanggal == "" or task == "" or kode_kuliah == "" or topik == ""):
        return False
    
    # Kalimat valid, masukkan ke database
    ID = len(temp_database) + 1
    new_data = []
    new_data.append(ID)
    new_data.append(tanggal)
    new_data.append(task)
    new_data.append(kode_kuliah)
    new_data.append(topik)
    temp_database.append(new_data)
    return True

kalimat = "Tubes IF2211 dengan topik String Matching pada 14 April 2021"
task_baru = tambah_task(kalimat)
if task_baru:
    print("Task baru berhasil ditambahkan!")

kalimat = "Halo bot, tolong ingetin kalau ada kuis IF3110 topik Bab 2-3 pada 22 April 2021"
task_baru = tambah_task(kalimat)
if task_baru:
    print("Task baru berhasil ditambahkan!")
kalimat = "Halo bot, tolong ingetin kalau ada kuis IF2110 topik Bab 2-3 pada 20 April 2021"
task_baru = tambah_task(kalimat)



for task in temp_database:
    print(task)

def lihat_task(kalimat, database):
    text = kalimat.lower()
    keyword_seluruh = ["deadline", "sejauh ini", "semua deadline", "dimiliki", "semua", "dimiliki"]
    count = 0
    for pattern in keyword_seluruh:
        for word in text:
            if (KMP(pattern, word)):
                count += 1
    
    if (count > 2):
        for task in temp_database:
            print("HEHEEGE")
            print(task)
        return
    
    # Kemungkinan lain
    status, extract = regex_lihattask(text)
    task = regex_katapenting(text)
    
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
        else:
            for deadline in database:
                y, m, d = konvert_tanggal(deadline[1])
                dt = datetime.date(y, m, d)
                if (d1 <= dt and dt <= d2):
                    print("Berhasil euy!")
                    print(deadline)
        


print("\n-----TES LIHAT TASK PERIODE TERTENTU-------")
kalimat = "Apa saja yang deadline tubes antara tanggal 02 april 2021 sampai 22 april 2021"
print(kalimat)
lihat_task(kalimat, temp_database)

def lihat_deadline(kalimat, database):
    kode_kuliah = regex_kodekuliah(kalimat)
    for deadline in database:
        if (kode_kuliah == deadline[3]):
            print(deadline[1])

print("\n-----CEK lihat_deadline-------")
kalimat = "Deadline tugas IF2211 itu kapan?"
print(kalimat)
lihat_deadline(kalimat, temp_database)

def ubah_deadline(kalimat, database):
    text = kalimat.lower()
    for data in database:
        #bila ditemukan task dengan ID yang ada di database
        if (KMP("task "+str(data[0])+" ", text)):
            data[1] = regex_tanggal(kalimat)
            print("Deadline task " + str(data[0]) +" berhasil diubah")
            break
    print("Tidak terdapat task dengan ID tersebut")

#ubah_deadline("tugas kuis tubes tucil", temp_database)
print("\n-----CEK ubah_deadline-------")
print("AWAL")
print(temp_database)
kalimat = "Deadline task 10 diundur menjadi 28 mei 2024"
print(kalimat)
ubah_deadline(kalimat, temp_database)
print("AKHIR")
print(temp_database)


