from flask import request
import bcrypt
from database import db_question, db_answer, db_user
import random
import string

def get_questions():
    return db_question.get_all_questions()


def get_questions_with_specific_id(question_id):
    return db_question.get_question_by_id(question_id)


def get_answers(question_id):
    return db_answer.get_all_answers_by_question_id(question_id)


def insert_question_into_table(title, message, image):
    # wpisane na sztywno: łapki oraz wyświetlenia
    VOTE_NUMBER = 0
    VIEW_NUMBER = 0
    return db_question.add_question(title, message, image, VIEW_NUMBER, VOTE_NUMBER)


def insert_answer_to_db(question_id, answer, image):
    VOTE_NUMBER = 0
    return db_answer.insert_answer_to_database(answer, question_id, VOTE_NUMBER, image)


def delete_answer_from_db(answer_id):
    return db_answer.delete_answer(answer_id)


def delete_question_from_db(question_id):
    return db_question.delete_question(question_id)


def update_question_view_number(question_id):
    updated_view_number = db_question.get_question_view_number_and_update(question_id)
    return db_question.update_question_view_number(question_id, updated_view_number)


def upvote_answer(id):
    updated_vote_numer = db_answer.get_answer_vote_number_and_add(id)
    return db_answer.update_vote_number(id, updated_vote_numer)


def downvote_answer(id):
    updated_vote_numer = db_answer.get_answer_vote_number_and_substract(id)
    return db_answer.update_vote_number(id, updated_vote_numer)


###### HERE COMES USERS VERIFICATION PART ######

def hashing_parole(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def id_generator(size=7, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def prepare_list_of_existing_ids():
    existing_ids = []
    ids_dict = db_user.get_all_users_id()
    for id in ids_dict:
        existing_ids.append(id['user_id'])
    return existing_ids

def check_id_uniqueness():
    existing_ids = prepare_list_of_existing_ids()
    unique_id = id_generator()
    while unique_id in existing_ids:
        unique_id = id_generator()
    return unique_id


def processing_registration_data(username, hashed_password):
    user_id = db_user.add_to_db(username, hashed_password)
    return user_id
    user_id = check_id_uniqueness()
    return db_user.add_to_db(username, hashed_password, user_id)

def is_existing(login):
    existance = db_user.check_if_user_exists(login)['exists']
    return existance

def are_passwords_equal(usr_password, login):
    db_password = db_user.get_password(login)['password']
    if usr_password == db_password:
        return True
    else:
        return False
