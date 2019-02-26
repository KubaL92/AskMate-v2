from flask import Flask, render_template
import data_manager

app = Flask(__name__,template_folder = 'Templates')


@app.route('/')
def route_index():
    user_questions = data_manager.get_titles(data_manager.csv_to_list('sample_data/question.csv'))

    return render_template('main_page.html', user_questions=user_questions)


@app.route('/add_question')
def route_add_question():
    return render_template('add_question.html')

if __name__ == "__main__":
    app.run()
