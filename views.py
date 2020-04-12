from server import app
from flask import Flask, render_template, request, redirect, session, jsonify
from model import Model, db, User, Goal
from sqlalchemy import update

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


@app.route("/add_goal", methods=["GET", "POST"])
def add_goal():
    """User can add short notes to their homepage."""

    user_id = session["user_id"]

    if request.method == "POST":
        goal = request.form["goal"]
        new_goal = Goal(goal=goal, user_id=user_id)

        db.session.add(new_goal)
        db.session.commit()

        # goal_id = new_goal.goal_id
        return jsonify({"goal_id": new_goal.goal_id, "Goal": new_goal.goal})
    else:
        return redirect(f"/")

@app.route("/edit_goal")
def edit_goal():
    """Function to search the user's goals"""

    user_id = session["user_id"]
    goal = Goal.query(User).get(user_id)
    goal_id = goal.goal_id
    updated_goal = goal.update(). \
        where(goal_id=goal_id). \
        values(goal='')

    return jsonify({"goal_id": goal.goal_id, "Goal": updated_goal.goal})


@app.route("/logout")
def logout():
    """User logout."""

    del session["user_id"]
    return redirect(f"/")