from ejemplo import opcion_1
from ejemplo2 import opcion_2

def menu(a):
    if a == 1:
        opcion_1()
    elif a == 2:
        opcion_2()
    else:
        print("incorrecto")

a = int(input("elije una opcion: "))
menu(a)