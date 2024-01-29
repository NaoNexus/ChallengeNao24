import re
import random

#descrizione prodotti
def Angelic_bracelet():
    return "L Angelic_bracelet  e un classico intramontabile. Il braccialetto rodiato propone una fila di Clear Crystal a taglio circolare, ognuno incorniciato dal pave e di Clear Crystal. Il gioiello si abbina perfettamente agli altri accessori della collezione Angelic. Il bracciale appartiene alla collezione Angelic, con cristalli e placcato in rodio"

def Angelic_necklace():
    return "L angelic necklace  e un raffinato collier si abbina perfettamente ad altre creazioni dell apprezzatissima linea Angelic Swarovski. Ideale per le occasioni speciali e da regalare,  e interpretato in Clear Crystal e metallo rodiato lucido. Questa collana appartiene alla collezione Angelic, con cristalli e placcato in rodio"

def Constella_cocktail_ring():
    return "Il Constella cocktail ring  e un anello Constella, testimone della potenza della semplicita,  e un must del guardaroba. Risultato di una sapiente lavorazione, la pietra centrale dal taglio Princess ruba la scena ed  e valorizzata da un elegante pave e sulla galleria e dalla fascia placcata rodio. Indossalo da solo perch e brilli in tutto il suo splendore. L anello  appartiene alla collezzione Constella, con   e placcatura in rodio"

def Dad_bracelet():
    return "Il dad bracelet  e placcato rodio ed  e un regalo ideale per la Festa del Papa. Al centro, la parola “PAPA”  e messa in rilievo con un delicato pave e di cristalli, mentre la massiccia catena a maglie presenta un estensore che garantisce una vestibilita perfetta. Pensato per questo giorno speciale, ma non solo, questo gioiello  e disponibile nelle dimensioni L e XL. Il bracciale appartiene alla collezione Mothers day, con cristalli e placcatura in rodio"

def Dancing_swan_necklace():
    return "Simbolo di graziosa eleganza e nobilta, il cigno  e l icona ideale per i gioielli Swarovski. Questa collana presenta uno splendido set di cigni con numerose pietre bianche scintillanti. Al centro risiede un “dancing element” che brilla luminoso. Questa collana rodiata  e un regalo affascinante per una persona speciale. Questa collana appartiene alla collezione Dancing Swan, con cristalli, placcatura in rodio e zirconi"

def Dextera_bracelet():
    return "Dettagli intricati incontrano una costruzione audace in questo moderno braccialetto della famiglia Dextera. Impreziosito dalla nostra celebre tecnica del pave e, presenta file di cristalli grigio-argento incastonati in una montatura placcata rutenio nero. Indossalo da solo o impilato, a seconda del tuo umore e del tuo outfit. Il bracciale appartiene alla collezione Dextera con cristalli e placcatura in rutenio"

#def Dextera_hoop_earrings():
#    return "Un tocco moderno ai classici orecchini a cerchio, questo paio genderless conferira dinamismo a qualsiasi outfit. Il design scultoreo celebra l iconica tecnica pave e di Swarovski con cristalli luccicanti laminati incastonati in una montatura placcata rodio. Questo duo  e adatto di giorno ma perfetto anche per la sera. Parte della famiglia Dextera, questi orecchini sono ideati dalla Direttrice Creativa Giovanna Engelbert per la Collection II. Questi orecchini fanno parte della collezione Dextera con cristalli e placcatura in rodio"

def Dextera_necklace():
    return "Ispirata alla nostra tradizione industriale, questa collana a tutto tondo raggiunge l equilibrio tra audace e raffinato. Caratterizzato da pave e di cristalli grigio argento e catene intrecciate,  e rifinito con una montatura placcata rutenio. Indossalo con altri pezzi della famiglia Dextera per un look audace. Questa collana appartiene alla collezione Dextera con cristalli e placcatura in rutenio"

def Florere_necklace():
    return "Sublima il tuo stile con la bellezza luminosa della natura. Questa brillante collana della famiglia Florere  e realizzata con un fiore che sboccia, creato dalla combinazione di placcatura in tonalita oro e cristalli rosa sfaccettati. Il pendente  e disposto su una catena scorrevole con una singola pietra splendente all estremita. Indossa questo bellissimo gioiello per sprigionare la gioia primaverile. La collana appartiene alla collezione Florere, con zirconi e placcatura in rodio"

def Florere_stud_earrings():
    return "Ispirato dalla meravigliosa bellezza della natura, questo gioiello luminoso sboccia con gli eleganti cristalli. Caratterizzati da una montatura placcata color oro, cinque petali rosa sono disposti attorno ad una pietra dalla tonalit a pi u scura. Scegli questi orecchini per illuminare la tua giornata. QUesti orecchini appartengono alla collezione Florere, con zirconi e placcatura color oro"

#def Gema_bracelet():
#    return "Questo gioioso braccialetto prismatico della famiglia Gema presenta uno scintillante mix di cristalli nelle pi u belle tonalit a pastello su una raffinata montatura rodiata. L abbagliante gamma di tagli e colori  e organizzata in modo organico, ma preciso, dando vita a un pezzo di inaspettata bellezza. Indossa questo braccialetto da solo o con i gioielli Gema abbinati per dare vivacit a alla tua quotidianit a. Questo bracciale appartiene alla collezione Gema, con cristalli e placcatura in rodio"

