from flask import Flask, render_template, url_for
import connection

app = Flask(__name__,template_folder = 'Templates')


@app.route('/')
def route_index():
    user_questions = connection.csv_to_list('sample_data/question.csv')

    return render_template('main_page.html', user_questions=user_questions)


@app.route('/add_question')
def route_add_question():
    return render_template('add_question.html')


@app.route('/question')
def route_question_list():
    user_questions = connection.csv_to_list('sample_data/question.csv')

    return render_template('question_page.html', user_questions=user_questions)


@app.route('/question/<int:id>', methods=['GET', 'POST'])
def route_spec_question(id):
    quest = connection.display_question(id)
    return render_template('question_page.html', quest=quest)

if __name__ == "__main__":
    app.run()