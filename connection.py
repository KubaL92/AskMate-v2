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

print(csv_to_list('sample_data/question.csv'))

def generate_new_id(file_path):
    data_list = csv_to_list(file_path)
    id_ = 0
    for data in data_list:
        id_ = int(data['id'])
    id_gen = id_ + 1
    return str(id_gen)


def add_question(data):
    data['id'] = generate_new_id()
    add_data_to_file(data, 'question', True)


def add_answer(data):
    data['id'] = generate_new_id()
    add_data_to_file(data, 'answer', True)


def update_question(data):
    add_data_to_file(data, 'question', False)


def update_answer(data):
    add_data_to_file(data, 'answer', False)


def add_data_to_file(data, type_, append=True):
    if type_ == 'question':
        data_header = ['id', 'submission_time', 'view_number', 'vote_number', 'title,message' ,'images']
        file_path = 'sample_data/question.csv'
    else:
        data_header = ['id', 'submission_time', 'vote_number' ,'question_id', 'message' ,'image']
        file_path = 'sample_data/answers.csv'
    existing_data = csv_to_list()

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
