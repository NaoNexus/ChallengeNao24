import re
def analizza_genere(frase):
    parole_chiave_maschili = ["fratello", "papà", "padre", "nonno", "amico", "fratello,", "papà,", "padre,", "nonno,", "amico,", "fratello.", "papà.", "padre.", "nonno.", "amico."]
    parole_chiave_femminili = ["sorella", "mamma", "madre", "nonna", "amica", "sorella,", "mamma,", "madre,", "nonna,", "amica,", "sorella.", "mamma.", "madre.", "nonna.", "amica."]

    # Tokenizza la frase in parole
    parole = frase.lower().split()  # Converto tutto in minuscolo per rendere la ricerca case-insensitive

    # Verifica la presenza di parole chiave maschili e femminili
    genere_maschile = any(parola in parole for parola in parole_chiave_maschili)
    genere_femminile = any(parola in parole for parola in parole_chiave_femminili)

    # Determina il risultato in base alla presenza di parole chiave
    if genere_maschile and not genere_femminile:
        return "male"
    elif genere_femminile and not genere_maschile:
        return "female"
    else:
        return ""

def estrai_eta(frase):
    # Utilizza un'espressione regolare per trovare un numero nella frase
    risposta = frase
    matches = re.findall(r'\b\d+\b', risposta)
    lista_numeri = len(matches)
    trovato = False
    for i in range(lista_numeri):
        if int(matches[i])<100:
            trovato = True
            return int(matches[i])
    if not trovato:
        return 0

def estrai_budget(frase):
    # Utilizza un'espressione regolare per trovare un numero nella frase
    risposta = frase
    matches = re.findall(r'\b\d+\b', risposta)
    lista_numeri = len(matches)
    trovato = False
    for i in range(lista_numeri):
        if int(matches[i])>=100:
            trovato = True
            return int(matches[i])
    if not trovato:
        return 0

def estrai_categoria(frase):
    parole_chiave_necklace = ["collana", "collane"]
    parole_chiave_ring = ["anello","anelli"]
    parole_chiave_bracelet = ["bracciale","bracciali", "braccialetto", "braccialetti"]
    parole_chiave_earring = ["orecchino","orecchini"]

    # Tokenizza la frase in parole
    parole = frase.lower().split()  # Converto tutto in minuscolo per rendere la ricerca case-insensitive

    if any(parola in parole for parola in parole_chiave_necklace):             #parola è una variabile temporanea
        return "necklace"
    elif any(parola in parole for parola in parole_chiave_ring):
        return "ring"
    elif any(parola in parole for parola in parole_chiave_bracelet):
        return "bracelet"
    elif any(parola in parole for parola in parole_chiave_earring):
        return "earring"
    else:
        return ""


if __name__ == "__main__":
    print("Buon pomeriggio, come posso aiutarti?")
    risposta1= str(input())
    gender  = str(analizza_genere(risposta1))
    age     = int(estrai_eta(risposta1))
    budget  = int(estrai_budget(risposta1))
    category= str(estrai_categoria(risposta1))

    profilo_utente = [gender, age, budget, category]
    posizioni_vuote = [pos for pos, val in enumerate(profilo_utente) if val == "" or val == 0]

    while len(posizioni_vuote)!=0:
        for i in range(len(posizioni_vuote)):
            if posizioni_vuote[i] == 0:
                print("posso chiederti per chi è il gioiello")
                risposta2 = str(input())
                gender = str(analizza_genere(risposta2))
                
            elif posizioni_vuote[i] == 1:
                print("E quanti ha?")
                risposta3 = str(input())
                age = int(estrai_eta(risposta3))
                
            elif posizioni_vuote[i] == 2:
                print("Avresti un budget specifico in mente per questo regalo?")
                risposta4 = str(input())
                budget = int(estrai_budget(risposta4))
                
            elif posizioni_vuote[i] == 3:
                print("E che genere di gioielli preferisce? Collane, bracciali, orecchini o anelli?")
                risposta5 = str(input())
                category = str(estrai_categoria(risposta5))
        
        profilo_utente = [gender, age, budget, category]
        posizioni_vuote = [pos for pos, val in enumerate(profilo_utente) if val == "" or val == 0]


    print(profilo_utente)
