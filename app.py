from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # આ લાઈન તમારી 'templates_index.html' ફાઈલને ઓપન કરશે
    return render_template('templates_index.html')

if __name__ == '__main__':
    app.run(debug=True)

