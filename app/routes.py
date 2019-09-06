from diistant2 import app
from flask import current_app
from flask import render_template


@current_app.route("/", methods=['GET', 'POST'])
def main():

    return render_template('index.html')
