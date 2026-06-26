print("LOADED APP.PY FROM:", __file__)

from flask import Flask, render_template, request, jsonify, send_from_directory
import database as db
import json
import random
import math
import os
import sqlite3

app = Flask(__name__)
app.config['STATIC_FOLDER'] = '.'

if os.environ.get("WERKZEUG_RUN_MAIN") == "true" or True:
    db.init_db()


@app.route("/__debug/routes")
def routes():
    return "\n".join(str(r) for r in app.url_map.iter_rules())


# Validation functions
def validate_stat(value):
    """Validate that a stat is between 1 and 20"""
    try:
        stat = int(value)
        return 1 <= stat <= 20
    except:
        return False

def calculate_modifier(stat):
    """Calculate D&D modifier from ability score"""
    return math.floor((stat - 10) / 2)

def randomize_stats():
    """Generate random ability scores using 3d6"""
    return {
        'str': sum(random.randint(1, 6) for _ in range(3)),
        'dex': sum(random.randint(1, 6) for _ in range(3)),
        'con': sum(random.randint(1, 6) for _ in range(3)),
        'int': sum(random.randint(1, 6) for _ in range(3)),
        'wis': sum(random.randint(1, 6) for _ in range(3)),
        'cha': sum(random.randint(1, 6) for _ in range(3))
    }

# Routes
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/script.js')
def serve_js():
    return send_from_directory('.', 'script.js')

@app.route('/style.css')
def serve_css():
    return send_from_directory('.', 'style.css')

@app.route('/api/characters', methods=['GET'])
def get_characters():
    """Get all characters"""
    characters = db.get_all_characters()
    return jsonify(characters)

@app.route('/api/characters', methods=['POST'])
def create_character():
    """Create a new character"""
    data = request.json
    
    # Validate input
    if not data.get('name') or not data.get('race') or not data.get('class'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        level = int(data.get('level', 1))
        if level < 1:
            return jsonify({'error': 'Level must be 1 or higher'}), 400
    except:
        return jsonify({'error': 'Invalid level'}), 400
    
    stats = data.get('stats')
    if stats.get('randomize'):
        stats = randomize_stats()
    else:
        # Validate manual stats
        for stat_name in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
            if not validate_stat(stats.get(stat_name)):
                return jsonify({'error': f'Invalid {stat_name} value'}), 400
        # Convert to int
        for stat_name in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
            stats[stat_name] = int(stats[stat_name])
    
    inventory = data.get('inventory', [])
    if not isinstance(inventory, list):
        inventory = [inventory] if inventory else []
    
    char_id = db.add_character(data['name'], level, data['race'], data['class'], stats, inventory)
    character = db.get_character(char_id)
    return jsonify(character), 201

@app.route('/api/characters/<int:char_id>', methods=['GET'])
def get_character(char_id):
    """Get a single character"""
    character = db.get_character(char_id)
    if not character:
        return jsonify({'error': 'Character not found'}), 404
    return jsonify(character)

@app.route('/api/characters/<int:char_id>', methods=['PUT'])
def update_character(char_id):
    """Update a character"""
    character = db.get_character(char_id)
    if not character:
        return jsonify({'error': 'Character not found'}), 404
    
    data = request.json
    name = data.get('name', character['name'])
    level = data.get('level', character['level'])
    race = data.get('race', character['race'])
    char_class = data.get('class', character['class'])
    stats = data.get('stats', character['stats'])
    inventory = data.get('inventory', character['inventory'])
    
    try:
        level = int(level)
        if level < 1:
            return jsonify({'error': 'Level must be 1 or higher'}), 400
    except:
        return jsonify({'error': 'Invalid level'}), 400
    
    db.update_character(char_id, name, level, race, char_class, stats, inventory)
    updated = db.get_character(char_id)
    return jsonify(updated)

@app.route('/api/characters/<int:char_id>', methods=['DELETE'])
def delete_character(char_id):
    """Delete a character"""
    character = db.get_character(char_id)
    if not character:
        return jsonify({'error': 'Character not found'}), 404
    
    db.delete_character(char_id)
    return '', 204

@app.route('/api/characters/search', methods=['GET'])
def search_characters():
    """Search characters by keyword"""
    keyword = request.args.get('q', '')
    if not keyword:
        return jsonify([])
    results = db.search_characters(keyword)
    return jsonify(results)

@app.route('/api/roll-dice', methods=['POST'])
def roll_dice():
    """Roll a d6"""
    roll = random.randint(1, 6)
    return jsonify({'result': roll})

@app.route('/api/randomize-stats', methods=['GET'])
def get_randomize_stats():
    """Generate random ability scores"""
    stats = randomize_stats()
    return jsonify(stats)

@app.route('/api/load-dummy', methods=['POST'])
def load_dummy_data():
    """Load dummy data into the database"""
    # Clear existing characters first
    conn = sqlite3.connect(db.DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM characters')
    conn.commit()
    conn.close()
    
    dummy_data = [
        {
            'name': 'Matan',
            'level': 6,
            'race': 'Human',
            'class': 'Warlock',
            'stats': {'str': 8, 'dex': 9, 'con': 9, 'int': 13, 'wis': 15, 'cha': 18},
            'inventory': ['Shrunken Head', 'Component Pouch']
        },
        {
            'name': 'Kenji',
            'level': 20,
            'race': 'Wood-Elf',
            'class': 'Samurai',
            'stats': {'str': 20, 'dex': 23, 'con': 16, 'int': 12, 'wis': 15, 'cha': 11},
            'inventory': ['Katana', 'Kabuto', 'Omamori Charm', 'Book of the Five Rings']
        },
        {
            'name': 'Steve Jobs',
            'level': 14,
            'race': 'Zombie',
            'class': 'Programmer',
            'stats': {'str': 11, 'dex': 10, 'con': 6, 'int': 18, 'wis': 15, 'cha': 20},
            'inventory': ['Gray Turtleneck', 'iPhone 4']
        }
    ]
    
    for char in dummy_data:
        db.add_character(char['name'], char['level'], char['race'], char['class'], 
                        char['stats'], char['inventory'])
    
    return jsonify({'success': True, 'message': 'Dummy data loaded'}), 201

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
