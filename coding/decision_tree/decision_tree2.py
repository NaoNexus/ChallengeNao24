def recommend_jewelry(customer_info, product_info):
    
    gender = customer_info['gender']
    age = customer_info['age']
    budget = customer_info['budget']
    
    name = primo_dizionario[list(primo_dizionario.keys())[1]]
    category = primo_dizionario[list(primo_dizionario.keys())[2]]
    storage = primo_dizionario[list(primo_dizionario.keys())[3]]

    # -- male
    if gender == 'male':

        if age > 60:
            return 'Nessun articolo trovato'
        
        elif  age < 20: 

            if category == 'bracelet':
                
                if budget >= 155:
                    return 6
                
                else:
                    return 'Nessun articolo trovato'
            
            elif category == 'necklace':
                
                if budget < 175:
                    return 'Nessun articolo trovato'
                
                elif budget >= 175 and budget < 700:
                    return  8
                
                else:
                    # -- METTI MAGAZZINO per decidere tra 8 e 22
                    return  22 and  8
    
            else:
                return 'Nessun articolo trovato'

        elif 20 <= age <= 60:
            
            if category == 'bracelet':
                
                if budget < 145:
                    return 'Nessun articolo trovato'
                
                elif budget < 155:
                    return  4
                
                else:
                    # -- MAGAZZINO
                    return  6 and  4

            elif category == 'necklace':
                
                if budget < 175:
                    return 'Nessun articolo trovato'
                
                elif budget < 700:
                    return  8
                
                else: # --if budget >= 700:
                    # -- MAGAZZINO
                    return  8 and  22

            else:
                return 'Nessun articolo trovato'

    # -- female
    elif gender == 'female':
    
        if 0 < age < 20:
            
            if category == 'bracelet':
        
                if budget >= 155:
                    return  1
                
                else:
                    return 'Nessun articolo trovato'
                    
            elif category == 'necklace':
            
                if budget < 155:
                    return 'Nessun articolo trovato'
                    
                elif 155 <= budget < 175:
                    return  5
                    
                elif 175 <= budget < 230:
                    # -- MAGAZZINO
                    return  5 and  24
                    
                elif budget >= 230:
                    return  2 and  5 and  24
                    
            elif category == 'earrings':
            
                if budget < 115:
                    return 'Nessun articolo trovato'
                    
                elif 115 <= budget < 125:
                    return  7

                elif 125 <= budget < 135:
                    return  7 and  25 and  26

                else:
                    return  23 and  7 and  25 and  26
                    
            else:
                return 'Nessun articolo trovato'
                    
        elif 20 <= age < 40:
        
            if category == 'bracelet':
                    
                if budget >= 195:
                    return  11

                else:
                    return 'Nessun articolo trovato'
                    
            elif category == 'necklace':
            
                if budget < 115:
                    return 'Nessun articolo trovato'
                    
                elif 115 <= budget < 195:
                    return  28

                else:
                    return  28 and  13
                    
            elif category == 'earrings':
                
                if budget < 125:
                    return 'Nessun articolo trovato'
                    
                elif 125 <= budget < 129:
                    return  27

                elif 129 <= budget < 195:
                    return  27 and  29
                    
                else:
                    return  27 and  29 and  12
                
            else:
                return 'Nessun articolo trovato'
                    
        elif 40 <= age < 60:
        
            if category == 'necklace':
            
                if budget < 175:
                    return 'Nessun articolo trovato'
                
                elif 175 <= budget < 350:
                    return  9
                    
                else:
                    return  9 and  14
                    
            elif category == 'earrings':
                    
                if budget < 95:
                    return 'Nessun articolo trovato'
                    
                elif 95 <= budget < 195:
                    return  17
                    
                else:
                    return  17 and  10 and  15
                    
            elif category == 'ring':
            
                if budget < 75:
                    return 'Nessun articolo trovato'
                    
                elif 75 <= budget < 125:
                    return  30
                    
                elif 125 <= budget < 135:
                    return  16 and  30
                    
                else:
                 return  16 and  30 and  3
                 
            else:
                return 'Nessun articolo trovato'
                
        elif age >= 60:
        
            if category == 'bracelet':
                
                if budget < 400:
                    return 'Nessun articolo trovato'
                
                else:
                    return  18
                    
            elif category == 'necklace':
            
                if budget < 950:
                    return 'Nessun articolo trovato'
                    
                else:
                    return  20
                    
            elif category == 'ring':
                
                if budget < 135:
                    return 'Nessuno articolo trovato'
                    
                else:
                    return  19 and  21
            
            else:
                return 'Nessuno articolo trovato'
                
                
if __name__ == "__main__":

    customer_info = {'gender': 'male', 'age': 16, 'budget': 300}
    product_info = [
        {'id': 6, 'name': 'dextera necklace', 'category': 'necklace', 'storage': 5},
        {'id': 1, 'name': 'angelic_bracelet', 'category': 'bracelet', 'storage': 8},
        {'id': 2, 'name': 'angelic_necklace', 'category': 'necklace', 'storage': 2}
    ]

    # Accesso al primo dizionario
    primo_dizionario = product_info[0]

    # Accesso al primo valore del primo dizionario
    primo_valore = primo_dizionario[next(iter(primo_dizionario))]
    secondo_valore = primo_dizionario[list(primo_dizionario.keys())[1]]

    gioiello_consigliato = recommend_jewelry(customer_info, product_info)
    print("Ti consigliamo: ", gioiello_consigliato)
    
