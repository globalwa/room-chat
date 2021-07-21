from flask import render_template, redirect, url_for, session
from app.forms import IndexForm
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'name' in session:
        return redirect(url_for('chat'))

    form = IndexForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data

        return redirect(url_for('chat'))

    return render_template('index.html', title='login', form=form)


@app.route('/chat')
def chat():
    if 'name' not in session:
        return redirect(url_for('index'))

    return render_template('chat.html', title='converse')


@app.route('/leave')
def leave():
    session.pop('name', None)
    session.pop('room', None)
    
    return redirect(url_for('index'))