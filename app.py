from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__, static_url_path='/static')

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_description = request.form.get('task')
    date_str = request.form.get('date')
    date = datetime.strptime(date_str, '%Y-%m-%d')
    task = (task_description, date)
    tasks.append(task)
    return redirect('/')

@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_index = int(request.form.get('task_index'))
    del tasks[task_index]
    return redirect('/')

@app.route('/show_task/<int:task_index>')
def show_task(task_index):
    task, date = tasks[task_index]
    return render_template('show.html', task=task, date=date)

if __name__ == '__main__':
    app.run(debug=True)

