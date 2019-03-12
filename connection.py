import csv

def csv_to_list(file_path: str) -> list:
    list_of_data = []
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data = dict(row)
            a = '\n'
            for key, value in data.items():
                if a in value:
                    value = value.replace(a, "")
            list_of_data.append(data)

    list_of_data_sorted = sorted(list_of_data,
                                 key = lambda x: x['submission_time'],
                                 reverse=True)

    return list_of_data_sorted



def display_question(file_path, id):
    return csv_to_list(file_path)[id]

print(csv_to_list('sample_data/question.csv'))

def generate_new_id(file_path):
    data_list = csv_to_dict(file_path)
    id_ = 0
    for data in data_list:
        id_ = int(data['id'])
    id_gen = id_ + 1
    return str(id_gen)

def add_question(data):
    question['id'] = generate_new_id()
    add_data_to_file(data, True, 'question')

def add_answer(data):
    question['id'] = generate_new_id()
    add_data_to_file(data, True, 'answer')

def update_question(data):
    add_data_to_file(data, False, 'question')

def update_answer(data):
    add_data_to_file(data, False, 'answer')



def add_data_to_file(data, append=True, type):
    if type == 'question':
        data_header = ['id', 'submission_time', 'view_number', 'vote_number', 'title,message' ,'images']
        file_path = 'sample_data/question.csv'
    else:
        data_header = ['id', 'submission_time', 'vote_number' ,'question_id', 'message' ,'image']
        file_path = 'sample_data/answers.csv'
    existing_data = list_of_data_sorted()

    with open(file_path, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data_header)
        writer.writeheader()
        for row in existing_data:
            if not append:
                if row['id'] == data['id']:
                    row = data
            writer.writerow(row)
        if append:
            writer.writerow(data)
