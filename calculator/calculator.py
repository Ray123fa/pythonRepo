#non-gui
#shell/terminal mode

from my_function import *
from cprint import cprint

def main():
  print("Simple Calculator Program\nby rayhan.frdh\n")
  print("Opsi:\n1. Pertambahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Perpangkatan\n6. Modulo (sisa pembagian)\n7. Logaritma\n8. Akar pers. kuadrat\n")
  
  arr_typed = ["1", "2", "3", "4", "5", "6", "7", "8"]
  typed = input("Pilih salah satu dari opsi: ")
  
  if typed not in arr_typed:
    cprint("Not an Option!", c="y")
  else:
    cprint("\nGunakan tanda titik untuk menginput bilangan desimal.\nExample: 0,85 => 0.85", c="g")
    
    arr_func = [addition, substraction, multiplication, division, powered, mod, logarithm, quadratic_eq]
    i = int(typed)-1
    if typed in arr_typed[i]:
      arr_func[i]()
    
  #kode meminta validasi user apakah ingin menjalankan ulang
  rerun = input("\nUlang program? (Y/N): ")
  if rerun == "Y" or rerun == "y":
    main()
  if rerun == "N" or rerun == "n":
    print("\nThank you for using this program.")
main()
