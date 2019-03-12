def unix_to_gmit():
    for time in (csv_to_list('sample_data/question.csv')[[2]]):
        time = int(time)
    print(datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'))

unix_to_gmit()

def gmit_to_unix():