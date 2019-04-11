from database.db_connection import db_connection

@db_connection.connection_handler
def add_user(cursor, username, password):
    cursor.execute("INSERT INTO user_data (registration_time, username, password) VALUES (CURRENT_TIMESTAMP, %(username)s, %(password)s)", ({
        'username':username,
        'password':password
    }))

@db_connection.connection_handler
def get_username_and_password(cursor):
    cursor.execute("SELECT username, password FROM user_data")
    dejta = cursor.fetchall()
    return dejta

