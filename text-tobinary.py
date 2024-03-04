# python -c "import module name" -> untuk cek apakah modul sudah terinstall
# created by me

import re
import time

def txtToBin():
	str = input("Masukkan teks yang ingin dikonversi ke bilangan biner: \n")
	result = ' '.join(f"{ord(i):08b}" for i in str)
	print("\nResult:\n" + result)

	# kode meminta validasi user apakah ingin menjalankan ulang
	reconv = input("\nKonversi teks lagi? (Y/N): ")
	if reconv == "Y" or reconv == "y":
		txtToBin()
	if reconv == "N" or reconv == "n":
		cgconv = input("Atau konversi biner ke text? (Y/N): ")
		if cgconv == "Y" or cgconv == "y":
			binToTxt()
		if cgconv == "N" or cgconv == "n":
			print("\nThank you for using this program.")


def binToTxt():
	bin = input("Masukkan biner yang ingin dikonversi ke teks: \n")

	if re.findall(" ", bin):
		bin_replace = bin.replace(" ", "")
		n = int(bin_replace, 2)
		result = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
		print("\nResult: " + result)
	else:
		n = int(bin, 2)
		result = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
		print("\nResult: " + result)

	# kode meminta validasi user apakah ingin menjalankan ulang
	reconv = input("\nKonversi biner lagi? (Y/N): ")
	if reconv == "Y" or reconv == "y":
		binToTxt()
	if reconv == "N" or reconv == "n":
		cgconv = input("Atau konversi teks ke biner? (Y/N): ")
		if cgconv == "Y" or cgconv == "y":
			txtToBin()
		if cgconv == "N" or cgconv == "n":
			print("\nThank you for using this program.")

def main():
	print("Python String to Binary and Reverse to\nby rayhan.frdh\n")
	time.sleep(1.5)
	print("Cara penggunaan:\n- Ketik 1 untuk konversi teks ke biner\n- Ketik 2 untuk konversi biner ke teks\n\nBiner yang didukung seperti berikut: 01000001\n")
	time.sleep(2)

	arr_opsi = ["1", "2"]
	opsi = input("Pilih opsi: ")

	if opsi not in arr_opsi:
		print("Opsi yang dipilih tidak sesuai")
	else:
		if opsi == "1":
			txtToBin()
		elif opsi == "2":
			binToTxt()

if __name__ == "__main__":
	main()