from flask import request
import time
import connection


def get_titles(user_stories: list) -> list:
    list_of_titles = []
    for i in user_stories:
        list_of_titles.append(i['title'])
    return list_of_titles


def generate_question_id(file_path='sample_data/question.csv'):
    question_list = connection.csv_to_list(file_path)
    id_ = 0
    for question in question_list:
        id_ = int(question['id'])
    id_gen = id_ + 1
    return str(id_gen)


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


def get_answer_to_dict():
    if request.method == 'POST':
        id_= generate_question_id('sample_data/answer.csv')
        submission_time = int(time.time())
        vote_number = 0
        message = request.form['new_answer']
        image = ""
        question_id = request.args['id']
        answer_dict = {"id": id_,
                       "message" : message,
                       "submission_time" : submission_time,
                       "vote_number" : vote_number,
                       "question_id" : question_id,
                       "image" : image,
                       }
        return answer_dict