def Gema_drop_earrings():
    return "Questi orecchini a buco Gema di un lussureggiante savoir-faire infonderanno in ogni tuo outfit tutta la bellezza della natura. Il mix di cristalli multicolor  e disposto in maniera originale ma rigorosa su una raffinata montatura placcata rodio che fa risplendere ogni sfumatura. Da abbinare a una collana della famiglia Gema o da indossare da soli per un effetto glamour disinvolto al calar della notte. Questi orecchini appartengono alla collezione Gema, con cristalli e placcatura in rodio"

def Gema_necklace(): 
    return "Gioiello davvero spettacolare della famiglia Gema, questa straordinaria collana  e realizzata con una serie di sfavillanti cristalli in un mix di tagli e colori. Questo gioiello regala gioia e migliora subito l umore in qualsiasi modo tu decida di indossarlo. Questa collana fa parte della collezione Gema, con cristalli e placcatura in rodio"

def Matrix_drop_earrings():
    return "Questi versatili orecchini della famiglia Matrix si potranno indossare in due modi diversi. Il design placcato rodio presenta orecchini a lobo con Swarovski  zirconi rettangolari verdi e orecchini jacket con un  elegante goccia realizzata con cristalli Cry rotondi e uno Swarovski  zirconi rettangolare verde all  estremit a. Gli orecchini jacket hanno tre fori per regolarne la lunghezza. Inoltre, potrai anche staccarli per indossare solamente gli orecchini a lobo. Un gioiello straordinario che aggiunger a un immediato tocco glamour ad ogni stile. Questi orecchini fanno parte della colazione Matrix, con zirconi e placcatura in rodio"

def Matrix_ring():
    return "Combinando un profondo aspetto metallico con una lucentezza accattivante, questo anello Matrix costituir a un aggiunta versatile al tuo portagioielli. In un processo che unisce scienza e magia, le pietre grigie con taglio baguette Princess sono incastonate su una fascia placcata rutenio. Un accessorio accattivante, perfetto da impilare, che consente molteplici combinazioni per tutte le occasioni. Questo anello fa parte della collezione Matrix, con cristalli e placcatura in rutenio"

def Matrix_stud_earrings():
    return "Semplici ma affascinanti, questi borchie della famiglia Matrix offrono stile. Gli zirconi Swarovski rettangolari verde brillante sono inseriti in una raffinata montatura a doppia griffe placcata nella tonalit a oro. Scegli questi orecchini sfaccettati per un tocco di verde da far girare la testa. Questi orecchini fanno parte della collezione Matrix, con zirconi e placcatura color oro"

#def Matrix_tennis_necklace():
#    return "Combinando l eleganza classica con un tocco contemporaneo, questa collana da tennis Matrix  e allo stesso tempo raffinata e lussuosa. Un design a tutto tondo di pietre rotonde chiare  e intervallato da pietre rettangolari in verde intenso, illuminate da una montatura placcata rodio. Questo pezzo aggiunger a glamour immediato a qualsiasi look celebrativo e sar a anche un regalo memorabile. Questa collana fa parte della collezione Matrix, con zirconi e placcatura in rodio"

def Mesmera_bracelet():
    return "Questo sorprendente braccialetto rigido mette in risalto le qualita ipnotiche della famiglia Mesmera. Innovativi grappoli di cristalli sono sapientemente disposti a forma di mosaico, che nasconde abilmente la montatura delle griffe placcate rodio. Indossalo come una dichiarazione diurna con le maniche della camicia arrotolate o come un semplice abito a trapezio per la sera; sia stravagante che senza tempo in egual misura. Questo braccialetto fa parte della famiglia Mesmera, disegnata dal Direttore Creativo Giovanna Engelbert per la Collezione I. Come chiuderlo e aprirlo(): posiziona la bacchetta arrotondata nel punto pi u largo del foro opposto e falla scorrere fino al punto pi u basso. Una volta in posizione, abbassare il fermo di sicurezza con anello a D sulla parte superiore per garantire il fissaggio. Per aprire, sollevare il fermo di sicurezza con anello a D e far scorrere il bastone verso il punto pi u largo per rilasciare. Questo bracciale fa parte della collezione Mesmera, con cristalli e placcatura in rodio"

def Mesmera_cocktail_ring():
    return "Scenografico ma raffinato, questo anello dal motivo audace racchiude la forza ipnotica della famiglia Mesmera. Caratterizzato da un classico cristallo taglio Octagon al centro, questo gioiello senza tempo presenta un  elegante placcatura in rodio. Indossalo da solo o con altri anelli per un look da sera che non passer a inosservato. Parte della famiglia Mesmera, questo anello  e firmato dal Direttore Creativo Giovanna Engelbert per la Collection I. Questo anello fa parte della collezione Mersmera con cristalli e placcatura in rodio"

def Mesmera_necklace():
    return "Accendi il tuo stile con i dettagli drammatici di questa collana Mesmera. Realizzato per un lusso stravagante, il design rodiato  e stato realizzato con una gamma completa di cristalli sfaccettati. I tagli e le dimensioni misti sono un omaggio al rinomato savoir-faire di Swarovski, regalandoti un gioiello meraviglioso e ipnotico. Regalalo a una persona cara come scelta definitiva. Questa collana fa parte della collezione Mesmera, con cristalli e placcatura in rodio"

def Millenia_cocktail_ring():
    return "Indossato da solo o impilato, questo anello da cocktail Millenia catturer a sicuramente l attenzione. Abbagliante con un unica pietra taglio pera,  e incastonato su una fascia rodiata impreziosita da pave e per uno stile disinvolto e chic. Questo anello fa parte della collezione Millenia, con zirconi e placcatura in rodio"

