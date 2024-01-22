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
                            FROM Cliente;
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
