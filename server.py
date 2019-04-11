from flask import Flask, render_template, request, url_for, redirect
import data_manager


app = Flask(__name__, template_folder='Templates')


@app.route('/', methods=['GET', 'POST'])
def route_index():
    user_questions = data_manager.get_questions()

    return render_template('main_page.html', user_questions=user_questions)


@app.route('/login')
def login_page():

    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def validate_login_data():
    user_name = request.form['logusrname']
    password = request.form['logpswrd']
    hashed_password = data_manager.hashing_parole(password)
    return redirect(url_for('route_index'))

@app.route('/registration')
def registration_page():
    return render_template('registration.html')


@app.route('/registration', methods=['GET', 'POST'])
def add_user_to_database():
    user_name = request.form['regusrname']
    password = request.form['regpswrd']
    hashed_password = data_manager.hashing_parole(password)
    usr_id = data_manager.processing_registration_data(user_name, hashed_password)
    return redirect('route_index', usr_id=usr_id)

@app.route('/add_question')
def route_add_question():
    return render_template('add_question.html')


@app.route('/add_answer/<id>')
def ans_site(id):
    return render_template('add_answer.html', id=id)


@app.route('/question', methods=['POST'])
def add_question_to_database():
    title = request.form["title"]
    message = request.form["question"]
    image = request.form["image"]
    question_id = data_manager.insert_question_into_table(title, message, image)
    return redirect(url_for('route_spec_question', question_id=question_id))


@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def route_spec_question(question_id, count=True):
    if count == True:
        data_manager.update_question_view_number(question_id)
    question = data_manager.get_questions_with_specific_id(question_id)
    answers = data_manager.get_answers(question_id)
    return render_template('question_page.html',
                           question=question,
                           answers=answers)


@app.route('/submit_answer/<int:question_id>', methods=['POST'])
def add_new_answer_to_db(question_id):

    answer = request.form["new_answer"]
    image = request.form["image"]
    data_manager.insert_answer_to_db(question_id, answer, image)
    return redirect(url_for('route_spec_question', question_id=question_id))


@app.route("/question/<int:question_id>/delete/<id>")
def delete_questions_answer(question_id, id):
    data_manager.delete_answer_from_db(id)
    return redirect(url_for('route_spec_question', question_id=question_id))

@app.route("/question/<int:question_id>/upvote/<id>")
def upvote_answer(question_id, id):
    data_manager.upvote_answer(id)
    return redirect(url_for('route_spec_question', question_id=question_id, count=False))



@app.route("/question/<int:question_id>/downvote/<id>")
def downvote_answer(question_id, id):
    data_manager.downvote_answer(id)
    return redirect(url_for('route_spec_question', question_id=question_id, count=False))




@app.route("/delete-question/<id>")
def delete_question(id):
    data_manager.delete_question_from_db(id)
    return redirect('/')



"""
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
"""

if __name__ == "__main__":
    app.run(debug=True)
