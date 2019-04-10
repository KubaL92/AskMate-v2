import psycopg2
from database.db_connection import db_connection


@db_connection.connection_handler
def add_to_db(username, password):
    sql_str = """INSERT INTO user_data(registration_time, username, password)
    VALUES (current_timestamp, %(username)s, %(password)s)
    RETURNING user_id"""
