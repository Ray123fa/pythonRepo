# Gunting(G), Batu(B), Kertas(K)

import time
import random

def false():
	arr_gesture = ["G", "B", "K"]

	print("Inputan anda salah,\nharap inputkan salah satu dari G, B, dan K\n")
	user_gesture = input("Pilih gesture: ")
	if user_gesture not in arr_gesture:
		false()
	else:
		random.shuffle(arr_gesture)
		my_gesture = arr_gesture[0]

		if user_gesture == my_gesture:
			same()
		else:
			print(f"Program: {my_gesture}")

			if user_gesture == "G" and my_gesture == "B":
				print("My Program Win")
			elif user_gesture == "G" and my_gesture == "K":
				print("You Win")
			elif user_gesture == "B" and my_gesture == "G":
				print("You Win")
			elif user_gesture == "B" and my_gesture == "K":
				print("My Program Win")
			elif user_gesture == "K" and my_gesture == "G":
				print("My Program Win")
			elif user_gesture == "K" and my_gesture == "B":
				print("You Win")

def same():
	arr_gesture = ["G", "B", "K"]

	user_gesture = input("Pilih gesture lagi: ")
	if user_gesture not in arr_gesture:
		false()
	else:
		random.shuffle(arr_gesture)
		my_gesture = arr_gesture[0]

		if user_gesture == my_gesture:
			same()
		else:
			print(f"Program: {my_gesture}")

			if user_gesture == "G" and my_gesture == "B":
				print("My Program Win")
			elif user_gesture == "G" and my_gesture == "K":
				print("You Win")
			elif user_gesture == "B" and my_gesture == "G":
				print("You Win")
			elif user_gesture == "B" and my_gesture == "K":
				print("My Program Win")
			elif user_gesture == "K" and my_gesture == "G":
				print("My Program Win")
			elif user_gesture == "K" and my_gesture == "B":
				print("You Win")

def main():
	arr_gesture = ["G", "B", "K"]

	print("Program GBK (Gunting, Batu, Kertas)\nCreated by rayhan.frdh\n")
	time.sleep(1.5)
	print("Petunjuk penggunaan:\n• Pilih G untuk gunting\n• Pilih B untuk batu\n• Pilih K untuk kertas\n\n")
	print("Algoritma yang dipakai:\n- Gesture dari program dipilih secara acak agar tidak ada\n  unsur kecurangan.\n- Jika inputan user dan output dari program sama,\n  program secara otomatis akan meminta user menginputkan\n  ulang.\n\nSelamat Mencoba")
	time.sleep(1.5)

	user_gesture = input("Pilih gesture: ")
	if user_gesture not in arr_gesture:
		false()
	else:
		random.shuffle(arr_gesture)
		my_gesture = arr_gesture[0]

		if user_gesture == my_gesture:
			same()
		else:
			print(f"Program: {my_gesture}")

			if user_gesture == "G" and my_gesture == "B":
				print("My Program Win")
			elif user_gesture == "G" and my_gesture == "K":
				print("You Win")
			elif user_gesture == "B" and my_gesture == "G":
				print("You Win")
			elif user_gesture == "B" and my_gesture == "K":
				print("My Program Win")
			elif user_gesture == "K" and my_gesture == "G":
				print("My Program Win")
			elif user_gesture == "K" and my_gesture == "B":
				print("You Win")

	# kode meminta validasi user apakah ingin menjalankan ulang
	rerun = input("Ulang program? (Y/N): ").upper()
	if rerun == "Y":
		main()
	else:
		print("\nThank you for using this program.")

if __name__ == "__main__":
	main()