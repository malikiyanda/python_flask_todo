from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' #this will set out dql lite 3 DB file inside the Env root dir.

 #create db
db = SQLAlchemy(app)

#create models 
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)
 
with app.app_context():
    db.create_all()

# x= 10
# y='ken'

@app.route('/') 
def index():
    todo_list = Todo.query.all()
    total_todo = Todo.query.count()
    completed_todo = Todo.query.filter_by(complete=True).count()
    uncompleted_todo = total_todo - completed_todo
    # return render_template('dashboard/index.html', todo_list=todo_list, total_todo=total_todo)
    return render_template('dashboard/index.html', **locals())
    # return render_template('dashboard/index.html', **globals())

@app.route ('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>')
def update(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.complete = not todo.complete
    db.session.commit() 
    return redirect(url_for('index'))

@app.route('/About')
def about():
    return render_template('dashboard/about.html')


# should be at the end of your python files
if __name__ == '__main__':
    app.run(debug=True)