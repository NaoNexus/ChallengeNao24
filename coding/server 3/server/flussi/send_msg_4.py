'''
python2
'''

# Modules
import requests
import json

# Dati da inviare in formato JSON
data = {"id_cliente":1, "modalita_pagamento":"carta"}

# Specifica l'URL di destinazione
url = "http://127.0.0.1:5010/api/ordine/" + str(data)

# Invia la richiesta HTTP POST con i dati JSON
response = requests.post(url, json=data)

# Stampa la risposta
print(response.text)