#def Millenia_necklace():
#    return "Delicata e splendidamente raffinata, questa collana di cristalli grigi diventer a il tuo nuovo punto di riferimento. Presentando cristalli a taglio quadrato racchiusi in un elegante montatura placcata in rutenio nero, la sua silhouette fluida e lunga  e perfetta da abbinare ad altri pezzi o da avvolgere due volte attorno al collo per un doppio effetto. Indossalo per compensare una semplice maglietta bianca o una camicia su misura. Questa collana fa parte della famiglia Millenia, disegnata dal Direttore Creativo Giovanna Engelbert per la Collezione II. Come chiuderlo e aprirlo(): far scorrere i ganci nei fori corrispondenti alla base della pietra terminale e spingere per farli scattare in posizione. Fissare la catena di sicurezza utilizzando la piccola chiusura a leva. Per aprire, slacciare la catena di sicurezza e premere contemporaneamente i pulsanti su entrambi i lati della pietra per rilasciare i ganci. Questa collana fa parte della collezione Millenia, con cristalli e placcatura in rutenio"

def Stella_drop_earrings():
    return "Sei nato per brillare. Prova questi squisiti orecchini pendenti ispirati alle stelle della famiglia Stella. Impreziositi da pietre taglio aquilone in raffinate montature a griffe, questi eleganti modelli sono rifiniti con placcatura nella tonalit a oro rosa. Abbinali ad altri meravigliosi design per creare un look unico come te. Questi orecchini fanno parte della collezione Stella, con zirconi e placcatura color oro rosa"

def Stella_necklace():  
    return "Fai miracoli in questo bellissimo ciondolo della famiglia Stella. Presentando un elegante combinazione di perle di cristallo e pietre scintillanti rifinite con placcatura nella tonalit a oro rosa, questo design asimmetrico far a sicuramente girare la testa ovunque lo indossi. Modellalo da solo e preparati a brillare. Questa collana fa parte della collezione Stella, con perle di cristalli e zirconi"

def Stella_stud_earrings(): 
    return "Questi orecchini da sogno sono come la luce nell oscurit a. Parte della famiglia Stella, questo design scintillante offre un elegante mix di pietre brillanti a taglio rotondo e una perla di cristallo centrale rifinita con placcatura nella tonalit a oro rosa. Illumineranno ogni look, sia che li indossi in una pila di orecchie o che li lasci brillare da soli. Questi orecchini fanno parte della collezione stella, con perle di cristalli e zirconi"

def Stone_hoop_earrings():
    return "Il gioiello perfetto, indispensabile per la tua collezione. Realizzati in metallo rodiato, questi orecchini a cerchio brillano di lucentezza grazie al pave e chiaro. Un look minimal, da indossare da solo o da studiare per creare uno stile ancora pi u stravagante. Abbinandosi facilmente a qualsiasi outfit, questi orecchini ti accompagneranno nell  arco di tutta la giornata. Questi orecchini fanno parte della collezione Stone, con cristalli e placcatura in rodio"
 
def Swarovski_iconic_swan_earring_jackets():
    return "Raffinati e versatili, gli earring jackets placcati oro rosa riprendono il motivo del cigno, icona-simbolo Swarovski. La delicatezza del pave e di cristallo nero connota i gioielli di una luminosit a discreta. Indossati soli definiscono uno stile ricercato, mentre l  aggiunta degli elementi con Crystal Pearl rende gli orecchini pi u attuali.  Quesi orecchini fanno parte della collezione Iconic Swan, con cristalli e perle di cristali"
 
def Swarovski_iconic_swan_pendant():
    return "L elegante pendente rodiato sfoggia l  iconico motivo a cigno Swarovski. La delicatezza dei superlativi cristalli neri fissati con lesclusiva tecnica Pointiage  connota il gioiello di una luminosit a discreta, perfetta da abbinare alle mise formali o casual. Il pendente misura 1 x 1 cm ed  e abbinato ad una catena di 38 cm. Per interpretare l  attualit a dello stile multi metallo indossate il gioiello con lo stesso modello in versione placcata oro rosa. Questa collana fa parte della collezione Iconic Swan, con cristalli e placcatura in rodio"

def Swarovski_swan_stud_earrings():
    return "L iconico Cigno Swarovski prende forma elegantemente in questo paio di orecchini a lobo. Realizzato con le ali in alto, pronto a spiccare il volo, il cigno  e decorato con pave e di scintillanti cristalli trasparenti su una brillante placcatura rodio. Scegli questo gioiello per un delicato tocco di ispirazione quotidiana. Questi orecchini fanno parte della collezione Iconic Swan, con cristalli e placcatura in rodio"

def Vittore_ring():
    return "Questo anello Vittore  e ideale per un sottile tocco di glitter. Combina il classico abbinamento di cristalli Cry dal taglio Round con una finitura color oro e ti conferir a un look raffinato e lussuoso. Realizzato per brillare su tutti i lati, potrai indossare questo gioiello con altri stili, come, ad esempio, un affascinante anello cocktail, per un contrasto efficace. Questo anello fa parte della collezione Vittore, con zirconi"

#---


