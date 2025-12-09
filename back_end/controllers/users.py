from back_end import app
from flask import render_template, request, redirect, session, flash, url_for
from back_end.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def home_page():
    return render_template("Home.html")

@app.route('/city')
def city_page():
    return render_template("City.html")

@app.route('/register')
def register_page():
    return render_template("Register.html")

@app.route('/login')
def login_page():
    return render_template("Login.html")

@app.route('/club/tunis')
def club_tunis():
    return render_template("ClubTunis.html")

@app.route('/club/sousse')
def club_sousse():
    return render_template("ClubSousse.html")




@app.route('/users/create', methods=['POST'])
def register():
    print("FORM RECEIVED:", request.form)
    if not User.validate_register(request.form):
        return redirect(url_for('register_page'))
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }

    new_user_id = User.create(data)
    session['user_id'] = new_user_id
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        return redirect(url_for('login_page'))

    user = User.get_by_id({"id": session['user_id']})
    return render_template("Home.html", user=user)

@app.route('/login_user', methods=['POST'])
def login_user():
    data = { "email": request.form['email'] }
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Email not found", "login")
        return redirect(url_for('login_page'))

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Wrong password", "login")
        return redirect(url_for('login_page'))

    session['user_id'] = user_in_db.id
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home_page'))
