#from server import app
from flask import Flask, render_template, request, flash, redirect, session


@app.route("/")
def homepage():
    """Homepage with login or create profile."""

    return render_template("welcome_page.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    """User registration/create a profile page"""

    if request.method == "POST":

        user_name = request.form["user_name"]
        email = request.form["email"]
        password = request.form["password"]
        passwordConf = request.form['passwordConf']

        if password == passwordConf:
            new_user = User(user_name, email=email)
            new_user.create_password(password)
        else:
            del new_user['passwordConf']

        db.session.add(new_user)
        db.session.commit()

        user_id = new_user.user_id
        session["user_id"] = user_id

        return redirect(f"/user_goals/{user_id}")
    else:
        return redirect("/")


@app.route("/api/auth", methods=["POST"])
def login_process():
    """Have a user login."""

    user = User.query.filter_by(email=request.form.get('email')).first()
    user_id = user.user_id

    if user.is_valid_password(request.form.get('password')):
        session['user_id'] = user.user_id
        return redirect(f"/user_goals/{user_id}")
    else:
        return redirect("/")


@app.route("/logout")
def logout():
    """User logout."""

    del session["user_id"]
    return redirect(f"/")