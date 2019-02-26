import csv

def transform_questions_into_list():
    with open('sample_data/question.csv', 'r') as file:
        reader = csv.reader(file)
        my_list = list(reader)
        del my_list[0]
        return my_list

print(transform_questions_into_list())
