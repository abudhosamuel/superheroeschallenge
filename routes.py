from flask import Blueprint, request, jsonify
from models import db, Hero, Power, HeroPower

api = Blueprint('api', __name__)

# GET /heroes
@api.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heroes])

# GET /heroes/:id
@api.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'error': 'Hero not found'}), 404
    hero_powers = [{
        'hero_id': hp.hero_id,
        'id': hp.id,
        'power': {'description': hp.power.description, 'id': hp.power.id, 'name': hp.power.name},
        'power_id': hp.power_id,
        'strength': hp.strength
    } for hp in hero.hero_powers]
    return jsonify({
        'id': hero.id,
        'name': hero.name,
        'super_name': hero.super_name,
        'hero_powers': hero_powers
    })

# GET /powers
@api.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{'id': power.id, 'name': power.name, 'description': power.description} for power in powers])

# GET /powers/:id
@api.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    return jsonify({'id': power.id, 'name': power.name, 'description': power.description})

# PATCH /powers/:id
@api.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    # Fetch the Power instance by its ID
    power = Power.query.get(id)
    
    # If the power does not exist, return an error message
    if not power:
        return jsonify({"error": "Power not found"}), 404

    # Get the request data
    data = request.json

    # Validate the description
    if 'description' not in data or len(data['description']) < 20:
        return jsonify({"errors": ["Validation errors: Description must be at least 20 characters long."]}), 400

    # Update the power's description
    power.description = data['description']
    
    # Commit the changes to the database
    db.session.commit()

    # Return the updated power details
    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    })


# POST /hero_powers
@api.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    hero = Hero.query.get(data['hero_id'])
    power = Power.query.get(data['power_id'])
    
    if not hero or not power or data['strength'] not in ['Strong', 'Weak', 'Average']:
        return jsonify({'errors': ['Validation errors']}), 400

    hero_power = HeroPower(strength=data['strength'], hero_id=hero.id, power_id=power.id)
    db.session.add(hero_power)
    db.session.commit()

    return jsonify({
        'id': hero_power.id,
        'hero_id': hero.id,
        'power_id': power.id,
        'strength': hero_power.strength,
        'hero': {'id': hero.id, 'name': hero.name, 'super_name': hero.super_name},
        'power': {'id': power.id, 'name': power.name, 'description': power.description}
    })