def Luna_drop_earrings():
    return "Gli orecchini Luna combinano ispirazione lunare e stile sfavillante. Placcati in rodio, presentano eleganti mezzelune impreziosite da cristalli di cinque dimensioni, creando un sofisticato effetto pavé. Parte della famiglia Luna, questi gioielli sono adatti per ogni occasione, offrendo una scelta disinvolta. Il placcaggio rodio garantisce una lucentezza duratura e il design versatile si adatta a diversi outfit, rappresentando un elegante dichiarazione di stile."


def Meteora_drop_earrings():
    return "Gli orecchini Meteora, ispirati al cosmo, arricchiscono il tuo stile con un tocco di meraviglia. Placcati in rodio, presentano catenine pendenti con motivi a cupola a forma di meteora, splendidamente impreziositi da cristalli Cry rotondi. Questi orecchini rappresentano una dichiarazione di eleganza semplice ma potente, aggiungendo luminosita al viso e un tocco di magia a ogni look. Una scelta facile per illuminare il tuo stile quotidiano con la brillantezza distintiva di Swarovski."


def Lucent_hoop_earrings():
    return "Gli orecchini a cerchio Lucent in rosa sono un esempio lampante di cristallo saturo di colore completamente sfaccettato. Creati con maestria, questi orecchini sono rifiniti con una sottile chiusura a perno e sono versatili per qualsiasi outfit, dal casual all elegante. Parte della linea Lucent, sono un eccellente interpretazione del lusso sportivo firmato dalla Direttrice Creativa Giovanna Engelbert. La loro versatilita li rende adatti a molteplici occasioni, trasformando ogni giorno in un opportunita per brillare con la distintiva brillantezza Swarovski."


def Dxtera_hoop_earrings():
    return "Gli orecchini a cerchio intrecciati Dextera presentano due anelli tubolari placcati rodio, di cui uno impreziosito da pavé all-over. Con un tocco asimmetrico, gli anelli sono disposti in modo diverso su ciascun gioiello. La possibilita di rimuovere il secondo cerchio offre una versatilita unica, permettendo di personalizzare il look a seconda dell occasione. Oltre a essere una dichiarazione di stile, questi orecchini offrono una soluzione creativa e elegante per esprimere la propria individualita."


def Luna_cocktail_ring():
    return "L anello Luna cattura la magia della luna con una cupola in pavé di cristalli Cry. Il design placcato rodio, elegante e affascinante, si presenta come un elegante mezzaluna. La sua versatilita lo rende adatto a diverse fasi del tuo stile, illuminando con riflessi ogni outfit. Un gioiello che trasforma ogni gesto in un affermazione di eleganza, l anello Luna e un compagno luminoso per ogni occasione."


def Angelic_necklace():
    return "Il raffinato collier Angelic Swarovski si abbina perfettamente ad altre creazioni della linea. Ideale per occasioni speciali, e realizzato in Clear Crystal e metallo rodiato lucido. Con un design senza tempo, questo collier e un regalo prezioso e un elegante dichiarazione di stile, aggiungendo un tocco di grazia e brillantezza a qualsiasi look."


def Florere_cocktail_ring():
    return "Lo sfavillante anello Florere con motivo floreale e un esempio brillante del savoir-faire di Swarovski. Il design a doppio gambo, placcato in tonalita oro, si adatta confortevolmente al dito, con petali straordinari impreziositi da cristalli rosa di varie dimensioni. Pensato per essere il protagonista della scena, questo anello aggiunge una nota affascinante a qualsiasi look, offrendo una combinazione unica di eleganza e stile floreale."


def Stilla_necklace():
    return "Indossa la collana Stilla per sublimare il tuo stile con gocce di colore brillante. Realizzata con una montatura placcata oro e una chiusura a moschettone, la collana presenta tagli di Swarovski Zirconia in sette colori complementari. Ogni pietra e circondata da cristalli quadrati piu piccoli, creando una collana che continua a brillare. Combina questa eclettica collana con eleganti orecchini della stessa famiglia o regalala a una persona cara per un tocco di eleganza vibrante."


def Matrix_tennis_necklace():
    return "Risplendi con la collana Matrix Tennis, caratterizzata da una fila di brillanti pietre rotonde gialle. Ogni pietra e incastonata in una catena placcata oro con una chiusura sicura e raffinata. Questo gioiello diventera un accessorio essenziale per il tuo look quotidiano, aggiungendo una nota di lusso alla tua collezione con la sua brillante cascata di colori."


def Creativity_pendant():
    return "Il pendente Creativity e una rivisitazione contemporanea del classico pendente tondo. Realizzato con pavé di Clear Crystal e metallo rodiato, aggiunge una nota moderna e si indossa splendidamente sovrapposto con un pendente piu lungo. Con le sue dimensioni di 1,5 x 2 cm, e un aggiunta elegante e versatile alla tua collezione di gioielli, offrendo un tocco di brillantezza e stile contemporaneo."


def Gema_bracelet():
    return "Il bracciale Gema con sfumature blu ghiaccio e un aggiunta straordinaria a qualsiasi collezione di gioielli. Con un design placcato rodio che gioca con tagli e colori ispirati allo stile bohémien, questo bracciale e un opera d arte lussuosa e dal tocco disinvolto. Indossalo da solo per un glamour rilassato o sovrapponilo ad altri gioielli della stessa famiglia per un look speciale, offrendo un mix irresistibile di eleganza e originalita."


