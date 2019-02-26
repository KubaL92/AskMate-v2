from flask import Flask, render_template

app = Flask(__name__,template_folder = 'Templates')


@app.route('/')
def route_index():
    return render_template('main_page.html')


@app.route('/add_question')
def route_add_question():
    return render_template('add_question.html')

if __name__ == "__main__":
    app.run()
