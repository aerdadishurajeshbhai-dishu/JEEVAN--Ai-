import os
from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    
    possible_files = ['template_index.html', 'templates_index.html', 'index.html']
    
    for filename in possible_files:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return render_template_string(f.read())
                
    return "Error: HTML file not found! Please check your GitHub repository file name."

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
