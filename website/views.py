from datetime import datetime
from flask import Blueprint, redirect, render_template, url_for, request
from .models import Todo
from . import db

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def home():
    todo_list = Todo.query.all()
    message = request.args.get("message", None)
    return render_template("index.html", todo_list=todo_list, message = message)

@my_view.route("/add", methods= ["POST"])
def add():
    try:
        task = request.form.get("task")
        new_todo = Todo(task=task, date_created=datetime.utcnow())
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("my_view.home"))
    except:
        message ="There was error adding your task."
        return redirect(url_for("my_view.home"), message=message)

@my_view.route("/update/<todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("my_view.home"),)

@my_view.route("/toggle/<todo_id>", methods=["POST"])
def toggle (todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("my_view.home"))


@my_view.route("/delete/<todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

@my_view.route("/edit/<todo_id>", methods=["GET", "POST"])
def edit(todo_id):
    todo = Todo.query.get(todo_id)

    if request.method == "POST":
        new_task = request.form.get("new_task")
        todo.task = new_task
        db.session.commit()
        return redirect(url_for("my_view.home"))

    return render_template("edit.html", todo=todo)