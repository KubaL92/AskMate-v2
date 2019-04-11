from database.db_connection import db_connection


@db_connection.connection_handler
#def add_to_db(cursor, username, password):  # zapis do bazy danych z arkusza rejestracji
 #   cursor.execute("""INSERT INTO user_data(registration_time, username, password)
  #                  VALUES (date_trunc('minute', now()), %(username)s, %(password)s)
   #                   RETURNING user_id""", {'username': username, 'password': password})
def add_to_db(cursor, user_id, username, hashed_password):  # zapis do bazy danych z arkusza rejestracji
    print(user_id, username, hashed_password)
    sql_str = """INSERT INTO user_data(user_id, registration_time,  username, password)
    VALUES (%(user_id)s, CURRENT_TIMESTAMP, %(username)s, %(password)s)
    RETURNING user_id"""
    print('dupsko')

    cursor.execute(sql_str, {'user_id': user_id,
                            'username': username,
                            'password': hashed_password
                            })
    print('dupa')
    usr_id = cursor.fetchone()
    print(usr_id)
    return usr_id['user_id']


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
