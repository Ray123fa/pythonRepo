# non-gui
# shell/terminal mode

from my_function import *
from cprint import cprint

def choose():
	arr_typed = ["1", "2", "3", "4", "5", "6", "7", "8"]
	typed = input("Pilih salah satu dari opsi: ")

	if typed not in arr_typed:
		cprint("Not in options! Please try again...\n", c="y")
		choose()
	else:
		cprint(
			"\nGunakan tanda titik untuk menginput bilangan desimal.\nExample: 0,85 => 0.85", c="g")

		arr_func = [addition, substraction, multiplication,
					division, powered, mod, logarithm, quadratic_eq]

		i = int(typed)-1
		if typed in arr_typed[i]:
			if int(typed) <= 6:
				while True:
					try:
						first = float(input("\nKetik angka pertama: "))
						second = float(input("Ketik angka kedua: "))
						arr_func[i](first, second)
						break
					except ValueError:
						cprint(
							"Invalid input! Please try again...\nThe input value must be an integer or decimal", c="r")
				# endwhile
			elif int(typed) == 7:
				cprint("\nCase-example:\n²log(4) = ?? --> 2 disebut basis dan 4 disebut numerus\nSyarat:\n• basis > 0 dan basis ≠ 1\n• numerus > 0\n", c="c")
				while True:
					try:
						basis = float(input("Masukkan nilai basis: "))
						numerus = float(input("Masukkan bilangan numerus: "))
						arr_func[i](basis, numerus)
						break
					except ValueError:
						cprint(
							"Invalid input! Please try again...\nThe input value must be an integer or decimal\n", c="r")
				# endwhile
			elif int(typed) == 8:
				cprint("\nCase-example:\nCarilah akar-akar persamaan ax²±bx±c dengan a,b,c dalam bil bulat atau bil desimal dan x anggota bilangan real\n", c="c")
				while True:
					try:
						a = Fraction(float(input("Masukkan nilai a: ")))
						b = Fraction(float(input("Masukkan nilai b: ")))
						c = Fraction(float(input("Masukkan nilai c: ")))
						arr_func[i](a, b, c)
						break
					except ValueError:
						cprint(
							"Invalid input! Please try again...\nThe input value must be an integer or decimal\n", c="r")
				# endwhile

def main():
	print("Calculator Program\nby rayhan.frdh\n")
	print("Opsi:\n1. Pertambahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Perpangkatan\n6. Modulo (sisa pembagian)\n7. Logaritma\n8. Akar pers. kuadrat\n")

	choose()

	# kode meminta validasi user apakah ingin menjalankan ulang
	rerun = input("\nUlang program? (Y/N): ").upper()
	if rerun == "Y":
		main()
	else:
		print("\nThank you for using this program.")

if __name__ == "__main__":
	main()