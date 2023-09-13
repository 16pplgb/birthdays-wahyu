# import os untuk mengakses sistem database
import os

# import SQL untuk menggunakan bahsa SQL didalam Python
from cs50 import SQL
# import tools untuk website
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# mengatur nama aplikasi
app = Flask(__name__)

# dipakai untuk koneksi ke database
db = SQL("sqlite:///birthdays.db")

# https://127.0.0.1.5000/
@app.route("/", methods=["GET", "POST"])
#ketika route "/" dipanggil/diakses, maka fungsi index() dieksekusi
def index():
    # jika request yang dilakukan pengguna adalah post, maka eksekusi kode dalam if
    if request.method == "POST":

        #Acces from data / membaca data yang diisikan pada form
        name = request.form.get("name") # ambil data dari input name
        month = request.form.get("month") # ambil data dari input month
        day = request.form.get("day") # ambil data dari input day

        # Insert data into database,  masukan data name, month, dan day ke data base
        db.execute("INSERT INTO brithdays (name, month, day) VALUES(?, ?, ?)" , name, month, day)

        # Go back to hpmepage, balik ke  https://127.0.0.1.5000/
        return redirect("/")

        # jika requestnya selain POST, maka tampilkan data dari tabel birthdays
        else:

            # ambil seluruh data dari tabel brithdays, simpan di variabel brithdays
            birthdays = db.execute(SELECT * FROM birthdays)

            # Salin isi variabel birthdays, lalu kirim ke index.html
            return render_template("index.html", birthdays=birthdays)