from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('resume.html', title='Resume', profile=default_profile())

@app.route('/resume')
def resume():
    return render_template('resume.html', title='Resume', profile=default_profile())

@app.route('/contacts', methods=['GET','POST'])
def contacts():
    sent = False
    if request.method == 'POST':
        sent = True
    return render_template('contacts.html', title='Contacts', sent=sent)

def default_profile():
    return {
        "name": "Любомир Думенчук",
        "position": "Junior Web Developer",
        "about": "Коротко про себе: зацікавлений у веб-розробці, вмію Python та Flask.",
        "education": [{"year": "2020-2024", "text": "Бакалавр, ..."}],
        "skills": ["HTML", "CSS", "Bootstrap", "Python", "Flask"],
        "technologies": ["Git", "VSCode", "Bootstrap", "Jinja2"],
        "experience": [{"company":"Проект A", "desc":"Розробка ...", "period":"2024"}],
        "photo": url_for('static', filename='images/photo.jpg')
    }

if __name__ == '__main__':
    app.run(debug=True)
