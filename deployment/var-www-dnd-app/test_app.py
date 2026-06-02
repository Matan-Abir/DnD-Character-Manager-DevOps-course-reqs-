#!/usr/bin/env python3
"""
Simple test script to verify the D&D Character Manager application works correctly.
Run this to test all core functionality.
"""

import sys
import os
import json
import sqlite3

def test_database():
    """Test database initialization and operations"""
    print("Testing database...")
    
    # Import database module
    sys.path.insert(0, os.path.dirname(__file__))
    import database as db
    
    # Initialize
    if os.path.exists('characters.db'):
        os.remove('characters.db')
    
    db.init_db()
    if not os.path.exists('characters.db'):
        print("  ✗ Database file not created")
        return False
    
    # Test add
    char_id = db.add_character(
        "Aragorn", 20, "Human", "Ranger",
        {'str': 18, 'dex': 16, 'con': 16, 'int': 14, 'wis': 15, 'cha': 17},
        ["Anduril", "Ranger's Cloak"]
    )
    
    if char_id is None:
        print("  ✗ Failed to add character")
        return False
    
    # Test retrieve
    chars = db.get_all_characters()
    if len(chars) != 1:
        print("  ✗ Failed to retrieve characters")
        return False
    
    char = chars[0]
    if char['name'] != "Aragorn" or char['level'] != 20:
        print("  ✗ Character data mismatch")
        return False
    
    # Test search
    results = db.search_characters("Ranger")
    if len(results) != 1:
        print("  ✗ Search function failed")
        return False
    
    # Test update
    db.update_character(char_id, "Strider", 20, "Human", "Ranger",
        {'str': 18, 'dex': 16, 'con': 16, 'int': 14, 'wis': 15, 'cha': 17},
        ["Anduril", "Ranger's Cloak", "Arkenstone"])
    
    updated = db.get_character(char_id)
    if updated['name'] != "Strider":
        print("  ✗ Update failed")
        return False
    
    if len(updated['inventory']) != 3:
        print("  ✗ Inventory not updated")
        return False
    
    # Test delete
    db.delete_character(char_id)
    remaining = db.get_all_characters()
    if len(remaining) != 0:
        print("  ✗ Delete failed")
        return False
    
    print("  ✓ Database tests passed")
    return True

def test_flask_app():
    """Test Flask application structure"""
    print("\nTesting Flask application...")
    
    try:
        import app
        
        # Check routes exist
        routes = [str(rule) for rule in app.app.url_map.iter_rules()]
        required = ['/', '/api/characters', '/static/<path:filename>']
        
        for route in required:
            if not any(route in str(r) for r in routes):
                print(f"  ✗ Missing route: {route}")
                return False
        
        # Test with Flask test client
        app.app.config['TESTING'] = True
        client = app.app.test_client()
        
        # Test index
        response = client.get('/')
        if response.status_code != 200:
            print(f"  ✗ Index route failed: {response.status_code}")
            return False
        
        # Test API
        response = client.get('/api/characters')
        if response.status_code != 200:
            print(f"  ✗ API route failed: {response.status_code}")
            return False
        
        data = json.loads(response.data)
        if not isinstance(data, list):
            print("  ✗ API response format incorrect")
            return False
        
        print("  ✓ Flask app tests passed")
        return True
        
    except Exception as e:
        print(f"  ✗ Flask test failed: {e}")
        return False

def test_static_files():
    """Test static files exist"""
    print("\nTesting static files...")
    
    files = {
        'index.html': 'text/html',
        'style.css': 'text/css',
        'script.js': 'application/javascript'
    }
    
    for filename, ftype in files.items():
        if not os.path.exists(filename):
            print(f"  ✗ Missing file: {filename}")
            return False
        
        with open(filename, 'r') as f:
            content = f.read()
            if len(content) < 100:
                print(f"  ✗ File too small: {filename}")
                return False
    
    print("  ✓ Static files present")
    return True

def test_config_files():
    """Test configuration files"""
    print("\nTesting configuration files...")
    
    files = ['requirements.txt', 'wsgi.py', 'DEPLOYMENT.md']
    
    for filename in files:
        if not os.path.exists(filename):
            print(f"  ✗ Missing file: {filename}")
            return False
    
    # Check requirements
    with open('requirements.txt', 'r') as f:
        reqs = f.read()
        if 'flask' not in reqs.lower():
            print("  ✗ Flask not in requirements.txt")
            return False
    
    print("  ✓ Configuration files present")
    return True

def main():
    print("=" * 60)
    print("D&D Character Manager - Application Tests")
    print("=" * 60)
    
    tests = [
        test_static_files,
        test_config_files,
        test_database,
        test_flask_app,
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"  ✗ Test error: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    
    if all(results):
        print(f"✓ All {total} tests passed!")
        print("\nApplication is ready to deploy.")
        print("Start with: python app.py (for development)")
        return 0
    else:
        print(f"✗ {total - passed} of {total} tests failed")
        return 1

if __name__ == '__main__':
    sys.exit(main())
