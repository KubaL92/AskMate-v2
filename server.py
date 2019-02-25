from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def route_index():
    return render_template('/main_page.html')

"""if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )"""