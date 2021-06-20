import time, datetime
from datetime import date

def main():
  #basis penghitungan pasaran dimulai
  base = date(1900, 1, 1)
  
  #urutan array pasaran sudah fix tidak bisa dirubah
  arr_pasaran = [
    'Pahing',
    'Pon',
    'Wage',
    'Kliwon',
    'Legi'
  ]
  
  print("Program Pencarian Pasaran dan Neptu")
  print("Created by: rayhan.frdh\n")
  time.sleep(1.5)
  print("Cara penggunaan:")
  print("misal: Yang ingin dicari 17 Agustus 1945")
  print("1. Inputkan 17 pada tanggal\n2. Karena Agustus adalah bulan ke-8, maka inputkan 8 pada bulan\n3. Inputkan 1945 pada tahun\nSelamat Mencoba\n")
  time.sleep(2)
  
  tgl = int(input("Masukkan tanggal: "))
  bln = int(input("Masukkan bulan: "))
  thn = int(input("Masukkan tahun: "))
  time.sleep(1.5)
  target = date(thn,bln,tgl) 
  selisih = (target - base).days
  
  days_en = target.strftime("%A") #hari dalam inggris
  days_id = {
    "Monday" : "Senin",
    "Tuesday" : "Selasa",
    "Wednesday" : "Rabu",
    "Thursday" : "Kamis",
    "Friday" : "Jum`at",
    "Saturday" : "Sabtu",
    "Sunday" : "Minggu"
  }
  days_id = days_id[days_en] #fungsi replace hari dalam inggris ke indo sesuai dengan keluaran harinya
  
  months_en = target.strftime("%B")
  months_id = {
    "January" : "Januari",
    "February" : "Februari",
    "March" : "Maret",
    "April" : "April",
    "May" : "Mei",
    "June" : "Juni",
    "July" : "Juli",
    "August" : "Agustus",
    "September" : "September",
    "October" : "Oktober",
    "November" : "November",
    "December" : "December"
  }
  months_id = months_id[months_en]
  
  neptu_hari = {
    "Senin" : 4,
    "Selasa" : 3,
    "Rabu" : 7,
    "Kamis" : 8,
    "Jum`at" : 6,
    "Sabtu" : 9,
    "Minggu" : 5
  }
  neptu_hari = neptu_hari[days_id]
  
  #mencari dimana jatuhnya pasaran menggunakan metode selisih hari lalu dibagi dengan 5 kemudian ambil sisanya
  #jika sisa=0 pahing, sisa=1 pon, sisa=2 wage, sisa=3 kliwon, sisa=4 legi
  pasaran = arr_pasaran[selisih % 5]
  
  neptu_pasaran = {
    "Pahing" : 9,
    "Pon" : 7,
    "Wage" : 4,
    "Kliwon" : 8,
    "Legi" : 5
  }
  neptu_pasaran = neptu_pasaran[pasaran]
  
  sum_neptu = neptu_hari + neptu_pasaran
  
  text1 = "\n" + str(tgl) + " " + months_id + " " + str(thn) + " jatuh pada: " + days_id + " " + pasaran
  text2 = "Neptu kamu adalah {}".format(sum_neptu)
  print(text1 + "\n" + text2)
  print("") #new line 
  
  #kode meminta validasi user apakah ingin menjalankan ulang
  rerun = input("Ulang program? (Y/N): ")
  if rerun == "Y" or rerun == "y":
    main()
  if rerun == "N" or rerun == "n":
    print("Thank you for using this program.")
main()
