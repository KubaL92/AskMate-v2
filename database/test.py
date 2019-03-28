from database.db_connection import db_connection

@db_connection.connection_handler
def get_everything(cursor):
    cursor.execute("SELECT * FROM answer WHERE id='1'")
    everything = cursor.fetchall()
    return everything

print(get_everything())