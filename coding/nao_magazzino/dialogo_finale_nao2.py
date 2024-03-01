def carenza(where, product_name):
    dove = where
    cosa = product_name

    if dove == "scaffale":
        return "È terminato " + product_name + " sullo scaffale"

    elif dove == "magazzino":
        return "Il " + product_name + " è quasi terminato in magazzino"
    
    else:
        return ""


dove = input()
cosa = input()

dialogo = carenza(dove, cosa)
print(dialogo)
