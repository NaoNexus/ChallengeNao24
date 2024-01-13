# -- decision tree

categoria = input("A che tipo di gioiello sei interessato? braccialetti/anelli/collane/orecchini")
if categoria == "braccialetti":

elif categoria == "anelli":

elif categoria == "collane":

elif categoria == "orecchini":


# -- categoria
braccialetti = []
anelli = []
orecchini = []
collane = []

# m == man
# w == women
# 2_3 == dai 20 ai 30 anni
# 3_4 "" ""
def consiglia_gioielli(genere, età):
    m_1_2 = "Gioiello 1"  # -- aggiunto indice di gradimento
    m_2_3 = "Gioiello 2"
    m_3_4 = "Gioiello 3"
    m_4_5 = "Gioiello 4"
    m_5_6 = "Gioiello 5"
    m_6 = "Gioiello 6"

    w_2_3 = "Gioiello 7"
    w_3_4 = "Gioiello 8"
    w_4_5 = "Gioiello 9"
    w_5_6 = "Gioiello 10"
    w_6 = "Gioiello 11"

    if genere == "maschio":
        if età >= 10 and età < 20:
            return m_1_2
            
        elif età >= 20 and età < 30:
            return m_2_3
            
        elif età >= 30 and età < 40:
            return m_3_4
            
        elif età >= 40 and età < 50:
            return m_4_5
            
        elif età >= 50 and età < 60:
            return m_5_6
            
        elif età >= 60:
            return m_6
            
    elif genere == "femmina":
        if età >= 10 and età < 20:
            return w_1_2
            
        elif età >= 20 and età < 30:
            return w_2_3
            
        elif età >= 30 and età < 40:
            return w_3_4
            
        elif età >= 40 and età < 50:
            return w_4_5
            
        elif età >= 50 and età < 60:
            return w_5_6
            
        elif età >= 60:
            return w_6


if __name__ == "__main__":
    genere_utente = input("Qual è il tuo genere? maschio/femmina ")
    età_utente = int(input("Età? "))

    gioiello_consigliato = consiglia_gioielli(genere_utente, età_utente)
    print("Ti consigliamo", gioiello_consigliato)
