from flask import Flask, render_template


app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('templates_index.html')

if __name__ == '__main__':
    app.run(debug=True)
