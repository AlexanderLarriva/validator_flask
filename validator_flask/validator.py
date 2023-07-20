# BEGIN (write your solution here)

# course_data = {'paid': True; 'title': 'Flask'}

def validate(course_data):
    errors = {}
    if not course_data['paid']:
        errors['paid'] = "Can't be blank"
    if not course_data['title']:
        errors['title'] = "Can't be blank"

    return errors
# END
