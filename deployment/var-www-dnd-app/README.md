# DnD-Character-Manager-DevOps-course-reqs-

A modern web application for managing Dungeons & Dragons 5E characters. Originally a CLI tool, now fully converted to a Flask web application with a responsive GUI ready for Apache deployment.

## 🎮 Features

- **Create & Manage Characters** - Full CRUD operations for D&D 5E characters
- **Ability Scores** - Input or randomize stats with automatic modifier calculation
- **Inventory Management** - Add/remove items from character inventories  
- **Search & Filter** - Find characters by name, race, or class
- **Dice Roller** - Roll a d6 anytime during gameplay
- **Persistent Storage** - SQLite database for permanent character storage
- **Modern UI** - Dark-themed, responsive design works on desktop and mobile
- **Apache Ready** - WSGI-compatible for production Apache hosting

## 🚀 Quick Start (Development)

### Prerequisites
- Python 3.8+
- pip

### Running Locally

**Windows:**
```bash
run_dev.bat
```

**Linux/Mac:**
```bash
chmod +x run_dev.sh
./run_dev.sh
```

**Manual:**
```bash
pip install -r requirements.txt
python app.py
```

The application will start on `http://localhost:5000`

## 🌐 Apache Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete Apache setup instructions including:
- mod_wsgi configuration
- Virtual host setup
- Static file serving
- Database permissions
- SSL/HTTPS setup

## 📁 Project Structure

```
├── app.py               # Flask web application (main entry point)
├── wsgi.py              # WSGI entry for Apache mod_wsgi
├── database.py          # SQLite database layer
├── index.html           # HTML template
├── style.css            # Modern CSS styling (dark theme)
├── script.js            # Frontend logic (vanilla JS)
├── requirements.txt     # Python dependencies
├── run_dev.bat          # Windows development starter
├── run_dev.sh           # Unix development starter
├── DEPLOYMENT.md        # Apache deployment guide
├── characters.db        # SQLite database (auto-created)
└── README.md            # This file
```

## 🛠️ API Reference

All endpoints return JSON responses.

### Characters
- `GET /api/characters` - List all characters (sorted by level)
- `POST /api/characters` - Create a new character
- `GET /api/characters/<id>` - Get character details
- `PUT /api/characters/<id>` - Update character
- `DELETE /api/characters/<id>` - Delete character
- `GET /api/characters/search?q=keyword` - Search by name/race/class

### Utilities
- `GET /api/randomize-stats` - Generate random ability scores (3d6)
- `POST /api/roll-dice` - Roll d6 (returns 1-6)

## 📊 Character Data Model

Each character stores:
- **Name** - Character name
- **Level** - Experience level (1-20)
- **Race** - Character race (e.g., Human, Elf, Dwarf)
- **Class** - Character class (e.g., Wizard, Rogue, Cleric)
- **Stats** - Six ability scores (STR, DEX, CON, INT, WIS, CHA)
  - Range: 1-20 (though 3-18 is typical)
  - Modifiers calculated as: `(score - 10) / 2`
- **Inventory** - List of items/equipment

## 🔄 Migrating from CLI Version

The original CLI functionality is preserved in the core logic, but the I/O layer has been completely rewritten for the web:

- **Old CLI Menus** → **Modern Web UI with modals**
- **Console Output** → **JSON API endpoints**  
- **In-Memory Characters** → **SQLite persistence**
- **Text-Based Navigation** → **Responsive point-and-click interface**

The core business logic (stat calculations, validation, etc.) remains unchanged.

## 🎲 Character Creation Examples

The web UI guides you through character creation with:
- Manual stat entry with validation (1-20)
- Automatic randomization button (3d6 per stat)
- Real-time modifier calculation display
- Inventory item management
- All changes saved to persistent database

## 📝 Development Notes

- Database file: `characters.db` (auto-created on first run)
- To reset data, delete `characters.db` and refresh browser
- All stats stored with 6-stat D&D ability score format
- Search is case-insensitive partial matching
- Modifiers display in parentheses next to stats

## ✅ Requirements Met

✓ Web-based GUI (HTML/CSS/JavaScript)  
✓ Modern but simple interface  
✓ Apache hostable (WSGI compatible)  
✓ Fast deployment (production-ready)  
✓ Persistent data storage  
✓ All original features preserved  

## 🤝 Contributing

Originally created for the Technion DevOps course. Feel free to extend with:
- Spell management
- Multi-player campaign features
- Character sheets export (PDF)
- Dice pool mechanics
- Database backups

## 📄 License

Technion DevOps Course Project

