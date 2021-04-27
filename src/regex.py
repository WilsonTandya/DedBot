import re

def regex_tanggal(tanggal):
    # Tanggal dengan format XX NAMA_BULAN YYYY
    tanggal = tanggal.lower()
    # print(tanggal)
    bulan = 'januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember'
    pattern = r'[0-9]{1,2}\s(' + bulan + ')' + r'\s[0-9]{4,4}'
    # pattern 2 = r'[0-9]{'
    x = re.search(pattern, tanggal)
    if x :
        print(x.group())
        return x.group()
    else:
        print("Tidak ketemu kode mata kuliah")
        return ""

def regex_kodekuliah(kode):

    # Kode mata kuliah yang valid adalah IFXYAA, dimana X [1-9], Y [0-3], A [0-9]
    pattern = r'IF[1-9][0-3][0-9][0-9]'
    x = re.search(pattern, kode)
    if x:
        print(x.group())
        return x.group()
    else:
        print("Tidak ketemu kode mata kuliah")
        return ""

def regex_katapenting(kata):
    kata = kata.lower()
    kata_penting = "kuis|ujian|tucil|tubes|praktikum"
    pattern = r'(' + kata_penting + r')'
    x = re.search(pattern, kata)

    if (x):
        # print(x.group())
        return x.group()
    else:
        print("Tidak ketemu kata penting!")
        return ""

def regex_topik(topik):
    # Asumsi panjang sebuah topik selalu dua kata
    # dan diawali dengan kata topik
    # contoh : Tubes IF2240 dengan topik String Matching pada tanggal 22/03/2021
    # maka topik: String Matching
    topik = topik.lower()
    pattern = r'topik\s[a-zA-Z0-9-,_]+\s[a-zA-Z0-9-,_]+'
    # pattern = r'topik\s\w+(?:-\w+)+\s'
    x = re.search(pattern, topik)
    if x:
        print(x.group())
        return x.group()
    else:
        print("Tidak ketemu topik")
        return ""

# regex_tanggal("test 123 tanggal 13 april 2021")
# regex_tanggal("test 123 tanggal 003 DeSember 2021")

# regex_tanggal("test 123 tanggal 20 mei 2021")
# regex_tanggal("Tambahkan tugas baru pada tanggal 22 juni 2021")

# regex_kodekuliah("Mata kuliah IF1030 OKE MANTAP")

regex_katapenting("Tolong tambahkan tucil TuBeS praktikuM deadline Tubes IF2211")

regex_topik("Tubes IF2240 dengan topik string Matching gege")
regex_topik("Halo tolong ingetin kalau ada kuis IF3110 dengan topik Bab 2_3 pada 22 April 2021")

# Regex untuk melihat daftar deadline yang dimiliki

def regex_lihattask(kalimat):
    kalimat = kalimat.lower()
    bulan = 'januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember'
    pattern_date = r'[0-9]{1,2}\s(' + bulan + ')' + r'\s[0-9]{4,4}'
    pattern_periode = pattern_date + r'\ssampai\s' + pattern_date
    pattern_N_minggu = r'[1-9]{1,3}\sminggu\ske\sdepan'
    pattern_N_hari = r'[0-9]{1,9}\shari\ske\sdepan'
    pattern_hari_ini = r'hari\sini'

    # pattern_semua = r'deadline\ssejauh\sini'
    # print(pattern_semua)
    
    a = re.search(pattern_periode, kalimat)
    b = re.search(pattern_N_minggu, kalimat)
    c = re.search(pattern_N_hari, kalimat)
    d = re.search(pattern_hari_ini, kalimat)
    
    status = []
    extract = []

    if a:
        status.append(True)
        extract.append(a.group())
    else:
        status.append(False)
        extract.append("")
    if b:
        status.append(True)
        extract.append(b.group())
    else:
        status.append(False)
        extract.append("")
    if c:
        status.append(True)
        extract.append(c.group())
    else:
        status.append(False)
        extract.append("")
    if d:
        status.append(True)
        extract.append(d.group())
    else:
        status.append(False)
        extract.append("")
    
    return status, extract
    
def regex_get_nTask(kalimat):
    pattern = r'task\s[0-9]{1,5}'
    x = re.search(pattern, kalimat)

    if x:
        temp = x.group()
        temp = temp.split(" ")[1]
        return int(temp)
    else:
        return -1

def regex_tugas(kalimat):
    pattern = r'tugas'
    x = re.search(pattern, kalimat.lower())
    if x:
        return x.group()
    else:
        return ""

# status, extract = regex_lihattask("Coba blbalba antara tanggal 14 mei 2021 sampai 17 Mei 2021 ")
status, extract = regex_lihattask("Apa saja deadline 3 minggu ke depan nih bot?")
# regex_lihattask("Apa saja deadline 5 minggu ke depan")
# regex_lihattask("apa saja deadline sejauh ini?")
# regex_lihattask("apa saja sejauh ini? ada deadline apa saja")
print(status)
print(extract)
print(extract[0].rsplit(" sampai "))
print(extract[1].rsplit(" ")[0])


# print(konvert_tahun(extract[0].rsplit(" sampai ")[0]))
# print(konvert_bulan(extract[0].rsplit(" sampai ")[0]))
# print(konvert_tanggal(extract[0].rsplit(" sampai ")[0]))
