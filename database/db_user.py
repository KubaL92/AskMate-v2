from database.db_connection import db_connection


@db_connection.connection_handler
def add_to_db(username, user_id, password, cursor):  # zapis do bazy danych z arkusza rejestracji
    sql_str = """INSERT INTO user_data(registration_time, user_id, username, password)
    VALUES (current_timestamp, %(user_id)s, %(username)s, %(password)s)
    RETURNING user_id"""
    cursor.execute(sql_str({'username': username,
                            'password': password,
                            'user_id': user_id}))
    usr_id = cursor.fetchone()
    return int(usr_id['id'])


@db_connection.connection_handler
def get_all_users_id(cursor):
    cursor.execute("SELECT user_id FROM user_data");
    ids = cursor.fetchall()
    return ids


@db_connection.connection_handler
def get_all_users_name(cursor):
    cursor.execute("SELECT username FROM user_data");
    names = cursor.fetchall()
    return names


@db_connection.connection_handler
def check_if_user_exists(cursor, login):
    cursor.execute("SELECT EXISTS(SELECT 1 "
                   "FROM user_data "
                   "WHERE username=%(login)s)",{
        'login':login
    });
    existance = cursor.fetchone()
    return existance

@db_connection.connection_handler
def get_password(cursor, login):
    cursor.execute("SELECT password FROM user_data WHERE username=%(login)s",{
        'login':login
    })
    usr_password = cursor.fetchone()
    return usr_password
