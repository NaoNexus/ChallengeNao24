def dialogo1():
    return "Hai preferenze tra collane, bracciali e pendenti? O pensavi a qualcosa di più piccolo come orecchini o anelli?"

#Collane

def dialogo_collane():
    return "Perfetto! Abbiamo la collana Eleganza Radiante, realizzata in oro 18 carati con diamanti per un tocco di lusso, oppure la collana Cuore di Rubini con un cuore incastonato in oro giallo 18 carati e rubini per un design più romantico. Quale le piace di più?"

def scelta_collane():
    return "Ottimo, (eccola qui). Posso consigliarle qualcos'altro o vuole procedere all'acquisto"


#Bracciali

def dialogo_bracciali():
    return "Perfetto! Abbiamo il bracciale Stellare Brillanza in acciaio inossidabile con zirconi bianchi per un look luminoso, oppure il bracciale Fiori di Luce con dettagli floreali e zirconi cubici. Quale le piace di più?"

def scelta_bracciale():
    return "Ottimo, (eccola qui). Posso consigliarle qualcos'altro o vuole procedere all'acquisto"


#orecchini

def dialogo_orecchini():
    return "Perfetto! Gli orecchini Cristallo Azzurro in argento sterling con cristalli blu per un tocco di eleganza, oppure gli orecchini Brillante Splendore con cristalli Swarovski per un look scintillante. Quale le piace di più?"

def scelta_orecchini():
    return "Ottimo, (eccola qui). Posso consigliarle qualcos'altro o vuole procedere all'acquisto"


#anelli

def dialogo_anelli():
    return "Eccellente! Abbiamo l'Anello Sinfonia di Smeraldi in oro rosa 14 carati con smeraldi per un tocco di eleganza, oppure l'Anello Serenità Diamante in platino con un diamante taglio brillante al centro per uno stile raffinato. Quale le piace di più?"

def scelta_anelli():
    return "Ottimo, (eccola qui). Posso consigliarle qualcos'altro o vuole procedere all'acquisto"


#pendenti

def dialogo_pendenti():
    return "Ottimo! Abbiamo il Pendente Luna Incantata in oro bianco 14 carati con una perla di Tahiti per un tocco raffinato, oppure il Pendente Gioiello d'Amore in oro bianco 18 carati con diamante e zaffiro per un design romantico. Quale le piace di più?"

def scelta_pendenti():
    return "Ottimo, (eccola qui). Posso consigliarle qualcos'altro o vuole procedere all'acquisto"


#fine---------------

def scelta():
    return "Ottimo, (eccola qui). Posso consigliarle qualcos'altro o vuole procedere all'acquisto?"

def cassa():
    a =  ', '.join(map(str, carrello))
    return "Il suo carrello è composto da: {}".format(a)



carrello = []

while True:
    print(dialogo1())
    risposta1 = input()
    
    if risposta1 == "collane":
        print(dialogo_collane())
        collane1 = input()
        carrello.append(collane1)
        print(scelta())
        risposta = input()
        if risposta == "si":
            continue
        else:
            print(cassa())
            break
        
    elif risposta1 == "bracciali":
        print(dialogo_bracciali())
        bracciali1 = input()
        carrello.append(bracciali1)
        print(scelta())
        risposta = input()
        if risposta == "si":
            continue
        else:
            print(cassa())
            break
        
    elif risposta1 == "orecchini":
        print(dialogo_orecchini())
        orecchini1 = input()
        carrello.append(orecchini1)
        print(scelta())
        risposta = input()
        if risposta == "si":
            continue
        else:
            print(cassa())
            break
        
    elif risposta1 == "anelli":
        print(dialogo_anelli())
        anelli1 = input()
        carrello.append(anelli1)
        print(scelta())
        risposta = input()
        if risposta == "si":    
            continue
        else:
            print(cassa())
            break
        
    elif risposta1 == "pendenti":
        print(dialogo_pendenti())
        pendenti1 = input()
        carrello.append(pendenti1)
        print(scelta())
        risposta = input()
        if risposta == "si":
            continue
        else:
            print(cassa())
            break
        
    

