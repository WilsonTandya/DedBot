from regex import regex_katapenting, regex_kodekuliah, regex_tanggal, regex_topik

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
    new_data.append("ID: " + str(ID))
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


for task in temp_database:
    print(task)