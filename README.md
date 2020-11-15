# SABEB  SEARCH  ENGINE

Search engine ini merupakan salah satu project sekaligus tugas besar mata kuliah IF2123 Aljabar Linier dan Geometri. Project ini disusun oleh kelompok Sabeb sehingga project ini kami namakan Sabeb Search Engine. Kelompok kami beranggotakan Giovani Anggasta (NIM 13519155), M. Ibnu Syah Hafizh (NIM 13519177), dan Farhan Fadillah Rafi (NIM 13519204).

## Setup & Installation in MacOs 

Sebelum menikmati experience dan berselancar di Sabeb Search Engine, kamu harus menyiapkan beberapa barang wajib. Pastikan Pythonnya yang terbaru yaak (kalau masih yg lama silakan menyesuaikan).

```bash
python3 -m venv Env
source Env\bin\activate
python -m pip install --upgrade pip
pip3 install numpy
pip3 install sastrawi
pip3 install scipy
pip3 install pandas
```

## Usage

Setelah siap semua persediaan, saatnya mulai!!

```bash
cd src
manage.py runserver
```
jika tidak bisa dijalankan dan terdapat pesan cinta seperti ini "You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions." Jangan panik kawan..

kamu kekurangan amunisi, coba ikutin ini

```bash
python manage.py migrate
```
kemudian ketik ulang  ```bash manage.py runserver```

Nantinya akan diperoleh link suci menuju Sabeb Search Engine. Selamat menikmati!!! :V

