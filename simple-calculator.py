#non-gui
#shell/terminal mode

import math

def addition():
  first = int(input("Type first number: "))
  second = int(input("Type second number: "))
  result = first + second
  print(f"The result of {first}+{second} is {result}")

def substraction():
  first = int(input("Type first number: "))
  second = int(input("Type second number: "))
  result = first - second
  print(f"The result of {first}-{second} is {result}")
  
def multiplication():
  first = int(input("Type first number: "))
  second = int(input("Type second number: "))
  result = first * second
  print(f"The result of {first}×{second} is {result}")
  
def division():
  first = int(input("Type first number: "))
  second = int(input("Type second number: "))
  result = first / second
  print(f"The result of {first}:{second} is {result}")
  
def powered():
  first = int(input("Type first number: "))
  second = int(input("Type second number: "))
  result = first ** second
  print(f"The result of {first}^{second} is {result}")

def mod():
  first = int(input("Type first number: "))
  second = int(input("Type second number: "))
  result = first % second
  print(f"The result of {first}mod{second} is {result}")

def main():
  print("Simple Calculator Program\nby rayhan.frdh\n")
  print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Powered by\n6. Mod by\n")
  
  arr_typed = ["1", "2", "3", "4", "5", "6"]
  typed = input("Type one off all: ")
  
  if typed not in arr_typed:
    print("Your input is wrong")
  else:
    if typed == "1":
      addition()
    elif typed == "2":
      substraction()
    elif typed == "3":
      multiplication()
    elif typed == "4":
      division()
    elif typed == "5":
      powered()
    elif typed == "6":
      mod()
    
  #kode meminta validasi user apakah ingin menjalankan ulang
  rerun = input("Ulang program? (Y/N): ")
  if rerun == "Y" or rerun == "y":
    main()
  if rerun == "N" or rerun == "n":
    print("\nThank you for using this program.")
main()
