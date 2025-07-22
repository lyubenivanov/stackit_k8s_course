from flask import Flask
from flask_restx import Api
from app.models import Item
from app.db import db

api = Api(title="Item Management API", description="A simple Item management API", version="1.0")

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    api.init_app(app)

    from app.routes import register_routes
    register_routes(api)

    with app.app_context():
        # Initialize the database
        db.create_all()

        # Add sample data
        if not Item.query.first():  # Avoid duplicate sample data
            sample_item = Item(name="Sample Item", description="This is a sample item.")
            db.session.add(sample_item)
            db.session.commit()

    return app