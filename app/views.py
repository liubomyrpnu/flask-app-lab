from flask import Blueprint, render_template, request, url_for

main_bp = Blueprint('main', __name__)

def default_profile():
    return {
        'name': 'Любомир Думенчук',
        'position': 'Junior Web Developer',
        'about': 'Коротко про себе: зацікавлений у веб-розробці, вмію Python та Flask.',
        'education': [{'year': '2020-2024', 'text': 'Бакалавр, ...'}],
        'skills': ['HTML','CSS','Bootstrap','Python','Flask'],
        'technologies': ['Git','VSCode','Bootstrap','Jinja2'],
        'experience': [{'company':'Проект A','desc':'Розробка ...','period':'2024'}],
        'photo': url_for('static', filename='images/photo.jpg')
    }

@main_bp.route('/')
def index():
    return render_template('resume.html', title='Resume', profile=default_profile())

@main_bp.route('/resume')
def resume():
    return render_template('resume.html', title='Resume', profile=default_profile())

@main_bp.route('/contacts', methods=['GET','POST'])
def contacts():
    sent = False
    if request.method == 'POST':
        sent = True
    return render_template('contacts.html', title='Contacts', sent=sent)
