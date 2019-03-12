from flask import Flask, render_template, request, url_for
import connection, data_manager

app = Flask(__name__, template_folder='Templates')


@app.route('/')
def route_index():
    user_questions = connection.csv_to_list('sample_data/question.csv')

    return render_template('main_page.html', user_questions=user_questions)


@app.route('/add_question')
def route_add_question():
    return render_template('add_question.html')


@app.route('/question/<int:id>', methods=['GET', 'POST'])
def route_spec_question(id):
    quest = connection.display_question('sample_data/question.csv', id)
    answers = connection.csv_to_list('sample_data/answer.csv')
    generated_id = data_manager.generate_question_id()
    # answers = connection.display_question('sample_data/answer.csv', id)
    return render_template('question_page.html',
                           quest=quest,
                           answers=answers,
                           generated_id=generated_id)


@app.route('/question', methods=['POST'])
def dodaj_pytanie_do_pliku():
    question_title = request.form['title']
    question_message = request.form['question']
    cały_text = question_message + '' + question_title
    return redirect




# @app.route('/question/<int:id>', methods=['GET', 'POST'])
# def route_new_question():
#     generated_id = data_manager.generate_question_id()
#     return render_template('question_page.html', generated_id=generated_id)


if __name__ == "__main__":
    app.run(debug=True)
