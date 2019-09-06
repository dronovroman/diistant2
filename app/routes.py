from flask import current_app
from flask import render_template


@current_app.route("/", methods=['GET', 'POST'])
def main():

    return render_template('index.html')


@current_app.route("/about", methods=['GET', 'POST'])
def about():

    return render_template('about.html')


@current_app.route("/build", methods=['GET', 'POST'])
def build():

    return render_template('build.html')
