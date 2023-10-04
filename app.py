from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample todo list
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    todos.append(todo)
    return redirect('/')

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    if todo_id < len(todos):
        todos.pop(todo_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)