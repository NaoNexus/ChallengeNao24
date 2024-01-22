import re
def analizza_genere(frase):
    parole_chiave_maschili = ["fratello", "papà", "padre", "nonno", "amico", "fratello,", "papà,", "padre,", "nonno,", "amico,", "fratello.", "papà.", "padre.", "nonno.", "amico.""]
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
    match_numero = re.search(r'\b\d+\b', frase)

    # Verifica se è stato trovato un numero
    if match_numero:
        eta = int(match_numero.group())
        return eta
    else:
        return None  # Restituisci None se non viene trovato nessun numero


def estrai_budget(frase):
    # Utilizza un'espressione regolare per trovare un numero nella frase
    match_numero = re.search(r'\b\d+\b', frase)

    # Verifica se è stato trovato un numero
    if match_numero:
        budget = int(match_numero.group())
        return budget
    else:
        return None  #non è stato trovato nessun budget


def estrai_categoria(frase):
    parole_chiave_necklace = ["collana", "collane"]
    parole_chiave_ring = ["anello","anelli"]
    parole_chiave_bracelet = ["bracciale","bracciale", "braccialetto", "braccialetti"]
    parole_chiave_earring = ["orecchino","orecchini"]

    # Tokenizza la frase in parole
    parole = frase.lower().split()  # Converto tutto in minuscolo per rendere la ricerca case-insensitive

    if any(parola in parole for parola in parole_chiave_necklace):             #parola è una variabile temporanea
        return "necklace"
    elif any(parola in parole for parola in parole_chiave_ring):
        return "ring"
    elif any(parola in parole for parola in parole_chiave_braelet):
        return "bracelet"
    elif any(parola in parole for parola in parole_chiave_earring):
        return "earring"


if __name__ == "__main__":
    #domanda1
    print("posso chiederti per chi è il gioiello")
    risposta1 = str(input())
    gender = str(analizza_genere(risposta1))
    #print (gender)

    #domanda2
    print("E quanti ha?")
    risposta2 = str(input())
    age = int(estrai_eta(risposta2))
    #print(type(age))

    #domanda3
    print("Avresti un budget specifico in mente per questo regalo?")
    risposta3 = str(input())
    budget = int(estrai_budget(risposta3))
    #print(budget)

    #domanda4
    print("E che genere di gioielli preferisce? Collane, bracciali, orecchini o anelli?")
    risposta4 = str(input())
    category = str(estrai_categoria(risposta4))
    #print(category)



    profilo_utente = [gender, age, budget, category]
    print(profilo_utente)


