from flask import Flask, render_template, url_for, request, flash


app = Flask(__name__)
app.secret_key = 'super secret key'
# app.config['SESSION_TYPE'] = 'filesys'
# menu = ('Установка', 'Первое приложение', 'Обратная связь')
menu = [
    {'name': 'Установка', 'url': 'install-flask'},
    {'name': 'Первое приложение', 'url': 'first-app'},
    {'name': 'Обратная связь', 'url': 'contact'},
]

@app.route("/")
def index():
    # print("url_for('index'):" + url_for('index'))
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    # print("url_for('about'):" + url_for('about'))
    return render_template('about.html', title='О сайте', menu=menu)


@app.route("/profile/<username>/<int:id>")
def profile(username, id):
    return f'Пользователь: {username}, {id}'


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        # print(request.form)
        print('username:' + request.form['username'])
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template('contact.html', title='Обратная связь', menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu), 404

if __name__ == '__main__':
    app.run(debug=True, port=5556)
