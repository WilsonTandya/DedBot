def konvert_tahun(tgl):
    return int(tgl.split(" ")[2])

def konvert_bulan(tgl):
    nama_bln = tgl.split(" ")[1]
    bulan = ["januari", "februari", "maret","april", "mei", "juni", "juli", "agustus", "september", "oktober", "november", "desember"]
    for i in range(12):
        if nama_bln == bulan[i]:
            return i+1

def konvert_hari(tgl):
    hari = tgl.split(" ")[0]
    return int(hari)

def konvert_tanggal(tgl):
    return konvert_tahun(tgl), konvert_bulan(tgl), konvert_hari(tgl)

def data_db_to_String(data):
    response = ""
    response += "(ID: " + str(data[0]) + ") - " + (data[1].upper()) + " - " + data[2].upper() + " - " + data[3].upper() + " - " + data[4].upper()
    return response