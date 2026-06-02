@echo off
REM D&D Character Manager - Windows Development Server
REM Run this to start the application in development mode

cd /d "%~dp0"

echo Installing dependencies...
python -m pip install -q flask werkzeug

echo.
echo Starting D&D Character Manager...
echo.
echo Access the application at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
