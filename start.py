""" Pada module ini akan di perkenalkan library yang berfungsi untuk.
mengimport library pandas dan numpy sebagai pd dan np masing-masing. Kemudian, dataf, pd, dan np 
dideklarasikan sebagai variabel global, sehingga dapat digunakan pada skrip seluruh program tanpa harus 
direimport setiap kali digunakan. pandas adalah library open source yang membantu dalam memproses dan analisis 
data. Ini digunakan untuk mengatasi masalah seperti manipulasi tabel dan pengolahan data secara efisien. 
numpy adalah library numerikal Python yang digunakan untuk operasi matematis dan pengolahan array 
multidimensional. Ini sangat berguna untuk melakukan operasi matematis dan pemrosesan data numeral.
"""


# Import library yang akan digunakan
global dataf, pd, np
import pandas as pd
import numpy as np

"""
Pada project ini terdapat beberapa method/fungsi yang digunakan sebagai berikut.
init: Fungsi ini dipanggil saat membuat objek baru dari class Transaction.
reset_transaction: Fungsi ini menghapus semua item dari list item_list.
check_order: Fungsi ini menampilkan data belanja dalam bentuk tabel.
update_item: Fungsi ini mengubah nama item barang.
update_jumlah: Fungsi ini mengubah jumlah item barang.
update_harga: Fungsi ini mengubah harga item barang.
delete_item: Fungsi ini menghapus item barang dari list item_list.
total_price: Fungsi ini menghitung dan menampilkan total harga belanja.
"""
