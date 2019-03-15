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


@app.route('/question', methods=['POST'])
def dodaj_pytanie_do_pliku():
    new_question = data_manager.get_data_to_dict()
    connection.add_data_to_file()
    return redirect(url_for('route_spec_question', id=new_question['id']))

@app.route('/question/<int:id>', methods=['GET', 'POST'])
def route_spec_question(id):
    connection.save_updated_view_number('sample_data/question.csv', id)
    question = connection.display_question('sample_data/question.csv', id)
    answers = data_manager.give_specific_answers(id, connection.csv_to_list('sample_data/answer.csv'))
    generated_id = data_manager.generate_question_id()
    return render_template('question_page.html',
                           question=question,
                           answers=answers,
                           generated_id=generated_id)

@app.route('/add_answer/<id>')
def ans_site(id):
    return render_template('add_answer.html', id=id)

@app.route('/delete_question')
def delete_question_site():
    return render_template('delete_question.html')

# @app.route('/delete_question', methods=['POST'])
#     def delete_question(id):



@app.route('/question/<id_>/new-answer', methods=['POST'])
def add_new_answer(id_):
    id_ = int(id_)
    question = connection.display_question('sample_data/question.csv', id_)
    answers = data_manager.give_specific_answers(id_, connection.csv_to_list('sample_data/answer.csv'))
    generated_id = data_manager.generate_question_id('sample_data/answer.csv')
    answer_text = request.form["new_answer"]
    #TODO ->  zapisywanie do pliku 'answers'

@app.route('/add_answer/<id>', methods=['POST'])
def dodaj_odp_do_pliku(id):
    new_answer = data_manager.get_answer_to_dict(id)
    connection.add_answer_to_file(new_answer)
    return redirect('/question/%s' % id)

@app.route("/list", methods=['GET'])
def order_question():
    user_questions = connection.csv_to_list('sample_data/question.csv')

    order_by = request.args.get('order_by')
    order_direction = request.args.get('order_direction')
    if order_by in ["id", "submission_time", "view_number", "vote_number", "title", "message", "image"]:
        if order_direction == "asc":
            user_questions = sorted(user_questions, key=lambda dict_: dict_[order_by])
        else:
            user_questions = sorted(
                user_questions,
                key=lambda dict_: dict_[order_by],
                reverse=True)

        return render_template('main_page.html', user_questions=user_questions)
    return render_template('main_page.html', user_questions=user_questions)


if __name__ == "__main__":
    app.run(debug=True)
