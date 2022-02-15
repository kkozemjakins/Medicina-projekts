from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    article = db.Column(db.String(20), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Task %r' % self.id

class Slimnicas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nosaukums = db.Column(db.String(20), nullable=False)
    adrese = db.Column(db.String(30), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Slimnicas %r' % self.id

@app.route('/')
def sakum_login():
  return render_template("login.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/guest_visits')
def guest_visits():
  return render_template("guest_visits.html")

@app.route('/guest_main')
def guest_main():
  return render_template("guest_main.html")

@app.route('/admin_main')
def admin_main():
  return render_template("admin_main.html")

@app.route('/admin_doctor_page')
def admin_doctor_page():
  return render_template("admin_doctor_page.html")

@app.route('/admin_hospital_page')
def admin_hospital_page():
  return render_template("admin_hospital_page.html")

@app.route('/admin_statistika')
def admin_statistika():
  return render_template("admin_statistika.html")


# Doctor page
@app.route('/ok', methods=['POST', 'GET'])
def doctors():
    if request.method == 'POST':

      new_task = Todo(content=request.form['content'], title=request.form['title'], article=request.form['article'])

      try:
        db.session.add(new_task)
        db.session.commit()
        return redirect('/ok')
      except:
        return "che delat to"
    else:
      tasks = Todo.query.order_by(Todo.date_created).all()
      return render_template("admin_doctor_page.html", tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/ok')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        task.title = request.form['title']
        task.article = request.form['article']

        try:
            db.session.commit()
            return redirect('/ok')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update_doctor_page.html', task=task)

# Slimnicas page
@app.route('/ok2', methods=['POST', 'GET'])
def slimnicas():
    if request.method == 'POST':

      new_slimnica = Slimnicas(nosaukums=request.form['nosaukums'], adrese=request.form['adrese'])

      try:
        db.session.add(new_slimnica)
        db.session.commit()
        return redirect('/ok2')
      except:
        return "Error"
    else:
      tasks2 = Slimnicas.query.order_by(Slimnicas.date_created).all()
      return render_template("admin_hospital_page.html", tasks2=tasks2)


@app.route('/delete2/<int:id>')
def delete2(id):
    slimnica_to_delete = Slimnicas.query.get_or_404(id)

    try:
        db.session.delete(slimnica_to_delete)
        db.session.commit()
        return redirect('/ok2')
    except:
        return 'There was a problem deleting that task'

@app.route('/update2/<int:id>', methods=['GET', 'POST'])
def update2(id):
    task = Slimnicas.query.get_or_404(id)

    if request.method == 'POST':
        task.nosaukums = request.form['nosaukums']
        task.adrese = request.form['adrese']

        try:
            db.session.commit()
            return redirect('/ok2')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update_hospital_page.html', task=task)


if __name__ == "__main__": 
  app.run(host='0.0.0.0', port=8080)