def Hyperbola_drop_earrings():
    return "Gli orecchini Hyperbola sono il mezzo perfetto per aggiungere un tocco passionale al tuo stile. Placcati in rodio, presentano un design tridimensionale con Swarovski Zirconia trasparenti e una pietra danzante blu a forma di cuore. Abbinati a un pendente coordinato, enfatizzano il glamour e l originalita, offrendo una dichiarazione audace di stile e personalita."


def Lucent_bangle():
    return "Il bracciale rigido ottagonale Lucent con cristallo verde acceso e un aggiunta elegante a qualsiasi outfit. La montatura rivestita in PVD oro e la chiusura magnetica innovativa lo rendono un accessorio versatile. Parte della linea Lucent, questo bracciale rigido e un opzione moderna e chic per la Collection III, offrendo un mix di stile geometrico e brillantezza vivace."


def Lucent_cocktail_ring():
    return "L anello Lucent, ispirato all iconico Swarovski Nirvana, e un capolavoro d impatto con una tonalita verde intensa. Con oltre 138 sfaccettature e una fascia metallica coordinata, puo essere indossato da solo o in abbinamento ad altri anelli per un effetto esplosivo di colore. Firmato dalla Direttrice Creativa Giovanna Engelbert, e parte della famiglia Lucent e della Collection I, offrendo un elegante dichiarazione di stile con una cascata di colore vibrante."


def Millenia_necklace():
    return "La vibrante collana Millenia e formata da cristalli taglio Octagon verdi, montati su una catena placcata oro distintiva. Aggiungi una cascata prismatica di colori al tuo look quotidiano, indossando questo gioiello su sfondi monocromatici. Firmata dalla Direttrice Creativa Giovanna Engelbert, fa parte della famiglia Millenia e della Collection I, offrendo un tocco distintivo di brillantezza e stile audace."


def Disney_mickey_mouse_pendant():
    return "In celebrazione dei 100 anni della Disney, il pendente placcato rodio raffigura Topolino aggrappato alla catena con il suo sorriso iconico. Un gioiello tridimensionale perfetto per chi ama l avventura e conserva il cuore di un bambino, offrendo un tocco giocoso e nostalgico di magia Disney."


def Crystalline_delight_watch():
    return "Chic e facile da indossare, l orologio Crystalline Delight di Swarovski brilla con circa 1.000 Clear Crystal. Il quadrante moderno, la cassa in acciaio inossidabile e il bracciale ispirato ai gioielli creano un accessorio elegante e resistente all acqua fino a 50 metri. Prodotto in Svizzera, e una perfetta fusione di stile e funzionalita, offrendo un tocco di lusso e brillantezza in ogni momento."


def Gema_necklace():
    return "La collana Gema offre uno stile unico con una varieta di tagli e colori vivaci. Realizzata con una catena placcata rodio, presenta cristalli di dimensioni e tagli straordinari, creando un affascinante armonia. Aggiungi gioia prismatica al tuo look indossando questa collana e abbinala ad altri gioielli Gema per un look irresistibile, offrendo un mix di colore vivace e stile distintivo."



#fine descrizione dei prodotto

def analizza_genere(frase):
    parole_chiave_maschili = ["maschio","fratello", "papà", "padre", "nonno", "amico","figlio", "fratello,", "papà,", "padre,", "nonno,", "amico,","figlio,", "fratello.", "papà.", "padre.", "nonno.", "amico.","figlio."]
    parole_chiave_femminili = ["femmina","sorella", "mamma", "madre", "nonna", "amica", "sorella,", "mamma,", "madre,", "nonna,", "amica,", "sorella.", "mamma.", "madre.", "nonna.", "amica.","figlia","figlia,","figlia."]

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
    parole_chiave_necklace = ["collana", "collane", "collana,", "collane,", "collana.", "collane."]
    parole_chiave_ring = ["anello","anelli", "anello,","anelli,", "anello.","anelli."]
    parole_chiave_bracelet = ["bracciale","bracciali", "braccialetto", "braccialetti", "bracciale,","bracciali,", "braccialetto,", "braccialetti,", "bracciale.","bracciali.", "braccialetto.", "braccialetti."]               
    parole_chiave_earring = ["orecchino","orecchini", "orecchino,","orecchini,", "orecchino.","orecchini."]
    parole_chiave_watch = ["orologio","orologio,","orologio."]
    
    category = ["necklace","ring","bracelet","earrings"]
    parola_chiave=["uguale","indifferente"]
    
    # Tokenizza la frase in parole
    parole = frase.lower().split()  # Converto tutto in minuscolo per rendere la ricerca case-insensitive

    if any(parola in parole for parola in parole_chiave_necklace):             #parola è una variabile temporanea
        return "necklace"
    elif any(parola in parole for parola in parole_chiave_ring):
        return "ring"
    elif any(parola in parole for parola in parole_chiave_bracelet):
        return "bracelet"
    elif any(parola in parole for parola in parole_chiave_earring):
        return "earrings"
    elif any(parola in parole for parola in parole_chiave_watch):
        return "watch"
    
    elif any(parola in parole for parola in parola_chiave):
        random_category = random.choice(category)
        return random_category
    else:
        return ""

