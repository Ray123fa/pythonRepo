import requests as req
import json

webApi = req.get("https://js-indo.herokuapp.com/corona/country/indonesia/provinsi/kalimantan")
result = webApi.json()
  
print("Kasus COVID-19 di Pulau Kalimantan\nby rayhan.frdh\nSupported by js-indo.herokuapp.com/corona\n")
  
for i in range(5):
  provinsi = result['jsindo']['data'][i]['provName']
  positif = result['jsindo']['data'][i]['case']['positive']
  dirawat = result['jsindo']['data'][i]['case']['recovered']
  meninggal = result['jsindo']['data'][i]['case']['deaths']
  print(f"{provinsi}\nPositif: {positif}\nDirawat: {dirawat}\nMeninggal: {meninggal}")
  print("")
  
print("Thank you for using this program.")
