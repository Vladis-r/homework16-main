from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/")
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
    app.run(debug=True)

Hello world fucken git hub