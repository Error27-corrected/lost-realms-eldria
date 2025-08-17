# The Lost Realms of Eldria - Text-Based Adventure Game

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Game](https://github.com/Error27-corrected/lost-realms-eldria)](https://github.com/Error27-corrected/lost-realms-eldria)

## 🎮 Game Overview

**The Lost Realms of Eldria** is a captivating text-based adventure game built in Python. Players embark on a journey through the mystical realm of Eldria, making crucial decisions that shape their destiny and determine the outcome of their adventure.

## 🚀 Quick Start

### Option 1: Play Online (Recommended)
1. **Clone this repository:**
   ```bash
   git clone https://github.com/Error27-corrected/lost-realms-eldria.git
   cd lost-realms-eldria
   ```

2. **Run the game:**
   ```bash
   python adventure_game.py
   ```

### Option 2: Download and Play
1. Click the green "Code" button above
2. Select "Download ZIP"
3. Extract the ZIP file
4. Open terminal/command prompt in the extracted folder
5. Run: `python adventure_game.py`

### Option 3: One-Click Run (Windows)
- Double-click `run_game.bat` to start the game automatically

## 🌟 Features

### Core Game Engine
- **Modular Design**: Clean, object-oriented architecture with separate game state management
- **Scene System**: Dynamic location-based storytelling with smooth transitions
- **User Input Validation**: Robust input handling with error prevention
- **Status Tracking**: Real-time display of health, gold, reputation, and inventory

### Engaging Narrative
- **Rich Storytelling**: Immersive descriptions with atmospheric text effects
- **Multiple Locations**: 9 unique locations to explore
- **Character Development**: Player reputation system affecting game outcomes
- **Lore Integration**: Deep world-building with historical context

### Decision-Making System
- **Three Major Decision Points**: Each with significant consequences
- **Branching Storylines**: Multiple paths based on player choices
- **Consequence Tracking**: Actions affect reputation, health, and available options
- **Quest System**: Multiple side quests with different rewards

### User Experience
- **Smooth Interface**: Clear prompts and intuitive navigation
- **Visual Feedback**: Emoji indicators and status displays
- **Error Handling**: Graceful handling of invalid inputs and interruptions
- **Inventory Management**: Easy item tracking and usage

## 🎯 Major Decision Points

### Decision Point #1: The Mysterious Stranger (Tavern)
- **Location**: Golden Ale Tavern
- **Choice**: Accept or decline a dangerous treasure hunt
- **Consequences**: 
  - Accept: Gain ancient map, lose 20 gold, unlock special chest interaction
  - Decline: Gain reputation, maintain safety
  - Ask for details: Learn more about the risks

### Decision Point #2: The Forest Crossroads
- **Location**: Forest Path
- **Choice**: Choose between three different paths
- **Consequences**:
  - Well-traveled path: Safe journey to Stonebridge, complete delivery quest
  - Overgrown trail: Discover hidden clearing with rare herbs
  - Water path: Find waterfall cave with ancient chest

### Decision Point #3: The Ancient Chest
- **Location**: Waterfall Cave
- **Choice**: Risk opening trapped chest or explore deeper
- **Consequences**:
  - Open chest: Success with map, failure without (health loss)
  - Explore deeper: Discover ancient library with valuable knowledge
  - Leave: Safe but miss potential rewards

## 🗺️ Game Locations

1. **Moonhaven Village** - Starting location with multiple options
2. **Golden Ale Tavern** - First major decision point
3. **Village Notice Board** - Quest opportunities
4. **Village Elder's Cottage** - Lore and wisdom
5. **Forest Path** - Second major decision point
6. **Inventory** - Item management
7. **Stonebridge Village** - Market and rest opportunities
8. **Hidden Clearing** - Magical altar and rare herbs
9. **Waterfall Cave** - Third major decision point

## 🎒 Game Mechanics

### Player Stats
- **Health**: 0-100 (affects survival and interactions)
- **Gold**: Currency for purchases and quests
- **Reputation**: Affects NPC reactions and quest availability
- **Inventory**: Items that unlock special interactions

### Quest System
- **Wolf Hunting**: Combat-focused quest (30 gold reward)
- **Herb Gathering**: Exploration quest (15 gold + healing potion)
- **Package Delivery**: Travel quest (25 gold reward)

### Item System
- **Ancient Map**: Unlocks special chest interaction
- **Healing Potions**: Restore health
- **Rare Herbs**: Valuable crafting materials
- **Ancient Artifacts**: High-value treasures
- **Knowledge Items**: Provide lore and reputation

## 🚀 How to Play

### Installation
1. Ensure Python 3.6+ is installed
2. Download the `adventure_game.py` file
3. Run the game using: `python adventure_game.py`

### Controls
- **Number Input**: Choose options by entering the corresponding number
- **Enter Key**: Confirm selections and progress through text
- **Ctrl+C**: Exit the game at any time

### Gameplay Tips
- **Explore Thoroughly**: Visit all locations to discover hidden content
- **Manage Resources**: Balance health, gold, and reputation
- **Read Carefully**: Pay attention to descriptions for clues
- **Make Strategic Choices**: Consider long-term consequences
- **Complete Quests**: Earn rewards and unlock new content

## 🏗️ Technical Architecture

### Core Classes

#### GameState
- Manages player statistics and inventory
- Handles item addition/removal
- Tracks quest completion and game flags

#### GameEngine
- Controls game flow and scene transitions
- Handles user input validation
- Manages text display and screen clearing

### Key Methods
- `add_location()`: Register new game scenes
- `get_user_input()`: Validate and process user choices
- `display_status()`: Show current player stats
- `type_text()`: Create typing effect for immersive experience

### Design Patterns
- **State Management**: Centralized game state tracking
- **Scene System**: Modular location-based storytelling
- **Command Pattern**: Input validation and processing
- **Observer Pattern**: Status updates and notifications

## 🎨 Game Design Principles

### Narrative Design
- **Immersive Descriptions**: Rich, atmospheric text
- **Character Agency**: Meaningful choices with real consequences
- **World Building**: Consistent lore and setting
- **Pacing**: Balanced exploration and decision-making

### User Experience
- **Clear Navigation**: Intuitive menu systems
- **Visual Feedback**: Status indicators and progress tracking
- **Error Prevention**: Input validation and helpful prompts
- **Accessibility**: Simple controls and clear text

### Game Balance
- **Risk vs. Reward**: Meaningful trade-offs in decisions
- **Resource Management**: Strategic use of health, gold, and reputation
- **Multiple Paths**: Different valid strategies for success
- **Replayability**: Different outcomes based on choices

## 🔧 Customization and Extension

### Adding New Locations
1. Define a new scene function
2. Register it with `game.add_location()`
3. Add navigation options from existing locations

### Creating New Quests
1. Add quest flags to game state
2. Create quest-specific items and rewards
3. Implement quest completion logic

### Expanding the Story
1. Add new decision points with consequences
2. Create additional NPCs and dialogue
3. Implement new game mechanics

## 🐛 Troubleshooting

### Common Issues
- **Input Errors**: Ensure you're entering valid numbers/options
- **Screen Display**: Game uses console output, ensure terminal supports emoji
- **Python Version**: Requires Python 3.6+ for f-string support

### Performance
- **Text Speed**: Adjust `delay` parameter in `type_text()` method
- **Screen Clearing**: Modify `clear_screen()` for different terminals

## 📝 Future Enhancements

### Potential Features
- **Save/Load System**: Persistent game state
- **Sound Effects**: Audio feedback for actions
- **Character Classes**: Different starting abilities
- **Combat System**: Turn-based encounters
- **Crafting System**: Item creation and modification
- **Multiplayer Elements**: Shared world exploration

### Technical Improvements
- **Database Integration**: Persistent quest and item data
- **Web Interface**: Browser-based gameplay
- **Mobile Support**: Touch-friendly controls
- **Modding Support**: User-created content

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### What we're looking for:
- 🐛 Bug fixes and improvements
- 🎮 New game features and content
- 📚 Documentation improvements
- 🎨 UI/UX enhancements
- 🧪 Testing and quality assurance

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic text-based adventure games
- Built with Python's standard library
- Created for educational purposes

## 📞 Support

- 📖 **Documentation**: Check [WALKTHROUGH.md](WALKTHROUGH.md) for detailed gameplay guide
- 🐛 **Issues**: Report bugs on [GitHub Issues](https://github.com/yourusername/lost-realms-eldria/issues)
- 💡 **Suggestions**: Share ideas for new features
- ⭐ **Star**: If you enjoy the game, please give it a star!

---

**Happy Adventuring in the Lost Realms of Eldria!** 🌟

---

<div align="center">
  <a href="https://github.com/Error27-corrected/lost-realms-eldria">
    <img src="https://img.shields.io/badge/GitHub-View%20on%20GitHub-blue?style=for-the-badge&logo=github" alt="View on GitHub">
  </a>
  <a href="https://github.com/Error27-corrected/lost-realms-eldria/issues">
    <img src="https://img.shields.io/badge/GitHub-Issues-red?style=for-the-badge&logo=github" alt="GitHub Issues">
  </a>
  <a href="https://github.com/Error27-corrected/lost-realms-eldria/stargazers">
    <img src="https://img.shields.io/badge/GitHub-Stars-yellow?style=for-the-badge&logo=github" alt="GitHub Stars">
  </a>
</div>
