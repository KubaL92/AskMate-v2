# moduł łączenia z bazą danych, obsługujący tablicę answer

from database.db_connection import db_connection


@db_connection.connection_handler
def get_all_answers_by_question_id(cursor, question_id): #testowa funkcja, zgarnia całą tablicę question
    cursor.execute("SELECT * FROM answer WHERE question_id=%(question_id)s", {'question_id':question_id+1}) # +1 wyrównuje id pytań (inaczej niż python, baza danych numeruje od 1 nie od 0)
    answers = cursor.fetchall()
    return answers

@db_connection.connection_handler
def insert_answer_to_database(cursor, message, question_id, vote_number, image):
    sql_str = """INSERT INTO answer (submission_time, vote_number, question_id, message, image)
              SELECT CURRENT_TIMESTAMP, %(vote_number)s, question.id, %(message)s, %(image)s
              FROM question 
              WHERE question.id = %(question_id)s;
              """
    cursor.execute(sql_str, ({'vote_number': vote_number,
                              'message': message,
                              'image': image,
                              'question_id': question_id}))
    #
    # question_id = cursor.fetchone()
    # return int(question_id['question_id'])