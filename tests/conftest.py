# tests/conftest.py
import pytest
from app import create_app
from app.models.models import db

@pytest.fixture(scope='module')
def app():
    """Create and configure a new app instance for each test module."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    """A test client for the app."""
    return app.test_client()
