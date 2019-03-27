# moduł łączenia z bazą danych, obsługujący tablicę question
from database.db_connection import db_connection


@db_connection.connection_handler
def get_all_questions(cursor): #testowa funkcja, zgarnia całą tablicę question
    cursor.execute("SELECT * FROM question")
    all_questions = cursor.fetchall()
    return all_questions


@db_connection.connection_handler
def get_question_by_id(cursor, question_id):
    cursor.execute("SELECT * FROM question WHERE id=%(question_id)s", {'question_id':question_id})
    question_with_specific_id = cursor.fetchone()
    return question_with_specific_id




