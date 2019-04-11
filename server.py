from flask import Flask, render_template, request, url_for, redirect, session, abort, flash
import data_manager


app = Flask(__name__, template_folder='Templates')
app.secret_key = 'Impond3rabIlli@'


@app.route('/', methods=['GET', 'POST'])
def route_index():
    user_questions = data_manager.get_questions()

    return render_template('main_page.html', user_questions=user_questions)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def log_user():
    login = request.form.get('logusrname')
    password = request.form.get('logpswrd')
    if not data_manager.is_existing(login):
        flash('User not existant')
        return redirect('/login')
    if not data_manager.are_passwords_equal(password, login):
        flash('Incorrect password')
        return redirect('/login')
    session['username']=login
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')



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
    image = "Null"
    question_id = data_manager.insert_question_into_table(title, message, image)
    return redirect(url_for('route_spec_question', question_id=question_id))


@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def route_spec_question(question_id, count=True):
    count=request.args.get('count')
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
    image = "Null"
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
#
# @app.route("/login")
# def login_handler():
#


if __name__ == "__main__":
    app.run(debug=True)
