import csv


def csv_to_list(file_path: str) -> list:
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

    user_stories_sorted = sorted(user_stories,
                                 key = lambda x: x['submission_time'],
                                 reverse=True)

    # return the temporary list
    return user_stories_sorted

# for i in csv_to_list('sample_data/question.csv'):
#     print(i)


def display_question(file_path, id):
    return csv_to_list(file_path)[id]


# print(display_question('sample_data/answer.csv',0))
print(csv_to_list('sample_data/answer.csv'))