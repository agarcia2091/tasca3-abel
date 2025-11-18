#Fes un programa que demana un número per teclat, no avança fins que no és un número, 
# i suma aquest número introduït per teclat a tots els elements de la llista llista=[1,2,3,4,5,6,7,8,9,10] 
# utilitzant un bucle for. Cal modificar la llista original.
llista=[1,2,3,4,5,6,7,8,9,10]
numeric = False
num = 0
num = input("Introdueix un número: ")
while not numeric:
    if num.isdigit():
        num = int(num)
        for i in range(len(llista)):
            llista[i] += num
            numeric = True
        print(llista)
    else:
        print("Introdueix un numero, no una cadena")
        num = input("Introdueix un número: ")
