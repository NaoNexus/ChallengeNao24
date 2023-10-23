import random # importiamo una libreria di numeri casuali

# -- doc
"""
Nome programma: Vettore_casuale.py
Descrizione: vettore di numeri casuali 
Autore: Giacomo Santi
"""

# -- start
nome_programma = "Vettore_casuale.py"
print("Inizio esecuzione", nome_programma)


# -- input
n = 10
v = [] # vettore / lista 

# -- execute
for i in range(0, n):
    v.append (random.randint(1, 99)) # == funzione che ci permette di estrarre un numero casuale intero 

v.sort() # == ordino il vettore v

# -- output
print(v)
print("La dimensione è: ", len(v))

print("Il primo elemento è", v[0])
print("L'ultimo elemento è", v[-1])

print("I primi tre elementi :", v[0: 3]) # estraggo i pimi tre elementi

# -- end
print("Fine esecuzione", nome_programma)

