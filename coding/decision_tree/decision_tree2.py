# da mettere poi nel main
customer_info = {'gender': 'male', 'age': 16, 'budget': 300}
product_info = {'name': 'dextera necklace', 'category': 'necklace', 'storage': 5}

def recommend_jewelry(customer_info, product_info):
    
    gender = customer_info['gender']
    age = customer_info['age']
    budget = customer_info['budget']
    jewelry_name = product_info['name']
    jewelry_category = product_info['category']
    jewelry_storage = product_info['storage']

    # -- male
    if gender == 'male':

        if age > 60:
            return: 'Nessun articolo trovato'
        
        elif  age < 20: 

            if category == 'bracelet':
                
                if budget >= 155:
                    return prodotto 6
                
                else:
                    return 'Nessun articolo trovato'
            
            elif category == 'necklace':
                
                if budget < 175:
                    return 'Nessun articolo trovato'
                
                elif budget >=175 and budget < 700:
                    return prodotto 8
                
                else:
                    # -- METTI MAGAZZINO per decidere tra 8 e 22
                    return prodotto 22 and prodotto 8
    
            else:
                return 'Nessun articolo trovato'

        elif 20 <= age <= 60:
            
            if category == 'bracelet':
                
                if budget < 145:
                    return 'Nessun articolo trovato'
                
                elif budget < 155:
                    return prodotto 4
                
                else:
                    # -- MAGAZZINO
                    return prodotto 6 and prodotto 4

            elif category == 'necklace':
                
                if budget < 175:
                    return 'Nessun articolo trovato'
                
                elif budget < 700:
                    return prodotto 8
                
                else: # --if budget >= 700:
                    # -- MAGAZZINO
                    return prodotto 8 and prodotto 22

            else:
                return 'Nessun articolo trovato'

    # -- female
    elif gender == 'female':
    
        if 0 < age < 20:
            
            if category == 'bracelet':
        
                if budget >= 155:
                    return prodotto 1
                
                else:
                    return 'Nessun articolo trovato'
                    
            elif category == 'necklace':
            
                if budget < 155:
                    return 'Nessun articolo trovato'
                    
                elif 155 <= budget < 175:
                    return prodotto 5
                    
                elif 175 <= budget < 230:
                    # -- MAGAZZINO
                    return prodotto 5 and prodotto 24
                    
                elif budget >= 230:
                    return prodotto 2 and prodotto 5 and prodotto 24
                    
            elif category == 'earrings':
            
                if budget < 115:
                    return 'Nessun articolo trovato'
                    
                elif 115 <= budget < 125:
                    return prodotto 7

                elif 125 <= budget < 135:
                    return prodotto 7 and prodotto 25 and prodotto 26

                else:
                    return prodotto 23 and prodotto 7 and prodotto 25 and prodotto 26
                    
            else:
                return 'Nessun articolo trovato'
                    
        elif 20 <= age < 40:
        
            if category == 'bracelet':
                    
                if budget >= 195:
                    return prodotto 11

                else:
                    return 'Nessun articolo trovato'
                    
            elif category == 'necklace':
            
                if budget < 115:
                    return 'Nessun articolo trovato'
                    
                elif 115 <= budget < 195:
                    return prodotto 28

                else:
                    return prodotto 28 and prodotto 13
                    
            elif category == 'earrings':
                
                if budget < 125:
                    return 'Nessun articolo trovato'
                    
                elif 125 <= budget < 129:
                    return prodotto 27

                elif 129 <= budget < 195:
                    return prodotto 27 and prodotto 29
                    
                else:
                    return prodotto 27 and prodotto 29 and prodotto 12
                
            else:
                return 'Nessun articolo trovato'
                    
        elif 40 <= age < 60:
        
            if category == 'necklace':
            
                if budget < 175:
                    return 'Nessun articolo trovato'
                
                elif 175 <= budget < 350:
                    return prodotto 9
                    
                else:
                    return prodotto 9 and prodotto 14
                    
            elif category == 'earrings'
                    
                if budget < 95:
                    return 'Nessun articolo trovato'
                    
                elif 95 <= budget < 195:
                    return prodotto 17
                    
                else:
                    return prodotto 17 and prodotto 10 and prodotto 15
                    
            elif category == 'ring':
            
                if budget < 75:
                    return 'Nessun articolo trovato'
                    
                elif 75 <= budget < 125:
                    return prodotto 30
                    
                elif 125 <= budget < 135:
                    return prodotto 16 and prodotto 30
                    
                else:
                 return prodotto 16 and prodotto 30 and prodotto 3
                 
            else:
                return 'Nessun articolo trovato'
                
        elif age >= 60:
        
            if category == 'bracelet':
                
                if budget < 400:
                    return 'Nessun articolo trovato'
                
                else:
                    return prodotto 18
                    
            elif category == 'necklace':
            
                if budget < 950:
                    return 'Nessun articolo trovato'
                    
                else:
                    return prodotto 20
                    
            elif category == 'ring':
                
                if budget < 135:
                    return 'Nessuno articolo trovato'
                    
                else:
                    return prodotto 19 and prodotto 21
            
            else:
                return 'Nessuno articolo trovato'    
            
