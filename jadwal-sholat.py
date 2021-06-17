import requests as req
import json, datetime, time, re

arr_days_en = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', '', '', '', '', '']
arr_days_id = ['Senin', 'Selasa', 'Rabu', 'Kamis', "Jum'at", 'Sabtu', 'Minggu', '', '', '', '', '']

arr_months_en = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
arr_months_id = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

num_months_arb = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
name_months_arb = ['Muharram', 'Safar', 'Rabiul Awal', 'Rabiul Akhir', 'Jumadil Awal', 'Jumadil Akhir', 'Rajab', "Sya'ban", 'Ramadhan', 'Syawal', 'Dzulkaidah', 'Dzulhijjah']

arr_name = ['imsak', 'subuh', 'dzuhur', 'ashar', 'maghrib', 'isya']
arr_timezone = ['Asia/Jakarta', 'Asia/Makassar', 'Asia/Jayapura']
tz_replace = ['GMT+07.00 (WIB)', 'GMT+08.00 (WITA)', 'GMT+09.00 (WIT)']

now = str(datetime.datetime.now())
today = now[:10]
year = today[:4]
month = today[5:7]
date = today[-2:]

api = req.get("https://api.aladhan.com/v1/timings/{}?latitude=-3.320807&longitude=114.638840&method=4".format(date + "-" + month + "-" + year)) #Daerah Sei Lulut dan sekitarnya
result = api.json()

dt = time.strftime("%A, %d %B %Y", time.localtime()) #gregorian date

dt2 = result['data']['date']['hijri']['date'] #hijr date
tgl = dt2[:2]
m = dt2[3:5] #nomor bulan
thn = dt2[-4:]

for x in range(12):
  if re.findall(arr_days_en[x], dt):
    p = dt.replace(arr_days_en[x], arr_days_id[x])
  if re.findall(arr_months_en[x], dt):  
    grego_date = p.replace(arr_months_en[x], arr_months_id[x])
  if re.findall(num_months_arb[x], m):
    bln = m.replace(num_months_arb[x], name_months_arb[x]) #nama bulan
    hijr_date = tgl + " " + bln + " " + thn  
    
arr_praytimes = {
  "date" : grego_date + " | " + hijr_date,
  "imsak" : "Imsak: " + result['data']['timings']['Imsak'],
  "subuh" : "Subuh: " + result['data']['timings']['Fajr'],
  "dzuhur" : "Dzuhur: " + result['data']['timings']['Dhuhr'],
  "ashar" : "Ashar: " + result['data']['timings']['Asr'],
  "maghrib" : "Maghrib: " + result['data']['timings']['Maghrib'],
  "isya" : "Isya: " + result['data']['timings']['Isha']
}

tz = result['data']['meta']['timezone'] #timezone as tz
for i in range(3):
  if re.findall(arr_timezone[i], tz):
    zonawaktu = tz.replace(arr_timezone[i], tz_replace[i])

arr_settings = {
  "latitude" : result['data']['meta']['latitude'],
  "longitude" : result['data']['meta']['longitude'],
  "timezone" : zonawaktu,
  "calculation" : "Universitas Umm Al-Qura",
  "juristic" : "Syafi'i"
}

print(arr_praytimes['date'])
print(arr_settings['timezone'])
print()

for i in range(6):
  x = arr_praytimes[arr_name[i]]
  print(x)

print()  
print("Koordinat: " + str(arr_settings['latitude']) + ", " + str(arr_settings['longitude']))
print("Metode Kalkulasi: " + arr_settings['calculation'])
print("Metode Juristik: Standar(" + arr_settings['juristic'] + ")")
