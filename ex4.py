#Escriviu un programa que donada una llista de strings, no ha de ser introduïda per teclat,
# ens digui quants elements hi ha a la llista de longitud més gran o igual que 2,
# i comenci per ‘a’. Mostrar per pantalla el resultat.
llista = ['abc', 'xyz', 'aba', '1221', 'a']
# Inicialitzem el comptador
i = 0
# Recorrem la llista
for element in llista:
    # si la longitud es igual o inferior a 2 i comença l'index de cada clau per a minuscula
    # se li suma 1 al contador
    if len(element) >= 2 and element[0].lower() == 'a':  
        i += 1

# Mostrar resultat
print(f"Hi ha {i} elements")