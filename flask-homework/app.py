from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
    app.logger.info("This is logger for main page")
    return '<h1>Main page</h1>'


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


if __name__ == '__main__':
    app.run(debug=True)