#decizion tree
def recommend_jewelry(customer_info, product_info):
    
    gender = customer_info[0]
    age = customer_info[1]
    budget = customer_info[2]
    category = customer_info[3]

    '''
    name = primo_dizionario[list(primo_dizionario.keys())[1]]
    category = primo_dizionario[list(primo_dizionario.keys())[2]]
    storage = primo_dizionario[list(primo_dizionario.keys())[3]]
    '''
    
    # -- male
    if gender == 'male':

        if age > 60:
            return 0
        
        elif  age < 20: 

            if category == 'bracelet':
                
                if budget >= 155:
                    gioielli_consigliati = [6]
                    return gioielli_consigliati
                
                else:
                    return 0
            
            elif category == 'necklace':
                
                if budget < 175:
                    return 0
                
                else:
                    gioielli_consigliati = [8]
                    return  gioielli_consigliati
                
            else:
                return 0

        elif 20 <= age <= 60:
            
            if category == 'bracelet':
                
                if budget < 145:
                    return 0
                
                elif 145 <= budget < 155:
                    gioielli_consigliti = [4]
                    return gioielli_consigliati
                
                else: #(budget >= 155:)
                    gioielli_consigliati = [4, 6]
                    return gioielli_consigliati

            elif category == 'necklace':
                
                if budget < 175:
                    return 0
                
                else:
                    gioielli_consigliati = [8]
                    return gioielli_consigliati

            else:
                return 0

    # -- female
    elif gender == 'female':
    
        if 0 < age < 20:
            
            if category == 'bracelet':
        
                if budget >= 155:
                    gioielli_consigliati = [1]
                    return gioielli_consigliati
                
                else:
                    return 0
                    
            elif category == 'necklace':
                
                if budget < 125:
                    return 0
                    
                elif 125 <= budget < 155:
                    gioielli_consigliati = [31]
                    return gioielli_consigliati
                    
                elif 155 <= budget < 175:
                    gioielli_consigliati = [5,31]
                    return  gioielli_consigliati
                    
                elif 175 <= budget < 230:
                    gioielli_consigliati = [5,24,31]
                    return  gioielli_consigliati
                    
                elif budget >= 230:
                    gioielli_consigliati = [2,5,24,31]
                    return  gioielli_consigliati
                    
            elif category == 'earrings':
            
                if budget < 125:
                    return 0

                elif 125 <= budget < 135:
                    gioielli_consigliati = [25,26]
                    return  gioielli_consigliati
                    
                elif 135 <= budget < 155:
                    gioielli_consigliati = [23, 25, 26]
                    return  gioielli_consigliati

                else:
                    gioielli_consigliati = [23,7,25,26]
                    return  gioielli_consigliati
                    
            else:
                return 0
                    
        elif 20 <= age < 40:
        
            if category == 'bracelet':
                    
                if budget < 195:
                    return 0

                elif 195 <= budget < 215:
                    gioielli_consigliati = [11]
                    return  gioielli_consigliati

                else:
                    gioielli_consigliati = [11,32]
                    return  gioielli_consigliati
                    
            elif category == 'necklace':

                
                if budget < 75:
                    return 0

                elif 75 <= budget < 115:
                    gioielli_consigliati = [36]
                    return  gioielli_consigliati

                elif 115 <= budget < 175:
                    gioielli_consigliati = [36,28]
                    return  gioielli_consigliati
                    
                elif 175 <= budget < 195:
                    gioielli_consigliati = [36,28,35]
                    return  gioielli_consigliati

                else:
                    gioielli_consigliati = [36,28,35,13]
                    return  gioielli_consigliati
                    
            elif category == 'earrings':
                
                if budget < 89:
                    return 0

                elif 89 <= budget <125:
                    gioielli_consigliati = [34]
                    return gioielli_consigliati
                
                elif 125 <= budget < 129:
                    gioielli_consigliati = [34,27]
                    return  gioielli_consigliati

                elif 129 <= budget < 195:
                    gioielli_consigliati = [34,27,29]
                    return  gioielli_consigliati

                elif 195 <= budget < 300:
                    gioielli_consigliati = [34,27,29,12]
                    return  gioielli_consigliati
                    
                else:
                    gioielli_consigliati = [34,27,29,12,33]
                    return  gioielli_consigliati
            
            elif category == 'watch':
                
                if budget >= 300:
                    gioielli_consigliati = [22]
                    return gioielli_consigliati
                
                else:
                    return 0
        
            else:
                return 0
                    
        elif 40 <= age < 60:
        
            if category == 'necklace':
            
                if budget < 175:
                    return 0
                
                elif 175 <= budget < 250:
                    gioielli_consigliati = [9]
                    return  gioielli_consigliati

                elif 250 <= budget < 550:
                    gioielli_consigliati = [9,14]
                    return  gioielli_consigliati
                
                else:
                    gioielli_consigliati = [9,14,37]
                    return  gioielli_consigliati
                    
            elif category == 'earrings':
                    
                if budget < 95:
                    return 0

                elif 95 <= budget < 175:
                    gioielli_consigliati = [17]
                    return  gioielli_consigliati
                
                elif 175 <= budget < 195:
                    gioielli_consigliati = [17,38]
                    return  gioielli_consigliati

                elif 195 <= budget < 230:
                    gioielli_consigliati = [17,38,10,15]
                    return  gioielli_consigliati
                    
                else:
                    gioielli_consigliati = [17,38,10,15,39]
                    return  gioielli_consigliati
                    
            elif category == 'ring':
            
                if budget < 75:
                    return 0
                    
                elif 75 <= budget < 125:
                    gioielli_consigliati = [30]
                    return  gioielli_consigliati
                    
                elif 125 <= budget < 135:
                    gioielli_consigliati = [16,30]
                    return  gioielli_consigliati

                elif 135 <= budget < 175:
                    gioielli_consigliati = [16,30,3]
                    return  gioielli_consigliati

                elif 175 <= budget < 250:
                    gioielli_consigliati = [16,30,3,41]
                    return  gioielli_consigliati

                elif 250 <= budget < 400:
                    gioielli_consigliati = [16,30,3,41,40]
                    return  gioielli_consigliati
                    
                else:
                    gioielli_consigliati = [16,30,3,41,40,42]
                    return  gioielli_consigliati
                 
            else:
                return 0
                
        elif age >= 60:
        
            if category == 'bracelet':
                
                if budget < 400:
                    return 0
                
                else:
                    gioielli_consigliati = [18]
                    return  gioielli_consigliati
                    
            elif category == 'necklace':
            
                if budget < 950:
                    return 0
                    
                else:
                    gioielli_consigliati = [20]
                    return  gioielli_consigliati
                    
            elif category == 'ring':
                
                if budget < 135:
                    return 0
                    
                else:
                    gioielli_consigliati = [19,21]
                    return  gioielli_consigliati
                
            else:
                return 0

