# server/testing/conftest.py
import pytest
from app import app, db, Plant

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()  # Create database tables
        # Add a test plant
        plant = Plant(name='Live Oak', image='http://example.com/oak.jpg', price=250.0)
        db.session.add(plant)
        db.session.commit()  # Commit the test plant
        yield app.test_client()
        db.drop_all()  # Cleanup after tests


