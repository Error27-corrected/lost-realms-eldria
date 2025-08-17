# Contributing to The Lost Realms of Eldria

Thank you for your interest in contributing to The Lost Realms of Eldria! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Bugs
- Use the [GitHub Issues](https://github.com/Error27-corrected/lost-realms-eldria/issues) page
- Include a clear description of the bug
- Provide steps to reproduce the issue
- Mention your Python version and operating system

### Suggesting Features
- Open a new issue with the "enhancement" label
- Describe the feature and why it would be useful
- Consider how it fits into the game's design philosophy

### Code Contributions
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**
4. **Test your changes**: Run `python test_game.py`
5. **Commit your changes**: `git commit -m 'Add your feature description'`
6. **Push to your fork**: `git push origin feature/your-feature-name`
7. **Create a Pull Request**

## 🎮 Game Design Guidelines

### Story and Narrative
- Maintain the fantasy/adventure theme
- Keep descriptions immersive and atmospheric
- Ensure choices have meaningful consequences
- Balance risk vs. reward in decision-making

### Game Mechanics
- Keep the interface simple and intuitive
- Maintain game balance
- Ensure all paths are viable
- Add replayability through different choices

### Code Quality
- Follow Python PEP 8 style guidelines
- Add docstrings to new functions
- Include type hints where appropriate
- Write tests for new features

## 🛠️ Development Setup

### Prerequisites
- Python 3.6 or higher
- Git

### Local Development
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Error27-corrected/lost-realms-eldria.git
   cd lost-realms-eldria
   ```

2. **Run the game:**
   ```bash
   python adventure_game.py
   ```

3. **Run tests:**
   ```bash
   python test_game.py
   ```

## 📁 Project Structure

```
lost-realms-eldria/
├── adventure_game.py      # Main game file
├── test_game.py          # Test suite
├── README.md             # Project documentation
├── WALKTHROUGH.md        # Game strategy guide
├── CONTRIBUTING.md       # This file
├── LICENSE               # MIT License
├── requirements.txt      # Python dependencies
├── setup.py             # Package setup
├── run_game.bat         # Windows launcher
└── .gitignore           # Git ignore rules
```

## 🎯 Areas for Contribution

### High Priority
- **Bug fixes**: Any issues that break gameplay
- **Documentation**: Improving guides and README
- **Testing**: Adding more comprehensive tests
- **Accessibility**: Making the game more accessible

### Medium Priority
- **New locations**: Adding more areas to explore
- **Additional quests**: Creating new side quests
- **Character development**: Expanding the reputation system
- **Save/load functionality**: Persistent game state

### Low Priority
- **UI improvements**: Better text formatting
- **Sound effects**: Audio feedback (if possible)
- **Modding support**: Tools for custom content
- **Multiplayer features**: Shared world exploration

## 📝 Code Style

### Python Style
- Use 4 spaces for indentation
- Follow PEP 8 naming conventions
- Keep functions under 50 lines when possible
- Add comments for complex logic

### Documentation
- Use docstrings for all functions and classes
- Include examples in docstrings
- Keep README up to date
- Document any new game mechanics

### Testing
- Write tests for new features
- Ensure existing tests pass
- Test edge cases and error conditions
- Include integration tests for game flow

## 🚀 Release Process

### Version Numbers
We use [Semantic Versioning](https://semver.org/):
- **Major version**: Breaking changes
- **Minor version**: New features (backward compatible)
- **Patch version**: Bug fixes (backward compatible)

### Release Checklist
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Version number is updated
- [ ] Changelog is updated
- [ ] Release notes are written

## 🏆 Recognition

Contributors will be recognized in:
- The project README
- Release notes
- GitHub contributors page
- Game credits (if applicable)

## 📞 Getting Help

- **Discussions**: Use GitHub Discussions for questions
- **Issues**: Report bugs and request features
- **Pull Requests**: Submit code changes
- **Wiki**: Check the project wiki for additional resources

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to The Lost Realms of Eldria! Your help makes the game better for everyone. 🌟
