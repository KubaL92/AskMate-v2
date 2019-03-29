# moduł łączenia z bazą danych, obsługujący tablicę answer

from database.db_connection import db_connection


@db_connection.connection_handler
def get_all_answers_by_question_id(cursor, question_id):
    cursor.execute("SELECT * FROM answer WHERE question_id=%(question_id)s ORDER BY id", {'question_id':question_id})
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


@db_connection.connection_handler
def delete_answer(cursor, answer_id):
    cursor.execute("DELETE FROM answer WHERE id = %s", (answer_id))


@db_connection.connection_handler
def get_answer_vote_number_and_add(cursor, answer_id):
    cursor.execute("SELECT vote_number FROM answer WHERE id=%(answer_id)s", {'answer_id': answer_id})
    vote_number = cursor.fetchone()['vote_number']
    updated_vote_number = vote_number + 1
    return updated_vote_number

@db_connection.connection_handler
def get_answer_vote_number_and_substract(cursor, answer_id):
    cursor.execute("SELECT vote_number FROM answer WHERE id=%(answer_id)s", {'answer_id': answer_id})
    vote_number = cursor.fetchone()['vote_number']
    updated_vote_number = vote_number - 1
    return updated_vote_number



@db_connection.connection_handler
def update_vote_number(cursor, answer_id, updated_vote_number):
    cursor.execute("UPDATE answer SET vote_number = %(updated_vote_number)s WHERE id=%(answer_id)s",
                   ({'answer_id': answer_id, 'updated_vote_number':updated_vote_number}))


