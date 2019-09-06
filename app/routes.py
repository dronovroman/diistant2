from diistant2 import app
from flask import render_template


@app.route("/", methods=['GET'])
def main():

    return render_template('index.html')


@app.route("/about", methods=['GET'])
def about():

    return render_template('about.html')
