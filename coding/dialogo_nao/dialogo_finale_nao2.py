def carenza(where, product_name):
    dove = where
    cosa = product_name

    if dove == "scaffale":
        return "È terminato " + product_name + " sullo scaffale"

    elif dove == "magazzino":
        return "Il " + product_name + " è quasi terminato in magazzino"
    
    else:
        return ""

print("Dove: ")
dove = input()

print("Cosa: ")
cosa = input()

dialogo = carenza(dove, cosa)
print(dialogo)
