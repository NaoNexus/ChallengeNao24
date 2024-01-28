import psycopg2

from logging_helper import logger
from datetime import datetime


class DB:

    def __init__(self):
        import config_helper
        config_helper = config_helper.Config()

        try:
            self.connection = psycopg2.connect(host=config_helper.db_host, 
                                               database=config_helper.db_name,
                                               user=config_helper.db_user, 
                                               password=config_helper.db_password)
        except Exception as e:
            logger.error(str(e))


    def get_cliente(self):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            SELECT * 
                            FROM Cliente
                            ORDER BY id;
                            ''')

                if (cur.rowcount == 0):
                    return {}
                data = []
                for tupla in cur:
                    data.append({
                                'id'      : tupla[0], 
                                'username': tupla[1], 
                                'nome'    : tupla[2], 
                                'cognome' : tupla[3], 
                                'password': tupla[4]
                            })
                return data

    def get_id_cliente(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            SELECT * 
                            FROM Cliente
                            WHERE id::text = %s;
                            ''', (str(id),))

                if (cur.rowcount == 0):
                    return {}

                for tupla in cur:
                    return  {
                                'id'      : tupla[0], 
                                'username': tupla[1], 
                                'nome'    : tupla[2], 
                                'cognome' : tupla[3], 
                                'password': tupla[4]
                            }

    def set_cliente(self, username, nome, cognome, password):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            INSERT INTO Cliente(username,nome,cognome,password)
                            VALUES (%s, %s, %s, %s);
                            ''', (username, nome, cognome, password))
                return cur.statusmessage

    def set_id_cliente(self, id, username, nome, cognome, password):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            UPDATE Cliente
                            SET username = %s,
                                nome = %s,
                                cognome = %s,
                                password = %s
                            WHERE id::text = %s;
                            ''', (username, nome, cognome, password,str(id)))
                return cur.statusmessage

    def get_count_cliente(self):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            SELECT COUNT(*)
                            FROM Cliente;
                            ''')

                if (cur.rowcount == 0):
                    return {}
                for tupla in cur:
                    return {'count': tupla[0]}

    def delete_cliente(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            DELETE
                            FROM Cliente
                            WHERE id::text = %s;
                            ''', (str(id),))
                return id

    def get_oggetto(self):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            SELECT * 
                            FROM Oggetto
                            ORDER BY id;
                            ''')

                if (cur.rowcount == 0):
                    return {}
                data = []
                for tupla in cur:
                    data.append({
                                'id'                : tupla[0], 
                                'titolo'            : tupla[1], 
                                'categoria'         : tupla[2], 
                                'prezzo'            : tupla[3], 
                                'descrizione'       : tupla[4].decode('utf-8'),
                                'foto'              : tupla[5], 
                                'qta_magazzino'     : tupla[6], 
                                'qta_scaffale'      : tupla[7], 
                                'sconto'            : tupla[8], 
                                'eta_consigliata'   : tupla[9], 
                                'sesso_consigliato' : tupla[10] 
                            })
                return data

    def get_id_oggetto(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            SELECT * 
                            FROM Oggetto
                            WHERE id::text = %s;
                            ''', (str(id),))

                if (cur.rowcount == 0):
                    return {}
                for tupla in cur:
                    return {
                                'id'                : tupla[0], 
                                'titolo'            : tupla[1], 
                                'categoria'         : tupla[2], 
                                'prezzo'            : tupla[3], 
                                'descrizione'       : tupla[4].decode('utf-8'),
                                'foto'              : tupla[5], 
                                'qta_magazzino'     : tupla[6], 
                                'qta_scaffale'      : tupla[7], 
                                'sconto'            : tupla[8], 
                                'eta_consigliata'   : tupla[9], 
                                'sesso_consigliato' : tupla[10] 
                            }

    def set_oggetto(self, titolo, categoria, prezzo, descrizione, foto, qta_magazzino, qta_scaffale, sconto, eta_consigliata, sesso_consigliato):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            INSERT INTO Oggetto(titolo,categoria,prezzo,descrizione,foto,qta_magazzino,qta_scaffale,sconto,eta_consigliata,sesso_consigliato)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                            ''', (titolo,categoria,prezzo,descrizione,foto,qta_magazzino,qta_scaffale,sconto,eta_consigliata,sesso_consigliato))
                return cur.statusmessage

    def set_id_oggetto(self, id, titolo, categoria, prezzo, descrizione, foto, qta_magazzino, qta_scaffale, sconto, eta_consigliata, sesso_consigliato):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            UPDATE Oggetto
                            SET titolo = %s,
                                categoria = %s,
                                prezzo = %s,
                                descrizione = %s,
                                foto = %s,
                                qta_magazzino = %s,
                                qta_scaffale = %s,
                                sconto = %s,
                                eta_consigliata = %s,
                                sesso_consigliato = %s
                            WHERE id::text = %s;
                            ''', (titolo, categoria, prezzo, descrizione, foto, qta_magazzino, qta_scaffale, sconto, eta_consigliata, sesso_consigliato, str(id)))
                return cur.statusmessage

    def delete_oggetto(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            DELETE
                            FROM Oggetto
                            WHERE id::text = %s;
                            ''', (str(id),))
                return id

    def get_ordine_oggetto(self):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            SELECT * 
                            FROM OrdineOggetto AS OrdOgg INNER JOIN Oggetto AS Ogg ON OrdOgg.id_oggetto = Ogg.id
                                                            INNER JOIN Ordine AS Ord ON OrdOgg.id_ordine = Ord.id
                                                                INNER JOIN Cliente AS Cli ON Ord.id_cliente = Cli.id
                            ''')

                if (cur.rowcount == 0):
                    return {}
                '''
                for tupla in cur.description:
                    print tupla[0]
                '''
                data = []
                for tupla in cur:
                    data.append({
                                'id': tupla[0],
                                'oggetto': {
                                    'id'                : tupla[3], 
                                    'titolo'            : tupla[4], 
                                    'categoria'         : tupla[5], 
                                    'prezzo'            : tupla[6], 
                                    'descrizione'       : tupla[7].decode('utf-8'),
                                    'foto'              : tupla[8], 
                                    'qta_magazzino'     : tupla[9], 
                                    'qta_scaffale'      : tupla[10], 
                                    'sconto'            : tupla[11], 
                                    'eta_consigliata'   : tupla[12], 
                                    'sesso_consigliato' : tupla[13] 
                                },
                                'ordine': {
                                    'id'                : tupla[14],
                                    'prezzo_totale'     : tupla[16],
                                    'data_acquisto'     : tupla[17],
                                    'ora_acquisto'      : tupla[18],
                                    'modalita_pagamento': tupla[19]
                                },
                                'cliente': {
                                    'id'                : tupla[20],
                                    'username'          : tupla[21],
                                    'nome'              : tupla[22],
                                    'cognome'           : tupla[23],
                                    'password'          : tupla[24]
                                }
                            })
                return data

    def get_carrello_oggetto(self):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            SELECT * 
                            FROM CarrelloOggetto AS CarOgg INNER JOIN Oggetto AS Ogg ON CarOgg.id_oggetto = Ogg.id
                                                            INNER JOIN Carrello AS Car ON CarOgg.id_carrello = Car.id
                                                                INNER JOIN Cliente AS Cli ON Car.id_cliente = Cli.id
                            ''')

                if (cur.rowcount == 0):
                    return {}
                '''
                for tupla in cur.description:
                    print tupla[0]
                '''
                data = []
                for tupla in cur:
                    data.append({
                                'id': tupla[0],
                                'oggetto': {
                                    'id'                : tupla[3], 
                                    'titolo'            : tupla[4], 
                                    'categoria'         : tupla[5], 
                                    'prezzo'            : tupla[6], 
                                    'descrizione'       : tupla[7].decode('utf-8'),
                                    'foto'              : tupla[8], 
                                    'qta_magazzino'     : tupla[9], 
                                    'qta_scaffale'      : tupla[10], 
                                    'sconto'            : tupla[11], 
                                    'eta_consigliata'   : tupla[12], 
                                    'sesso_consigliato' : tupla[13] 
                                },
                                'carrello': {
                                    'id'                : tupla[1],
                                },
                                'cliente': {
                                    'id'                : tupla[16],
                                    'username'          : tupla[17],
                                    'nome'              : tupla[18],
                                    'cognome'           : tupla[19],
                                    'password'          : tupla[20]
                                }
                            })
                return data

    def get_carrello(self):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            SELECT * 
                            FROM Carrello
                            ORDER BY id;
                            ''')

                if (cur.rowcount == 0):
                    return {}
                data = []
                for tupla in cur:
                    data.append({
                                'id'        : tupla[0], 
                                'id_cliente': tupla[1]
                            })
                return data

    def set_qta_scaffale_plus(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            UPDATE Oggetto
                            SET qta_scaffale = qta_scaffale + 1
                            WHERE id::text = %s;
                            ''', (str(id),))

                return cur.statusmessage

    def set_qta_scaffale_minus(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            UPDATE Oggetto
                            SET qta_scaffale = qta_scaffale - 1
                            WHERE id::text = %s;
                            ''', (str(id),))

                return cur.statusmessage


    def set_qta_magazzino_plus(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            UPDATE Oggetto
                            SET qta_magazzino = qta_magazzino + 1
                            WHERE id::text = %s;
                            ''', (str(id),))

                return cur.statusmessage

    def set_qta_magazzino_minus(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            UPDATE Oggetto
                            SET qta_magazzino = qta_magazzino - 1
                            WHERE id::text = %s;
                            ''', (str(id),))

                return cur.statusmessage

    def get_abbinamento(self):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            SELECT * 
                            FROM Abbinamento
                            ORDER BY id;
                            ''')

                if (cur.rowcount == 0):
                    return {}
                data = []
                for tupla in cur:
                    data.append({
                                'id'         : tupla[0], 
                                'id_oggetto1': tupla[1],
                                'id_oggetto2': tupla[2]
                            })
                return data

    def set_abbinamento(self, id1, id2):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            INSERT INTO Abbinamento(id_oggetto1,id_oggetto2)
                            VALUES (%s, %s);
                            ''', (id1, id2))
                return cur.statusmessage

    def delete_abbinamento(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                            DELETE
                            FROM Abbinamento
                            WHERE id::text = %s;
                            ''', (str(id),))
                return id



    """
    def save_report(self, report):
        with self.connection:
            with self.connection.cursor() as cur:
                if (report.get('date', '') == ''):
                    report['date'] = datetime.now().isoformat()

                if (report.get('id', '') == ''):
                    cur.execute('''
                        INSERT INTO Reports(date, temperature, co2, humidity, "nPeople", "internalLight", "externalLight")
                        VALUES (%s, %s, %s, %s, %s, %s, %s);''',
                                (report['date'], report['temperature'], report['co2'], report['humidity'], report.get('nPeople', 0), report.get('internalLight', 0), report.get('externalLight', 0),))
                else:
                    cur.execute('''
                        UPDATE Reports
                        SET date = %s, temperature = %s, co2 = %s, humidity = %s, "nPeople" = %s, "internalLight" = %s, "externalLight" = %s
                        WHERE id = %s;''',
                                (report['date'].split('.')[0], report['temperature'], report['co2'], report['humidity'], report['nPeople'], report['internalLight'], report['externalLight'], report['id']))

                return cur.statusmessage

    def get_report(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                    SELECT * FROM Reports
                    WHERE id::text = %s
                    ORDER BY date;''',
                            (str(id),))

                if (cur.rowcount == 0):
                    return {}
                for tupla in cur:
                    return {'id': tupla[0], 'date': tupla[1], 'temperature': tupla[2], 'co2': tupla[3], 'humidity': tupla[4], 'nPeople': tupla[5], 'internalLight': tupla[6], 'externalLight': tupla[7]}

    def get_reports(self):
        with self.connection:
            with self.connection.cursor() as cur:
                data = []
                cur.execute('''
                    SELECT * FROM Reports
                    ORDER BY date DESC;''')

                for tupla in cur:
                    data.append(
                        {'id': tupla[0], 'date': tupla[1], 'temperature': tupla[2], 'co2': tupla[3], 'humidity': tupla[4], 'nPeople': tupla[5], 'internalLight': tupla[6], 'externalLight': tupla[7]})

                return data

    def delete_report(self, id):
        with self.connection:
            with self.connection.cursor() as cur:
                cur.execute('''
                    DELETE FROM Reports
                    WHERE id::text = %s;''',
                            (str(id),))

                return id
    """
