llista1 = []
longitud = 0
# Bucle per demanar la mida de la llista fins que sigui vàlida
while longitud < 2 or longitud > 10:
    numero = input("Introdueix un número entre 2 i 10, els dos inclosos: ")
    # Comprovem que sigui un número enter
    if numero.isdigit():  
        longitud = int(numero)
        if longitud < 2 or longitud > 10:
            print("Has introduit un número que no esta entre 2 i 10")
    else:
        print("Has d'introduir un número.")

# Bucle for per posar elements, amb un while aniuat per validar cada element
for i in range(longitud):
    valid = False
    while not valid:
        valor = input(f"Introdueix el valor #{i+1}: ")
        # Només acceptem enters positius
        if valor.isdigit():
            #afegim el valor a la llista que abans estava buida  
            llista1.append(int(valor))
            valid = True
        else:
            print("Has d'introduir un número enter positiu.")
# Mostrar la llista
print(f"\nLlista: {llista1}")
# suma tots els caracters de la llista
suma = sum(llista1)
print(f"Suma: {suma}")
# recorre tota la llista i multiplica els caracters que estan dins d'ella
# comença amb 1 perque sino multiplicaria per 0
multiplicacio = 1
for n in llista1:
    multiplicacio *= n
print(f"Multiplicació: {multiplicacio}")