def get_product_name_by_id(product_info, target_product_id):
    product = next((product for product in product_info if product['id'] == target_product_id), None)
    if product:
        return product['name']

def Descrizione_prodotto(funzione_prodotto):
    if funzione_prodotto in globals() and callable(globals()[funzione_prodotto]):
        # Richiama la funzione
        result = globals()[funzione_prodotto]()
        return result

def estrai_si_no(frase):
    parole_chiave_no = ["no", "non mi piace", "non mi ispira", "no grazie","a posto cosi"] #chiedere se mettono le accentate
    parole_chiave_si = ["si", "mi piace", "si grazie"]      
    frase = frase.lower()
    
    if any(parola in frase for parola in parole_chiave_no):
        return "no"
    elif any(parola in frase for parola in parole_chiave_si):
        return "si"
    else:
        return ""

def funzione_abbinamento(product_name):
    abbinamenti = {
        'angelic necklace': 'stilla necklace',
        'creativity pendant': 'disney mickey mouse pendant',
        'crystalline delight watch': 'gema bracelet',
        'dextera hoop earrings': 'hyperbola drop earrings',
        'disney mickey mouse pendant': 'creativity pendant',
        'florere cocktail ring': 'luna cocktail ring',
        'gema bracelet': 'gema necklace',
        'gema necklace': 'gema bracelet',
        'hyperbola drop earrings': 'meteora drop earrings',
        'lucent bangle': 'lucent cocktail ring',
        'lucent cocktail ring': 'lucent bangle',
        'lucent hoop earrings': 'lucent cocktail ring',
        'luna cocktail ring': 'luna drop earrings',
        'luna drop earrings': 'luna cocktail ring',
        'matrix tennis necklace': 'millenia necklace',
        'meteora drop earrings': 'hyperbola drop earrings',
        'millenia necklace': 'matrix tennis necklace',
        'stilla necklace': 'angelic necklace',
    }

    return abbinamenti.get(product_name, None)


