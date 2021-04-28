# DedBot
> Deadline reminder chatbot <br>
> Dibangun menggunakan Python dengan Flask dan Bootstrap 4.

## Daftar Isi
* [General info](#general-info)
* [Screenshots](#screenshot)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Contact](#contact)

## General Info
Dedbot, sebuah chatbot yang berfungsi untuk membantu mengingat berbagai deadline, tanggal penting, dan task-task tertentu pada penggunanya dengan memanfaatkan algoritma String Matching dan Regular Expression. Dedbot memiliki berbagai fitur, antara lain, menambahkan task baru, melihat daftar task yang harus dikerjakan, menampilkan deadline dari suatu task tertentu, memperbaharui task tertentu, Menandai bahwa suatu task sudah selesai dikerjakan, menampilkan opsi bantuan, dan menampilkan pesan kesalahan bila dedbot tidak dapat mengenali masukkan pengguna.


## Screenshot
<figure>
<img src="https://i.ibb.co/QJcbqPv/Snip20210428-5.png" alt="Screenshot Aplikasi" border="0">
<figcaption align="center"> Tampilan Awal DedBot </figcaption>

## Technologies
Menggunakan Flask with Python untuk bagian backend dan Bootstrap 4 untuk bagian tampilan web
```
Python 3.X
Flask 1.1.2
```

## Setup
Terdapat beberapa hal yang harus di-install sebelum menjalankan program ini.
Kami menggunakan text-editor Visual Studio Code pada proses pengembangan, berikut merupakan instalasi yang dilakukan untuk menjalankan program melalui VSCode

1. Install Python versi 3.X atau yang lebih baru, melalui VSCode.<br>
   Link: https://code.visualstudio.com/docs/python/python-tutorial
2. Install Flask dan ikuti seluruh langkah yang ada, termasuk persiapan Virtual Environment untuk program ini.<br>
   Link: https://code.visualstudio.com/docs/python/tutorial-flask
4. Semua prerequisite terpenuhi.

## Features
Fitur yang sudah ada:
- DedBot mampu menambahkan sebuah deadline baru
- DedBot mampu menampilkan task yang dimiliki dengan berbagai parameter, seperti semua deadline saat ini, deadline N hari ke depan, deadline N minggu ke depan, deadline hari ini.
- DedBot mampu menampilkan deadline task tertentu dengan keyoword kode kuliah
- DedBot mampu memperbaharui deadline sebuah task
- DedBot mampu menandai dan mengahapus task yang sudah diselesaikan

Saran pengembangan
- Fitur semacam auto-correct atau recommendation jika inputan pengguna memiliki kemiripan dengan keyword kata penting tertentu
- Menambah fitur-fitur lain yang mungkin membantu pengguna dalam mengatur task yang dimiliki

## Code Examples
Setelah semua prerequisite terpasang, lakukan clone repo ini ke direktori lokal. Kemudian jalankan program melalui `app.py`.
Terdapat 2 cara untuk menjalankannya pada local server.
Cara pertama dengan menekan tombol run pada VSCode.
Cara kedua ialah menggunakan terminal dan mengetik command berikut pada direktori src: 
```
$ cd src/
$ python3 app.py
atau
$ python3 -m flask run
atau
$ python app.py
```
Jika terjadi error saat melakukan load dan save database, anda dapat melakukan perubahan secara manual pada file `app.py` dan `bot.py`, dan melakukan perbaikan path ke `database.txt`. Hal ini dapat terjadi karena perbedaan sistem operasi yang Anda gunakan dengan yang kami gunakan.

Jika berhasil, kemudian akan muncul link local server pada project ini, klik link tersebut dan program berhasil dijalankan.

<p align="center">
  <a href="https://ibb.co/wJ9HY2V"><img src="https://i.ibb.co/1sDVb41/Snip20201115-4.png" alt="Snip20201115-4" border="0"></a>
</p>

## Contact
- Rizky Anggita S Siregar   -   13519132 <br>
- Wilson Tandya             -   13519209 <br>
<br>
Teknik Informatika <br>
Institut Teknologi Bandung <br>
2020
