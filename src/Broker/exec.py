from flask import Flask
from server import app
from api import connect_user


if __name__ == '__main__':
    app.run(debug=True)