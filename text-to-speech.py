# created by rayhan.frdh
# google text-to-speech adapted by python.hub

from gtts import gTTS
import random

def main():
	num = "1234567890"
	char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	uniqid = "".join(random.sample(f"{num}{char}", 8))

	audio = f"TtS_{uniqid.lower()}.mp3"
	convtext = input("Masukkan teks: \n")
	setting = gTTS(text=convtext, lang="id", slow=False)

	setting.save(audio)
	print("\nBerhasil konversi teks ke audio")

	# kode meminta validasi user apakah ingin menjalankan ulang
	rerun = input("Ulang program? (Y/N): ").upper()
	if rerun == "Y":
		main()
	else:
		print("\nThank you for using this program.")

if __name__ == "__main__":
	main()