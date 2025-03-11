from fonction import *

print("\t\t\tCALCULATRICE")
print("Opérateurs : \n 1- Addition(+) \n 2- Soustraction(-) \n 3- Multiplication(*) \n 4- Division(/) \n")

a = int(input("Value1 >>> "))
operation = int(input("Choisissez un opérateur (entre parenthèse) >>> "))
b = int(input("Value2 >>> "))

if operation == 1 :
    print(f"Résultat = {addition(a, b)}")
elif operation == 2 :
    print(f"Résultat = {soustraction(a, b)}")
elif operation == 3 :
    print(f"Résultat = {multiplication(a, b)}")
elif operation == 4 :
    print(f"Résultat = {division(a, b)}")
else :
    print("Cet opérateur n'est pas encore prise en compte !")

