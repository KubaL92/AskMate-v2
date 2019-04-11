from database.db_connection import db_connection


@db_connection.connection_handler
def add_to_db(cursor, username, password):  # zapis do bazy danych z arkusza rejestracji
    cursor.execute("""INSERT INTO user_data(registration_time, username, password)
                    VALUES (date_trunc('minute', now()), %(username)s, %(password)s)
                      RETURNING user_id""", {'username': username, 'password': password})
    usr_id = cursor.fetchone()
    return int(usr_id['user_id'])
