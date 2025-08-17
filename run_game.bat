@echo off
echo ========================================
echo    The Lost Realms of Eldria
echo    Text-Based Adventure Game
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    echo See INSTALL.md for detailed instructions
    echo.
    pause
    exit /b 1
)

echo Python found! Starting the game...
echo.
echo Press Ctrl+C at any time to exit the game
echo.

REM Run the game
python adventure_game.py

echo.
echo Thanks for playing The Lost Realms of Eldria!
pause
