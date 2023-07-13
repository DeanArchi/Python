import random
from functools import wraps

from flask import abort, request, redirect, render_template, session, url_for, jsonify
from app import app, db
from models import *


def is_user_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "username" in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return wrapper


@app.get('/')
@is_user_logged_in
def main_page():
    app.logger.info("This is logger for main page")
    return render_template("main.html", username=session["username"]), 200


@app.get("/users")
@is_user_logged_in
def get_users():
    counter = request.args.get("count")

    if counter:
        query = db.select(User).limit(counter)
    else:
        query = db.select(User)

    users_render = db.session.execute(query).scalars()

    context = {
        "title": "Users",
        "username": session["username"],
        "users": users_render
    }

    return render_template("users/users.html", **context), 200


@app.post("/users")
@is_user_logged_in
def create_user():
    data = request.json
    first_name = data.get("first_name")
    last_name = data.get("last_name")

    if not first_name or not last_name:
        abort(400, "Missing required fields")

    user = User(
        first_name=first_name,
        last_name=last_name
    )

    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201


@app.get("/books")
@is_user_logged_in
def get_books():
    query = db.select(Book)
    books_render = db.session.execute(query).scalars()

    context = {
        "title": "Books",
        "username": session["username"],
        "books": books_render
    }

    return render_template("books/books.html", **context), 200


@app.post("/books")
@is_user_logged_in
def create_book():
    data = request.json
    title = data.get("title")
    author = data.get("author")
    price = data.get("price")

    if not title or not author or not price:
        abort(400, "Missing required fields")

    book = Book(
        title=title,
        author=author,
        price=price
    )

    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Book created"}), 201


@app.get("/users/<user_id>")
@is_user_logged_in
def user_details(user_id):
    try:
        user_id_int = int(user_id)
    except ValueError:
        abort(400, 'Invalid user id')

    user = None

    query = db.select(User)
    users = db.session.execute(query).scalars()

    for item in users:
        if user_id_int == item.id:
            user = item
            break

    if not user:
        abort(404, "User not found")

    context = {
        "title": "User details",
        "username": session["username"],
        "user": user
    }

    return render_template("users/user_details.html", **context), 200


@app.get("/books/<string:title>")
@is_user_logged_in
def book_details(title):
    book = None
    title = str(title)
    edited_title = title.capitalize()

    query = db.select(Book)
    books = db.session.execute(query).scalars()
    for item in books:
        if edited_title == item.title:
            book = item
            break

    if not book:
        abort(404, "Book not found")

    context = {
        "title": "Book_details",
        "username": session["username"],
        "book": book
    }

    return render_template("books/book_details.html", **context), 200


@app.get("/purchases")
@is_user_logged_in
def get_purchases():
    query = db.select(User.first_name, User.last_name, Book.title, Book.author)\
        .join(Purchase, User.id == Purchase.user_id)\
        .join(Book, Book.id == Purchase.book_id)

    purchases_render = db.session.execute(query)

    context = {
        "title": "Purchases_list",
        "username": session["username"],
        "purchases": purchases_render
    }
    return render_template("purchases/purchases.html", **context), 200


@app.get("/purchases/<int:purchase_id>")
@is_user_logged_in
def purchase_details(purchase_id):
    try:
        purchase_id = int(purchase_id)
    except ValueError:
        abort(400, "Invalid purchase id")

    purchase = None

    query = db.select(Purchase)
    purchases = db.session.execute(query).scalars()

    for item in purchases:
        if purchase_id == item.id:
            purchase = item
            break

    if not purchase:
        abort(404, "Purchase not found")

    user_query = db.select(User).where(User.id == Purchase.user_id)
    book_query = db.select(Book).where(Book.id == Purchase.book_id)

    user = db.session.execute(user_query).scalar()
    book = db.session.execute(book_query).scalar()

    context = {
        "title": "User details",
        "username": session["username"],
        "purchase": purchase.id,
        "user": user,
        "book": book
    }

    return render_template("purchases/purchase_details.html", **context), 200


@app.post("/purchases")
def create_purchase():
    data = request.json
    user_id = data.get("user_id")
    book_id = data.get("book_id")

    if not user_id or not book_id:
        abort(400, "Missing required fields")

    user_query = db.select(User.id)
    users_id = [user[0] for user in db.session.execute(user_query)]
    if user_id not in users_id:
        abort(400, "User not found")

    book_query = db.select(Book.id)
    books_id = [book[0] for book in db.session.execute(book_query)]
    if book_id not in books_id:
        abort(400, "Book not found")

    purchase = Purchase(
        user_id=user_id,
        book_id=book_id
    )

    db.session.add(purchase)
    db.session.commit()
    return jsonify({"message": "Purchase created"}), 201


@app.route("/params")
@is_user_logged_in
def get_params():
    filters = request.args
    params_render = [{"key": key, "value": value} for key, value in filters.items()]

    context = {
        "title": "Parameters",
        "username": session["username"],
        "params": params_render
    }

    return render_template("parameters/params.html", **context), 200


@app.route("/login", methods=['GET', 'POST'])
def login():
    if "username" in session:
        return redirect(url_for("main_page"))
    else:
        if request.method == 'POST':
            username = request.form.get("username")
            password = request.form.get("password")

            if not username or not password:
                abort(400, "Missing data")

            if len(username) < 5:
                abort(400, "Invalid login data")

            if len(password) < 8 \
                    or not any(map(str.isdigit, password)) \
                    or not any(map(str.isupper, password)):
                abort(400, "Invalid login data")

            session["username"] = username

            return redirect(url_for("get_users"))

        else:
            return render_template("login/login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.errorhandler(404)
def error_not_found(error):
    return "<h1>You've caught a custom error 404!</h1>", 404


@app.errorhandler(500)
def server_error(error):
    return "<h1>Oops, my server is broken</h1>", 500
