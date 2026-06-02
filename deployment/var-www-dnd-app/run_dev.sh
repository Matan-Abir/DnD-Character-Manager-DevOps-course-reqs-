#!/bin/bash
# D&D Character Manager - Unix Development Server
# Run this to start the application in development mode

cd "$(dirname "$0")"

echo "Installing dependencies..."
python3 -m pip install -q flask werkzeug

echo ""
echo "Starting D&D Character Manager..."
echo ""
echo "Access the application at: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
