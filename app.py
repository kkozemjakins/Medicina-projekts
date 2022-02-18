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
    darbjoma = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    article = db.Column(db.String(20), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Task %r' % self.id

class Slimnicas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    adrese = db.Column(db.String(30), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Slimnicas %r' % self.id

class Vizit(db.Model):
    get = Todo()

    id = db.Column(db.Integer, primary_key=True)
    DARBJOMA = db.Column(db.String(20), nullable=False)
    TITLE = db.Column(db.String(20), nullable=False)
    ARTICLE = db.Column(db.String(20), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    ARTICLE = get.article
    TITLE = get.title
    DARBJOMA = get.darbjoma

    def __repr__(self):
        return 'Izvele %r' % self.id


@app.route('/')
def sakum_login():
  return render_template("login.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/guest_visits')
def guest_visits():
  return render_template("guest_visits.html", tasks3=Vizit.query.all())

@app.route('/guest_main')
def guest_main():
  return render_template("guest_main.html",  tasks=Todo.query.all(), tasks3=Vizit.query.all())

@app.route('/admin_main')
def admin_main():
  return render_template("admin_main.html")

@app.route('/admin_doctor_page')
def admin_doctor_page():
  return render_template("admin_doctor_page.html", tasks=Todo.query.all(), tasks2=Slimnicas.query.all())

@app.route('/admin_hospital_page')
def admin_hospital_page():
  return render_template("admin_hospital_page.html", tasks2=Slimnicas.query.all(), tasks=Todo.query.all())

@app.route('/admin_statistika')
def admin_statistika():
  return render_template("admin_statistika.html")

@app.route('/lapa_priekš_drukāšanai')
def lapa_priekš_drukāšanai():
  return render_template("lapa_priekš_drukāšanai.html")


# Doctor page
@app.route('/ok', methods=['POST', 'GET'])
def doctors():
    if request.method == 'POST':
      new_task = Todo(darbjoma=request.form['darbjoma'], title=request.form['title'], article=request.form['article'])

      try:
        db.session.add(new_task)
        db.session.commit()
        return redirect('/ok')
      except:
        return "Error"
    else:
      slimnicas = Slimnicas.query.order_by(Slimnicas.id).all()
      tasks = Todo.query.order_by(Todo.date_created).all()
      return render_template("admin_doctor_page.html", tasks=tasks, slimnicas=slimnicas, tasks2=Slimnicas.query.all())


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
        task.darbjoma = request.form['darbjoma']
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

      new_slimnica = Slimnicas(content=request.form['content'], adrese=request.form['adrese'])

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
        task.content = request.form['content']
        task.adrese = request.form['adrese']

        try:
            db.session.commit()
            return redirect('/ok2')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update_hospital_page.html', task=task)

#Vizit
@app.route('/ok4', methods=['POST', 'GET'])
def vizites():
    if request.method == 'POST':
      get = Todo()

      new_vizit = Vizit(DARBJOMA=request.form['DARBJOMA'], TITLE=request.form['TITLE'], ARTICLE=request.form['ARTICLE'])

      try:
        db.session.add(new_vizit)
        db.session.commit()
        return redirect('/ok4')
      except:
        return "Error"
    else:
      tasks3 = Vizit.query.order_by(Vizit.date_created).all()
      return render_template("guest_main.html", tasks3=tasks3)


if __name__ == "__main__": 
  app.run(host='0.0.0.0', port=8080)