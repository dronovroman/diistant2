from dotenv import load_dotenv
from app import create_app, db
from flask_migrate import Migrate, upgrade


load_dotenv()


app = create_app()
migrate = Migrate(app=app, db=db)


@app.cli.command()
def createdb():
    db.create_all()


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command()
def deploy():
    # Migrate db to latest revision
    upgrade()
