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
    list_of_answers = []
    for answer in list_of_all_answers:
        if answer['question_id'] == str(id):
            list_of_answers.append(answer)
    return list_of_answers

#
# def get_data_to_dict():
#     if request.method == 'POST':
#         title = request.form['title']
#         question = request.form['message']
#         id = generate_new_id('sample_data/question.csv')
#         view_number = 0
#         vote_number = 0
#         image = ""
#         submission_time = int(time.time())
#         my_dict = {"id": id,
#                    'submission_time': submission_time,
#                    "title": title,
#                    "question": question,
#                    'view_number': view_number,
#                    'vote_number': vote_number,
#                    'image': image}
#         return my_dict


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
                   "title": title,
                   "message": question,
                   "view_number" : view_number,
                   "vote_number" : vote_number,
                   "submission_time" : submission_time,
                   "image" : image}

        return my_dict


