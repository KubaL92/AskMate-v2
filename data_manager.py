import connection

def get_titles(user_stories: list) -> list:
    list_of_titles = []
    for i in user_stories:
        list_of_titles.append(i['title'])
    return list_of_titles

#print(get_titles(connection.csv_to_list('sample_data/question.csv')))