from flask import request
from flask_restx import Resource, fields
from app.models import Item, db

def register_routes(api):
    item_ns = api.namespace('items', description='Item operations')

    # Register the model with the namespace
    item_model = item_ns.model('Item', {
        'id': fields.Integer(readOnly=True, description='The unique identifier of an item'),
        'name': fields.String(required=True, description='The name of the item'),
        'description': fields.String(description='The description of the item')
    })

    @item_ns.route('/')
    class ItemList(Resource):
        @item_ns.marshal_list_with(item_model)
        def get(self):
            """Get all items"""
            items = Item.query.all()
            return items

        @item_ns.expect(item_model, validate=True)
        @item_ns.marshal_with(item_model, code=201)
        def post(self):
            """Create a new item"""
            data = request.json
            new_item = Item(name=data['name'], description=data.get('description'))
            db.session.add(new_item)
            db.session.commit()
            return new_item, 201

    @item_ns.route('/<int:item_id>')
    @item_ns.param('item_id', 'The item identifier')
    class ItemResource(Resource):
        @item_ns.marshal_with(item_model)
        def get(self, item_id):
            """Get a single item by ID"""
            item = Item.query.get_or_404(item_id)
            return item

        @item_ns.expect(item_model, validate=True)
        @item_ns.marshal_with(item_model)
        def put(self, item_id):
            """Update an item by ID"""
            item = Item.query.get_or_404(item_id)
            data = request.json
            item.name = data['name']
            item.description = data.get('description')
            db.session.commit()
            return item

        def delete(self, item_id):
            """Delete an item by ID"""
            item = Item.query.get_or_404(item_id)
            db.session.delete(item)
            db.session.commit()
            return '', 204