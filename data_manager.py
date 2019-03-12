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


def give_specific_answers(i_d, list_of_all_answers):
    list_of_answers=[]
    for answer in list_of_all_answers:
        if int(answer['question_id']) == i_d:
            list_of_answers.append(answer)
    return list_of_answers
