from database.db_connection import db_connection


@db_connection.connection_handler
def add_to_db(username, password, cursor): #zapis do bazy danych z arkusza rejestracji
    sql_str = """INSERT INTO user_data(registration_time, username, password),
    VALUES (current_timestamp, %(username)s, %(password)s),
    RETURNING user_id"""
    cursor.execute(sql_str({'username':username
                            'password':password}))
    usr_id = cursor.fetchone()
    return int(usr_id['id'])
