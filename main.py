from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def index():
  return render_template("guest_main.html")

@app.route('/guest_visits')
def guest_visits():
  return render_template("guest_visits.html")

@app.route('/guest_main')
def guest_main():
  return render_template("guest_main.html")



app.run(host='0.0.0.0', port=8080)