from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms import ContactForm

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

@main_bp.route('/contacts', methods=['GET', 'POST'])
def contacts():
    form = ContactForm()
    
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        with open("contact.log", "a", encoding="utf-8") as f:
            f.write(f"{name} | {email} | {message}\n")

        flash("Message sent successfully!", "success")
        return redirect(url_for('main.contacts'))  

    if form.errors:
        flash("Form contains errors", "danger")

    return render_template(
        'contacts.html',
        title="Contacts",
        form=form
    )
