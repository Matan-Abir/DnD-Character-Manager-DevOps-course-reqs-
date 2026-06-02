# D&D Character Manager - Web Application

A modern web-based character management system for Dungeons & Dragons 5E, designed for easy Apache deployment.

## Features

- ⚔️ Create, edit, and delete D&D 5E characters
- 📊 View ability scores with automatic modifier calculation
- 🎲 Dice rolling (d6)
- 📦 Inventory management
- 🔍 Search and filter characters by name, race, or class
- 💾 Persistent SQLite database
- 🎨 Modern dark theme responsive UI
- 📱 Mobile-friendly design

## Quick Start (Development)

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py
```

The application will be available at `http://localhost:5000`

## Apache Deployment (Production)

### Prerequisites
- Apache 2.4+
- mod_wsgi
- Python 3.8+ with dev headers

### Installation

1. **Install mod_wsgi:**
   ```bash
   pip install mod_wsgi
   # Or on your system: sudo apt-get install libapache2-mod-wsgi-py3
   ```

2. **Copy application files to Apache directory:**
   ```bash
   sudo cp -r /path/to/DnD-Character-Manager /var/www/dnd-app
   sudo chown -R www-data:www-data /var/www/dnd-app
   ```

3. **Create Apache configuration** (`/etc/apache2/sites-available/dnd-app.conf`):
   ```apache
   <VirtualHost *:80>
       ServerName yourdomain.com
       ServerAdmin admin@yourdomain.com

       # WSGI Configuration
       WSGIScriptAlias / /var/www/dnd-app/wsgi.py
       WSGIDaemonProcess dnd user=www-data group=www-data threads=5
       WSGIProcessGroup dnd

       # Directory permissions
       <Directory /var/www/dnd-app>
           Require all granted
       </Directory>

       # Static files (CSS, JS)
       Alias /static /var/www/dnd-app/
       <Directory /var/www/dnd-app>
           Require all granted
       </Directory>

       ErrorLog ${APACHE_LOG_DIR}/dnd-error.log
       CustomLog ${APACHE_LOG_DIR}/dnd-access.log combined
   </VirtualHost>
   ```

4. **Enable the site:**
   ```bash
   sudo a2enmod wsgi
   sudo a2ensite dnd-app
   sudo systemctl restart apache2
   ```

5. **Verify deployment:**
   Visit `http://yourdomain.com` in your browser

## Database

The application uses SQLite (`characters.db`) for persistent storage. The database is automatically initialized on first run.

**Database location:** Same directory as `app.py`

To reset the database, simply delete `characters.db` (it will be recreated on next run).

## API Endpoints

All endpoints return JSON responses.

### Characters
- `GET /api/characters` - Get all characters
- `POST /api/characters` - Create new character
- `GET /api/characters/<id>` - Get character by ID
- `PUT /api/characters/<id>` - Update character
- `DELETE /api/characters/<id>` - Delete character
- `GET /api/characters/search?q=keyword` - Search characters

### Utilities
- `GET /api/randomize-stats` - Get random ability scores
- `POST /api/roll-dice` - Roll a d6

## File Structure

```
├── app.py              # Flask application
├── wsgi.py             # WSGI entry point (for Apache)
├── database.py         # SQLite database functions
├── index.html          # Web UI template
├── style.css           # Styles
├── script.js           # Frontend logic
├── requirements.txt    # Python dependencies
├── characters.db       # SQLite database (auto-created)
└── README.md          # This file
```

## Troubleshooting

### Database file permission issues
```bash
sudo chown www-data:www-data /var/www/dnd-app/characters.db
sudo chmod 664 /var/www/dnd-app/characters.db
```

### Application won't start
- Check Apache error log: `sudo tail -f /var/apache2/error.log`
- Verify wsgi.py permissions
- Ensure Flask is installed for www-data user

### Static files not loading
- Verify Alias and Directory directives in Apache config
- Check file permissions on .css and .js files
- Ensure static files are in the correct directory

## Development Notes

- The application stores characters in memory during development. Use `dummy_data_main_loop()` to load sample data.
- Search functionality filters by name, race, and class.
- Ability scores use standard D&D 5E ranges (3-18 recommended, but 1-20 allowed).
- Stats modifiers are automatically calculated using the formula: (score - 10) / 2

## License

This is a course project for the Technion DevOps program.
