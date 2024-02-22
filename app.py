from flask import Flask, abort, render_template, request

app = Flask(__name__)
people = ['Isabel', 'Maria', 'Ana', 'Javier', 'Pablo']
new_people = ['Elena', 'Carmen', 'Alfonso']


@app.route('/page1/<username>')
def show_template(username):
    return render_template('page1.html', name=username.upper())


@app.route('/hello/<user_id>')
def example_route(user_id):
    return f'Hello, {user_id}!'


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error_detail=error), 404


@app.route('/not_defined')
def not_defined():
    abort(404)


@app.route('/people/<username>')
def people_page(username):
    return render_template('people.html', employees_names=people, boss_name=username.upper())


@app.route('/new_people/<username>')
def new_people_page(username):
    return render_template('new_people.html', employees_names=new_people, boss_name=username.upper())


@app.route('/extended_page')
def extended_page():
    return render_template('extended_page.html')


@app.route('/form', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        return render_template('form_example.html',
                               show_info_box=True, username=request.form.get('username'),
                               email=f"{request.form.get('email_username')}@{request.form.get('email_server')}",
                               description=request.form.get('description'))

    if request.method == 'GET':
        return render_template('form_example.html', show_info_box=False)


@app.route('/examplePage')
def basic_example():
    return "<h1>Example Page!</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
