from flask import Flask, redirect, render_template, request, make_response
# BEGIN (write your solution here)
from validator_flask.validator import validate


# END
import os

from validator_flask.data import Repository


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


repo = Repository()


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/courses')
def courses_get():
    courses = repo.content()
    return render_template(
        'courses/index.html',
        courses=courses,
    )


# BEGIN (write your solution here)
@app.route('/courses/new', methods=['GET', 'POST'])
def show_form():
    if request.method == 'POST':
        title = request.form.get('title')
        paid = request.form.get('paid')
        course_data = {'title': title, 'paid': paid}
        errors = validate(course_data)
        if errors:
            return render_template(
                'courses/new.html',
                course_data=course_data,
                errors=errors,
            ), 422  # Код ответа 422 для ошибки валидации
        repo.save(course_data)
        return redirect('/courses')  # Редирект при успешном сохранении курса
    
    return render_template('courses/new.html')

# END
