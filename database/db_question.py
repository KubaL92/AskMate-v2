# moduł łączenia z bazą danych, obsługujący tablicę question
from database.db_connection import db_connection


@db_connection.connection_handler
def get_all_questions(cursor):  # testowa funkcja, zgarnia całą tablicę question
    cursor.execute("SELECT * FROM question order by id")
    all_questions = cursor.fetchall()
    return all_questions


@db_connection.connection_handler
def get_question_by_id(cursor, question_id):
    cursor.execute("SELECT * FROM question WHERE id=%(question_id)s", {'question_id': question_id})
    question_with_specific_id = cursor.fetchone()
    return question_with_specific_id


@db_connection.connection_handler
def add_question(cursor, title, message, image, view_number, vote_number):
    sql_str = """ INSERT INTO question(submission_time, view_number, vote_number, title, message, image) 
    VALUES (CURRENT_TIMESTAMP , %(view_number)s, %(vote_number)s, %(title)s, %(message)s, %(image)s)
    RETURNING id """
    cursor.execute(sql_str, ({'title': title,
                              'message': message,
                              'image': image,
                              'view_number': view_number,
                              'vote_number': vote_number})) # slownik aby zawsze przekazac stringa

    question_id = cursor.fetchone() # otrzymujemy słownik
    return int(question_id['id'])   # zwracamy wartość ze słownika


@db_connection.connection_handler
def delete_question(cursor, question_id):
    cursor.execute("DELETE FROM answer WHERE question_id = %(question_id)s", ({'question_id': question_id}))
    cursor.execute("DELETE FROM question WHERE id = %(question_id)s", ({'question_id': question_id}))


@db_connection.connection_handler
def get_question_view_number_and_update(cursor, question_id):
    cursor.execute("SELECT view_number FROM question WHERE id=%(question_id)s", {'question_id': question_id})
    view_number = cursor.fetchone()['view_number']
    updated_view_number = view_number + 1
    return updated_view_number


@db_connection.connection_handler
def update_question_view_number(cursor, question_id, updated_view_number):
    cursor.execute(
        "UPDATE question SET view_number = %(updated_view_number)s "
        "WHERE id=%(question_id)s",
        ({'question_id': question_id, 'updated_view_number':updated_view_number}))
