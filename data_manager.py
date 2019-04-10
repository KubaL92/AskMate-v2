from flask import request
import bcrypt
from database import db_question, db_answer, db_user

"""
def change_to_string(something):
    return str(something)

def change_to_integer_and_add_1(something_else):
    return int(something_else)+1


def update_view_number_in_specific_question(file_path, id):
    all_with_number_unchanged = connection.csv_to_list(file_path)
    updated = []
    for line in all_with_number_unchanged:
        if line['id']==str(id):
            line['view_number'] = change_to_integer_and_add_1(line['view_number'])
            line['view_number'] = change_to_string(line['view_number'])
            updated.append(line)
        else:
            updated.append(line)
    return updated

# absolutnie niepotrzebne
def get_titles(user_stories: list) -> list:
    list_of_titles = []
    for i in user_stories:
        list_of_titles.append(i['title'])
    return list_of_titles

# absolutnie niepotrzebne
def generate_question_id(file_path='sample_data/question.csv'):
    question_list = connection.csv_to_list(file_path)
    id_ = 0
    for question in question_list:
        id_ = int(question['id'])
    id_gen = id_ + 1
    return str(id_gen)

# absolutnie niepotrzebne
def give_specific_answers(id, list_of_all_answers):
    list_of_all_answers = connection.csv_to_list('sample_data/answer.csv')
    list_of_answers = []
    for answer in list_of_all_answers:
        if answer['question_id'] == str(id):
            list_of_answers.append(answer)
    return list_of_answers
    
    
def get_data_to_dict():
    if request.method == 'POST':
        title = request.form['title']
        question = request.form['question']
        id_ = generate_question_id('sample_data/question.csv')
        view_number = 0
        vote_number = 0
        image = ""
        submission_time = int(time.time())
        my_dict = {"id": id_,
                   "submission_time" : submission_time,
                   "vote_number" : vote_number,
                   "view_number" : view_number,
                   "title": title,
                   "message": question,
                   "image" : image}

        return my_dict


def get_answer_to_dict(lol):
    if request.method == 'POST':
        id_= generate_question_id('sample_data/answer.csv')
        submission_time = int(time.time())
        vote_number = 0
        message = request.form['new_answer']
        image = ""
        question_id = lol
        answer_dict = {"id": id_,
                       "message" : message,
                       "submission_time" : submission_time,
                       "vote_number" : vote_number,
                       "question_id" : question_id,
                       "image" : image,
                       }
        return answer_dict
"""


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
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password


def processing_registration_data(username, hashed_password):
    return db_user.add_to_db(username, hashed_password)
