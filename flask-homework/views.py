import random
from flask import abort, request, redirect

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
    return f"""
    <h1>Main page</h1>
    <p>Here's links to other pages</p>
    <ul>
        <li><a href="/login">Login</a></li>
        <li><a href="/users">Users</a></li>
        <li><a href="/books">Books</a></li>
        <li><a href="/params">Params</a></li>
    </ul>
    """


@app.route('/hello')
def hello_world():
    app.logger.info("This is logger for page with endpoint /hello")
    return '<h1>Hello world!</h1>'


@app.route('/gethtml')
def get_html():
    app.logger.info("This is logger for page with endpoint /gethtml")
    return (
        '<h1>This page return html-code</h1>'
        '<p>Random text below header</p>'
    )


@app.route('/getjson')
def get_json():
    app.logger.info("This is logger for page with endpoint /getjson")
    return ({
        "user_1": {
            "name": "Ivan",
            "age": 18
        },
        "user_2": {
            "name": "Anatoliy",
            "age": 23
        }
    })


@app.route("/users")
def get_users():
    counter = request.args.get("count")
    if counter:
        counter = int(counter)
    else:
        counter = random.randint(1, 6)
    users_render = ''.join([
        f"<li>{user['first_name']} {user['second_name']}</li>"
        for user in random.sample(users, counter)
    ])

    response = f"""
    <h1>List of users</h1>
    <ul>
        {users_render}
    </ul>
    """
    return response, 200


@app.route("/books")
def get_books():
    books_render = ''.join([
        f"<li>Title: '{book['title']}', author: {book['author']}"
        for book in random.sample(books, len(books))
    ])

    response = f"""
    <h1>List of books</h1>
    <ul>
        {books_render}
    </ul>
    """
    return response, 200


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

    response = f"""
    <h1>Founded user:</h1>
    <p>First name: {user['first_name']}</p>
    <p>Second name: {user['second_name']}</p>
    """

    return response, 200


@app.get("/books/<string:title>")
def books_details(title):
    book = None
    title = str(title)
    edited_title = title.capitalize()
    for item in books:
        if edited_title == item["title"]:
            book = item
            break

    if not book:
        abort(404, "Book not found")

    response = f"""
    <h1>Founded book:</h1>
    <p>Title: {book['title']}</p>
    <p>Author: {book['author']}</p>
    """

    return response, 200


@app.route("/params")
def get_params():
    filters = request.args
    test_render = ''.join([
        f"<tr><td>{key}</td> <td>{value}</td></tr>"
        for key, value in filters.items()
    ])

    response = f"""
    <table>
        <thead>
            <tr><th>Parameter</th> <th>Value</th></tr>
        </thead>
        <tbody>
            {test_render}
        </tbody>
    </table>
    """

    return response, 200


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        if not username or not password:
            abort(400, "Missing data")

        if len(username) < 5:
            abort(400, "Invalid login data")

        if len(password) < 8 \
                or not any(map(str.isdigit, password)) \
                or not any(map(str.isupper, password)):
            abort(400, "Invalid login data")

        return redirect("/users")

    else:
        return f"""
        <form method="POST" action="/login">
            <label for="username">Username</label>
            <input type="text" name="username" id="username"><br><br>
        
            <label for="password">Password</label>
            <input type="password" name="password" id="password"><br><br>
        
            <input type="submit" value="Submit">
        </form>
        """


@app.errorhandler(404)
def error_not_found(error):
    return "<h1>You've caught a custom error 404!</h1>", 404


@app.errorhandler(500)
def server_error(error):
    return "<h1>Oops, my server is broken</h1>", 500
