from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def sakum_login():
  return render_template("login.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/')
def index():
  return render_template("guest_main.html")

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





app.run(host='0.0.0.0', port=8080)