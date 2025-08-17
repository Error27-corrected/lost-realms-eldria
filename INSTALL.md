# Installation Guide - The Lost Realms of Eldria

## 🐍 Python Installation

### Option 1: Download from Python.org (Recommended)
1. Visit [python.org](https://www.python.org/downloads/)
2. Download the latest Python version (3.8 or higher)
3. Run the installer
4. **Important**: Check "Add Python to PATH" during installation
5. Verify installation by opening Command Prompt and typing: `python --version`

### Option 2: Microsoft Store (Windows 10/11)
1. Open Microsoft Store
2. Search for "Python"
3. Install the latest version (3.8 or higher)
4. Verify installation by opening Command Prompt and typing: `python --version`

### Option 3: Using Chocolatey (Advanced Users)
1. Install Chocolatey first: [chocolatey.org](https://chocolatey.org/install)
2. Open PowerShell as Administrator
3. Run: `choco install python`

## 🎮 Running the Game

### Method 1: Command Prompt/PowerShell
1. Open Command Prompt or PowerShell
2. Navigate to the game directory:
   ```
   cd "C:\Users\radha\OneDrive\Desktop\sowmya"
   ```
3. Run the game:
   ```
   python adventure_game.py
   ```

### Method 2: Double-Click (Windows)
1. Right-click on `adventure_game.py`
2. Select "Open with" → "Python"

### Method 3: Using Python Launcher
1. Open Command Prompt
2. Navigate to game directory
3. Run: `py adventure_game.py`

## 🧪 Testing the Installation

### Quick Test
Run this command to test if Python is working:
```
python -c "print('Hello, Python is working!')"
```

### Game Test
Run the test script to verify the game components:
```
python test_game.py
```

## 🔧 Troubleshooting

### "Python is not recognized"
- Python is not in your PATH
- Solution: Reinstall Python and check "Add Python to PATH"
- Or add Python manually to PATH environment variable

### "Module not found" errors
- The game uses only Python standard library
- No additional packages needed
- Ensure you're using Python 3.6 or higher

### "Permission denied" errors
- Run Command Prompt as Administrator
- Or check file permissions

### Game doesn't start
- Ensure you're in the correct directory
- Check that `adventure_game.py` exists
- Try running with `py` instead of `python`

## 📁 File Structure

After installation, you should have these files:
```
sowmya/
├── adventure_game.py      # Main game file
├── test_game.py          # Test script
├── README.md             # Game documentation
├── WALKTHROUGH.md        # Strategy guide
├── requirements.txt      # Python requirements
└── INSTALL.md           # This file
```

## 🎯 Quick Start

1. **Install Python** (see above)
2. **Open Command Prompt**
3. **Navigate to game folder**:
   ```
   cd "C:\Users\radha\OneDrive\Desktop\sowmya"
   ```
4. **Run the game**:
   ```
   python adventure_game.py
   ```
5. **Enjoy your adventure!**

## 🆘 Getting Help

### Common Issues
- **Python not found**: Reinstall Python with PATH option
- **Game won't start**: Check file permissions and directory
- **Text display issues**: Ensure terminal supports Unicode/emoji

### Support
- Check the README.md for game documentation
- Review WALKTHROUGH.md for gameplay strategies
- Run test_game.py to verify installation

## 🎉 Success!

Once you see the game title "THE LOST REALMS OF ELDRIA" and can enter your character name, the installation is successful!

---

**Happy Gaming!** 🎮✨
