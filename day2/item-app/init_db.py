from app import db, Item

# Initialize the database
db.create_all()

# Add sample data
sample_item = Item(name="Sample Item", description="This is a sample item.")
db.session.add(sample_item)
db.session.commit()

print("Database initialized with sample data.")