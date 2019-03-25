import csv
import data_manager



def csv_to_list(file_path):
    user_stories = []
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_story = dict(row)
            a = '\n'
            for key, value in user_story.items():
                if a in value:
                    value = value.replace(a, "")
            user_stories.append(user_story)
    return user_stories




def display_question(file_path, id):
    return csv_to_list(file_path)[id]


def add_data_to_file():
    dictio = data_manager.get_data_to_dict()
    data_header = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
    file_path = 'sample_data/question.csv'
    existing_data = csv_to_list('sample_data/question.csv')
    existing_data.append(dictio)
    with open(file_path, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data_header)
        writer.writeheader()
        writer.writerows(existing_data)

def add_answer_to_file(new_answer):
    dictio = new_answer
    data_header = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
    file_path = 'sample_data/answer.csv'
    existing_data = csv_to_list('sample_data/answer.csv')
    existing_data.append(dictio)
    with open(file_path, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data_header)
        writer.writeheader()
        writer.writerows(existing_data)

