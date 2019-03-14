import csv
import data_manager

def csv_to_list(file_path: object) -> object:
    user_stories = []

    #  open csv file to read
    with open(file_path) as csvfile:
        #  use DictReader to directly create dictionaries from each lines in the csv file
        # csvfile = csvfile.replace('\n','')
        reader = csv.DictReader(csvfile)

        #  read all lines in csv file
        for row in reader:
            #  make a copy of the read row, since we can't modify it
            user_story = dict(row)
            a = '\n'
            for key, value in user_story.items():
                if a in value:
                    value = value.replace(a, "")

        #  store modified data in temporary list
            user_stories.append(user_story)

    # user_stories_sorted = sorted(user_stories,
    #                              key = lambda x: x['submission_time'],
    #                              reverse=True)
    #
    # # return the temporary list
    return user_stories

# for i in csv_to_list('sample_data/question.csv'):
#     print(i)


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

