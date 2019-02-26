import csv

def csv_to_list(file_path: str) -> list:
        one_user_story_id = "c"
        user_stories = []

        #  open csv file to read
        with open(file_path) as csvfile:
        #  use DictReader to directly create dictionaries from each lines in the csv file
                reader = csv.DictReader(csvfile)

                #  read all lines in csv file
                for row in reader:
                #  make a copy of the read row, since we can't modify it
                        user_story = dict(row)

                # if filtered, then just return this _found_ user story
                        if one_user_story_id is not None and one_user_story_id == user_story['id']:
                                return user_story

                #  store modified data in temporary list
                        user_stories.append(user_story)

        # return the temporary list
                return user_stories


