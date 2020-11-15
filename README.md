# SABEB  SEARCH  ENGINE

Search engine ini merupakan salah satu project sekaligus tugas besar mata kuliah IF2123 Aljabar Linier dan Geometri. Project ini disusun oleh kelompok Sabeb sehingga project ini kami namakan Sabeb Search Engine. Kelompok kami beranggotakan Giovani Anggasta (NIM 13519155), M. Ibnu Syah Hafizh (NIM 13519177), dan Farhan Fadillah Rafi (NIM 13519204).

## Setup & Installation in MacOs 

Pertama-tama buka terminal dan ketik ini dulu, jangan lupa

```bash
git clone https://github.com/ibnuhafizzh/Tubes2-ALGEO.git
```

Sebelum menikmati experience dan berselancar di Sabeb Search Engine, kamu harus menyiapkan beberapa barang wajib. Pastikan Python & Pip yang terbaru yaak (kalau masih yg lama silakan menyesuaikan).

```bash
pip3 install django
pip3 install numpy
pip3 install sastrawi
pip3 install scipy
pip3 install pandas
```

## Usage

Setelah siap semua persediaan, saatnya mulai!!

```bash
cd src

macOS:
python3 manage.py runserver

Windows:
manage.py runserver
```
Jika tidak bisa dijalankan dan terdapat pesan cinta seperti ini ```"You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions."``` Jangan panik kawan..

Kamu kekurangan amunisi, coba lakukan ini

```bash
mac:
python3 manage.py migrate

windows:
manage.py migrate
```
kemudian ketik ulang  
```bash 
mac:
python3 manage.py runserver

windows:
manage.py runserver
```

Apabila berhasil akan diperoleh link suci menuju Sabeb Search Engine.

```bash
Starting development server at (Link)
```
Selamat menikmati!!! :D

