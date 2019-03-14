from flask import Flask, render_template, request, url_for, redirect
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
    question = connection.display_question('sample_data/question.csv', id)
    answers = data_manager.give_specific_answers(id, 'sample_data/answer.csv')
    generated_id = data_manager.generate_question_id()
    return render_template('question_page.html',
                           question=question,
                           answers=answers,
                           generated_id=generated_id)


@app.route('/question', methods=['POST'])
def dodaj_pytanie_do_pliku():
    new_question = data_manager.get_data_to_dict()
    connection.add_data_to_file()
    return redirect(url_for('route_spec_question', id=new_question['id']))


@app.route('/question/<id_>', methods=['POST'])
def add_new_answer(id_):
    id_ = int(id_)
    question = connection.display_question('sample_data/question.csv', id_)
    answers = data_manager.give_specific_answers(id_, connection.csv_to_list('sample_data/answer.csv'))
    generated_id = data_manager.generate_question_id('sample_data/answer.csv')
    answer_text = request.form["new_answer"]
    #TODO ->  zapisywanie do pliku 'answers'

    print(answer_text)

    return redirect(url_for('route_spec_question', id=question['id']))


if __name__ == "__main__":
    app.run(debug=True)
