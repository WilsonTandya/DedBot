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

def tambah_tanggal_hari(tgl1, jumlah_hari):
    tahun = konvert_tahun(tgl1)
    bulan = konvert_bulan(tgl1)
    hari = konvert_hari(tgl1)

    hari2 = hari + jumlah_hari

    if (bulan==1 or bulan==3 or bulan==5 or bulan==7 or bulan==8 or bulan==10 or bulan==1 or 12):
        if (hari2 > 31):
            hari2 = hari2 - 31
            bulan2 = bulan + 1
    elif (bulan == 2):
        if (hari2 > 28):
            hari2 = hari2 - 28
            bulan2 = bulan + 1
    return 

def tanggal_less_than_eq(tgl1, tgl2):
    tahun1 = konvert_tahun(tgl1)
    bulan1 = konvert_bulan(tgl1)
    hari1 = konvert_hari(tgl1)

    tahun2 = konvert_tahun(tgl2)
    bulan2 = konvert_bulan(tgl2)
    hari2 = konvert_hari(tgl2)

    if tahun1 > tahun2:
        return False
    if tahun1 < tahun2:
        return True
    
    # tahun1 = tahun2, cek bulan
    if (bulan1 > bulan2):
        return False
    if (bulan1 < bulan2):
        return True
    
    # bulan1 = bulan2, cek hari
    if (hari1 > hari2):
        return False
    if (hari1 < hari2):
        return True
    
    # tahun1 = tahun2, bulan1 = bulan2, hari1 = hari2
    return True

def tanggal_greater_than_eq(tgl1, tgl2):
    tahun1 = konvert_tahun(tgl1)
    bulan1 = konvert_bulan(tgl1)
    hari1 = konvert_hari(tgl1)

    tahun2 = konvert_tahun(tgl2)
    bulan2 = konvert_bulan(tgl2)
    hari2 = konvert_hari(tgl2)

    if tahun1 < tahun2:
        return False
    if tahun1 > tahun2:
        return True
    
    # tahun1 = tahun2, cek bulan
    if (bulan1 < bulan2):
        return False
    if (bulan1 > bulan2):
        return True
    
    # bulan1 = bulan2, cek hari
    if (hari1 < hari2):
        return False
    if (hari1 > hari2):
        return True
    
    # tahun1 = tahun2, bulan1 = bulan2, hari1 = hari2
    return True
