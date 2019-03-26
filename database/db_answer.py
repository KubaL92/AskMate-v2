# moduł łączenia z bazą danych, obsługujący tablicę answer

from database.db_connection import db_connection


@db_connection.connection_handler
def get_all_answers_by_question_id(cursor, question_id): #testowa funkcja, zgarnia całą tablicę question
    cursor.execute("SELECT * FROM answer WHERE question_id=%(question_id)s", {'question_id':question_id+1}) # +1 wyrównuje id pytań (inaczej niż python, baza danych numeruje od 1 nie od 0)
    answers = cursor.fetchall()
    return answers

