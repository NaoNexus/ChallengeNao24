def recommend_jewelry(customer_info, product_info):
    
    gender = customer_info['gender']
    age = customer_info['age']
    budget = customer_info['budget']
    category = customer_info['category']

    '''
    name = primo_dizionario[list(primo_dizionario.keys())[1]]
    category = primo_dizionario[list(primo_dizionario.keys())[2]]
    storage = primo_dizionario[list(primo_dizionario.keys())[3]]
    '''
    
    # -- male
    if gender == 'male':

        if age > 60:
            return 'Nessun articolo trovato'
        
        elif  age < 20: 

            if category == 'bracelet':
                
                if budget >= 155:
                    gioielli_consigliati = [6]
                    return sgioielli_consigliati
                
                else:
                    return 'Nessun articolo trovato'
            
            elif category == 'necklace':

                #tengo cmq due return distinti e non una lista pk i prezzi sono motlo diversi
                
                if budget < 175:
                    return 'Nessun articolo trovato'
                
                elif budget >= 175 and budget < 700:
                    gioielli_consigliati = [8]
                    return  gioielli_consigliati
                
                else:
                    #indice? magazzino?
                    gioielli_consigliati = [8, 22]
                    return  gioielli_consigliati
    
            else:
                return 'Nessun articolo trovato'

        elif 20 <= age <= 60:
            
            if category == 'bracelet':
                
                if budget < 145:
                    return 'Nessun articolo trovato'
                
                else: #(budget >= 145:)
                    gioielli_consigliati = [4, 6]
                    return gioielli_consigliati

            elif category == 'necklace':
                
                if budget < 175:
                    return 'Nessun articolo trovato'
                
                elif budget < 700:
                    gioielli_consigliati = [8]
                    return  gioielli_consigliati
                
                else: #(budget >= 700):
                    #indice? magazzino?
                    gioielli_consigliati = [8, 22]
                    return gioielli_consigliati

            else:
                return 'Nessun articolo trovato'

    # -- female
    elif gender == 'female':
    
        if 0 < age < 20:
            
            if category == 'bracelet':
        
                if budget >= 155:
                    gioielli_consigliati = [1]
                    return gioielli_consigliati
                
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

    #ho aggiunto la categoria (che forse va aggiunta nel dataset in cliente??) pk è lui che deve specificare cosa vuole insieme al budget
    customer_info = {'gender': 'male', 'age': 16, 'budget': 300, 'category': 'necklace'}
    product_info = [
        {'id': 1, 'name': 'angelic bracelet', 'category': 'bracelet', 'storage': 8}, 
        {'id': 2, 'name': 'angelic necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 3, 'name': 'constella cocktail ring', 'category': 'ring', 'storage': 5}, 
        {'id': 4, 'name': 'dad bracelet', 'category': 'bracelet', 'storage': 5},
        {'id': 5, 'name': 'dancing swan necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 6, 'name': 'dextera bracelet', 'category': 'bracelet', 'storage': 5},  
        {'id': 7, 'name': 'dextera hoop earrings', 'category': 'earrings', 'storage': 5}, 
        {'id': 8, 'name': 'dextera necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 9, 'name': 'florere necklace', 'category': 'necklace', 'storage': 5}, 
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
        {'id': 22, 'name': 'millenia necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 23, 'name': 'stella drop earrings', 'category': 'earrings', 'storage': 5}, 
        {'id': 24, 'name': 'stella necklace', 'category': 'necklace', 'storage': 5}, 
        {'id': 25, 'name': 'stella stud earrings', 'category': 'earrings', 'storage': 5}, 
        {'id': 26, 'name': 'stone hoop earrings', 'category': 'earrings', 'storage': 5},
        {'id': 27, 'name': 'swarovski iconic swan earring jackets', 'category': 'earrings', 'storage': 5}, 
        {'id': 28, 'name': 'swarovski iconic swan pendant', 'category': 'necklace', 'storage': 5}, 
        {'id': 29, 'name': 'swarovski swan stud earrings', 'category': 'earrings', 'storage': 5}, 
        {'id': 30, 'name': 'vittore ring', 'category': 'ring', 'storage': 5}
    ]

    '''
    # Accesso al primo dizionario
    primo_dizionario = product_info[0]
    secondo_dizionario = product_info[1]

    # Accesso al primo e al secondo valore del primo dizionario
    primo_valore = primo_dizionario[next(iter(primo_dizionario))]
    secondo_valore = primo_dizionario[list(primo_dizionario.keys())[1]]
    '''
    
    gioiello_consigliato = recommend_jewelry(customer_info, product_info)
    print("Ti consigliamo: ", gioiello_consigliato)
    
    
