import random

from flask import abort, request, redirect, render_template, session, url_for

from app import app

users = [
    {
        "id": 1,
        "first_name": "Andriy",
        "second_name": "Ivanov"
    },
    {
        "id": 2,
        "first_name": "Ivan",
        "second_name": "Petrov"
    },
    {
        "id": 3,
        "first_name": "John",
        "second_name": "Sydorov"
    },
    {
        "id": 4,
        "first_name": "Vitalii",
        "second_name": "Kovalenko"
    },
    {
        "id": 5,
        "first_name": "Oleg",
        "second_name": "Vasylenko"
    },
    {
        "id": 6,
        "first_name": "Olexandr",
        "second_name": "Lysenko"
    }
]

books = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell"
    },
    {
        "id": 2,
        "title": "Kobzar",
        "author": "Taras Shevchenko"
    },
    {
        "id": 3,
        "title": "Tyhrolovy",
        "author": "Vasyl Shkliar"
    },
    {
        "id": 4,
        "title": "Mamai",
        "author": "Vasyl Sukhomlynskyi"
    },
    {
        "id": 5,
        "title": "Zyma",
        "author": "Borys Hrinchenko"
    },
    {
        "id": 6,
        "title": "Lis",
        "author": "Vasyl Stus"
    }
]


@app.route('/')
def main_page():
    app.logger.info("This is logger for main page")
    return render_template("main.html"), 200


@app.route("/users")
def get_users():
    counter = request.args.get("count")
    if counter:
        counter = int(counter)
    else:
        counter = random.randint(1, 6)

    users_render = [user for user in random.sample(users, counter)]

    context = {
        "title": "Users",
        "users": users_render
    }

    return render_template("users/users.html", **context), 200


@app.route("/books")
def get_books():
    books_render = [book for book in random.sample(books, len(books))]

    context = {
        "title": "Books",
        "books": books_render
    }

    return render_template("books/books.html", **context), 200


@app.get("/users/<user_id>")
def user_details(user_id):
    try:
        user_id_int = int(user_id)
    except ValueError:
        abort(400, 'Invalid user id')

    user = None

    for item in users:
        if user_id_int == item["id"]:
            user = item
            break

    if not user:
        abort(404, "User not found")

    context = {
        "title": "User details",
        "user": user
    }

    return render_template("users/user_details.html", **context), 200


@app.get("/books/<string:title>")
def book_details(title):
    book = None
    title = str(title)
    edited_title = title.capitalize()
    for item in books:
        if edited_title == item["title"]:
            book = item
            break

    if not book:
        abort(404, "Book not found")

    context = {
        "title": "Book_details",
        "book": book
    }

    return render_template("books/book_details.html", **context), 200


@app.route("/params")
def get_params():
    filters = request.args
    params_render = [{"key": key, "value": value} for key, value in filters.items()]

    context = {
        "title": "Parameters",
        "params": params_render
    }

    return render_template("parameters/params.html", **context), 200


@app.route("/login", methods=['GET', 'POST'])
def login():
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