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
        print(x.group())
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