if __name__ == '__main__':
    product_info = [
        {'id': 1,  'name': 'angelic bracelet', 'category': 'bracelet', 'storage': 8}, 
        {'id': 2,  'name': 'angelic necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 3,  'name': 'constella cocktail ring', 'category': 'ring', 'storage': 5}, 
        {'id': 4,  'name': 'dad bracelet', 'category': 'bracelet', 'storage': 5},
        {'id': 5,  'name': 'dancing swan necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 6,  'name': 'dextera bracelet', 'category': 'bracelet', 'storage': 5},  
        {'id': 7,  'name': 'dextera hoop earrings', 'category': 'earrings', 'storage': 5}, 
        {'id': 8,  'name': 'dextera necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 9,  'name': 'florere necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 10, 'name': 'florere stud earrings', 'category': 'earrings', 'storage': 5}, 
        {'id': 11, 'name': 'gema bracelet', 'category': 'bracelet', 'storage': 5}, 
        {'id': 12, 'name': 'gema drop earrings', 'category': 'earrings', 'storage': 5}, 
        {'id': 13, 'name': 'gema necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 14, 'name': 'matrix tennis necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 15, 'name': 'matrix drop earrings', 'category': 'earrings', 'storage': 5}, 
        {'id': 16, 'name': 'matrix ring', 'category': 'ring', 'storage': 5}, 
        {'id': 17, 'name': 'matrix stud earrings', 'category': 'earrings', 'storage': 5}, 
        {'id': 18, 'name': 'mesmera bracelet', 'category': 'bracelet', 'storage': 5}, 
        {'id': 19, 'name': 'mesmera cocktail ring', 'category': 'ring', 'storage': 5}, 
        {'id': 20, 'name': 'mesmera necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 21, 'name': 'millenia cocktail ring', 'category': 'ring', 'storage': 5}, 
        {'id': 22, 'name': 'crystalline delight watch', 'category': 'watch', 'storage': 5}, #
        {'id': 23, 'name': 'stella drop earrings', 'category': 'earrings', 'storage': 5}, 
        {'id': 24, 'name': 'stella necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 25, 'name': 'stella stud earrings', 'category': 'earrings', 'storage': 5}, 
        {'id': 26, 'name': 'stone hoop earrings', 'category': 'earrings', 'storage': 5},
        {'id': 27, 'name': 'swarovski iconic swan earring jackets', 'category': 'earrings', 'storage': 5}, 
        {'id': 28, 'name': 'swarovski iconic swan pendant', 'category': 'necklace', 'storage': 5}, 
        {'id': 29, 'name': 'swarovski swan stud earrings', 'category': 'earrings', 'storage': 5}, 
        {'id': 30, 'name': 'vittore ring', 'category': 'ring', 'storage': 5},
        {'id': 31, 'name': 'disney mickey mouse pendant', 'category': 'necklace', 'storage': 5},
        {'id': 32, 'name': 'lucent bangle', 'category': 'bracelet', 'storage': 5},
        {'id': 33, 'name': 'lucent hoop earrings', 'category': 'earrings', 'storage': 5},
        {'id': 34, 'name': 'meteora drop earrings', 'category': 'earrings', 'storage': 5},
        {'id': 35, 'name': 'stilla necklace', 'category': 'necklace', 'storage': 5},
        {'id': 36, 'name': 'creativity pendant', 'category': 'necklace', 'storage': 5},
        {'id': 37, 'name': 'millenia necklace', 'category': 'necklace', 'storage': 5},
        {'id': 38, 'name': 'luna drop earrings', 'category': 'earrings', 'storage': 5},
        {'id': 39, 'name': 'hyperbola drop earrings', 'category': 'earrings', 'storage': 5},
        {'id': 40, 'name': 'lucent cocktail ring', 'category': 'ring', 'storage': 5},
        {'id': 41, 'name': 'luna cocktail ring', 'category': 'ring', 'storage': 5},
        {'id': 42, 'name': 'florere cocktail ring', 'category': 'ring', 'storage': 5},
        
        
    ]

    #dialogo
    
    print("Buon pomeriggio")
    carrello = []
    user_input = True
    while user_input == True:
        print("Hai bisogno di qualcosa")
        risposta1 = str(input())

        gender  = str(analizza_genere(risposta1))
        age     = int(estrai_eta(risposta1))
        budget  = int(estrai_budget(risposta1))
        category= str(estrai_categoria(risposta1))

        profilo_utente = [gender, age, budget, category]
                    
        posizioni_vuote = [pos for pos, val in enumerate(profilo_utente) if val == "" or val == 0]

        while len(posizioni_vuote)!=0:
            for i in range(len(posizioni_vuote)):
                if posizioni_vuote[i] == 0:
                    print("posso chiederti per chi è il gioiello?")
                    risposta2 = str(input())
                    gender = str(analizza_genere(risposta2))
                                
                elif posizioni_vuote[i] == 1:
                    print("E quanti ha?")
                    risposta3 = str(input())
                    age = int(estrai_eta(risposta3))
                                
                elif posizioni_vuote[i] == 2:
                    print("Quanto vorresti spendere?")
                    risposta4 = str(input())
                    budget = int(estrai_budget(risposta4))
                                
                elif posizioni_vuote[i] == 3:
                    print("E che genere di gioielli preferisce? Collane, bracciali, orecchini o anelli?")
                    risposta5 = str(input())
                    category = str(estrai_categoria(risposta5))
                        
            profilo_utente = [gender, age, budget, category]
            posizioni_vuote = [pos for pos, val in enumerate(profilo_utente) if val == "" or val == 0]

        id_gioiello_consigliato = recommend_jewelry(profilo_utente, product_info)

        print(id_gioiello_consigliato)

        if type(id_gioiello_consigliato) == list:
            i = 0
            while i < len(id_gioiello_consigliato):
                product_name = get_product_name_by_id(product_info, id_gioiello_consigliato[i])

                print("Ti consiglio di prendere:", product_name)
                funzione_prodotto = product_name.capitalize().replace(' ', '_')
                descrizione = Descrizione_prodotto(funzione_prodotto)
                print(descrizione)

                print("Che ne pensi?")
                risposta_a1 = str(input())
                risposta_a1_= estrai_si_no(risposta_a1.lower())
                            
                if risposta_a1_ == "si":
                    carrello.append(product_name)
                                    
                    print("Posso consigliarti qualche abbinamento")                         
                    risposta_= input()
                    risposta__= estrai_si_no(risposta_.lower())
                                    
                    if risposta__ == "si":
                        print(type(product_name))
                        abbinamento = funzione_abbinamento(product_name)
                        
                        print("Ti consiglio di prendere:", abbinamento,"con", product_name)
                        funzione_prodotto2 = abbinamento.capitalize().replace(' ', '_')
                        descrizione2 = Descrizione_prodotto(funzione_prodotto2)
                        print(descrizione2)
                                    
                        print("Ti piace?")
                        risposta3 = input()
                        risposta3_ = estrai_si_no(risposta3.lower())
                                        
                        if risposta3 == "si":
                            carrello.append(abbinamento)
                            user_input = False
                            break
                        else:
                            print("non so che prodotto consigliarti")
                            user_input = False
                            break
                                            
                    else:
                        break

                i += 1
                if i == len(id_gioiello_consigliato):
                    print("Non ho trovato un prodotto che rispecchia le tue richieste")
                    user_input=False
                    break
                    
        else:
            print("Non ho trovato un prodotto che rispecchia le tue richieste")
            user_input=False
            break

        print("Vuoi acquistare acquistare unaltro prodotto?")
        user_input=str(input())
        user_input_1=estrai_si_no(user_input)

        if user_input_1=="no":
            user_input=False
            break
        else:
            user_input = True
            risposta1 = ""
            
    print(carrello)        
    print("Grazie per aver acquistato da swarovski")







