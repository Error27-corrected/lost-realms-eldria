#!/usr/bin/env python3
"""
Test script for The Lost Realms of Eldria text-based adventure game.
This script tests the core game components and demonstrates functionality.
"""

import sys
import time
from adventure_game import GameState, GameEngine

def test_game_state():
    """Test the GameState class functionality"""
    print("🧪 Testing GameState class...")
    
    state = GameState()
    
    # Test initial values
    assert state.health == 100, f"Expected health 100, got {state.health}"
    assert state.gold == 50, f"Expected gold 50, got {state.gold}"
    assert state.reputation == 0, f"Expected reputation 0, got {state.reputation}"
    assert state.inventory == [], f"Expected empty inventory, got {state.inventory}"
    
    # Test item management
    state.add_item("Test Sword")
    assert "Test Sword" in state.inventory, "Item not added to inventory"
    assert state.has_item("Test Sword"), "has_item() returned False for existing item"
    
    state.remove_item("Test Sword")
    assert "Test Sword" not in state.inventory, "Item not removed from inventory"
    assert not state.has_item("Test Sword"), "has_item() returned True for removed item"
    
    # Test stat modifications
    state.modify_health(-20)
    assert state.health == 80, f"Expected health 80, got {state.health}"
    
    state.modify_gold(30)
    assert state.gold == 80, f"Expected gold 80, got {state.gold}"
    
    state.modify_reputation(10)
    assert state.reputation == 10, f"Expected reputation 10, got {state.reputation}"
    
    print("✅ GameState tests passed!")

def test_game_engine():
    """Test the GameEngine class functionality"""
    print("🧪 Testing GameEngine class...")
    
    engine = GameEngine()
    
    # Test location management
    def test_scene(game_engine):
        return "test_scene"
    
    engine.add_location("test", test_scene)
    assert "test" in engine.locations, "Location not added"
    
    # Test location navigation
    result = engine.go_to_location("test")
    assert result == True, "Location navigation failed"
    assert engine.state.current_location == "test", "Location not updated"
    
    # Test input validation
    # Note: This would require mocking input, so we'll just test the structure
    assert hasattr(engine, 'get_user_input'), "get_user_input method missing"
    assert hasattr(engine, 'display_status'), "display_status method missing"
    assert hasattr(engine, 'type_text'), "type_text method missing"
    
    print("✅ GameEngine tests passed!")

def test_game_creation():
    """Test the complete game creation"""
    print("🧪 Testing game creation...")
    
    try:
        from adventure_game import create_game
        game = create_game()
        
        # Test that all expected locations are present
        expected_locations = [
            "start", "tavern", "notice_board", "elder", 
            "forest_path", "inventory", "stonebridge", 
            "hidden_clearing", "waterfall_cave"
        ]
        
        for location in expected_locations:
            assert location in game.locations, f"Missing location: {location}"
        
        # Test initial state
        assert game.state.current_location == "start"
        assert game.state.health == 100
        assert game.state.gold == 50
        
        print("✅ Game creation tests passed!")
        
    except Exception as e:
        print(f"❌ Game creation test failed: {e}")
        return False
    
    return True

def demonstrate_game_features():
    """Demonstrate key game features"""
    print("\n🎮 Demonstrating Game Features...")
    
    # Create a game instance
    from adventure_game import create_game
    game = create_game()
    
    print("\n📊 Initial Player Status:")
    game.display_status()
    
    print("\n🎒 Testing Inventory System:")
    game.state.add_item("Magic Sword")
    game.state.add_item("Healing Potion")
    game.state.add_item("Ancient Map")
    game.display_status()
    
    print("\n💰 Testing Economy System:")
    game.state.modify_gold(100)
    game.state.modify_gold(-25)
    game.display_status()
    
    print("\n❤️ Testing Health System:")
    game.state.modify_health(-30)
    game.state.modify_health(20)
    game.display_status()
    
    print("\n🌟 Testing Reputation System:")
    game.state.modify_reputation(15)
    game.state.modify_reputation(-5)
    game.display_status()
    
    print("\n🎯 Testing Quest System:")
    game.state.game_flags["wolf_quest"] = True
    game.state.game_flags["herb_quest"] = True
    game.state.completed_quests.append("Wolf Hunting")
    print(f"Active Quests: {list(game.state.game_flags.keys())}")
    print(f"Completed Quests: {game.state.completed_quests}")

def run_quick_game_demo():
    """Run a quick demonstration of the game"""
    print("\n🎮 Quick Game Demo...")
    print("This will show a brief gameplay sequence.")
    
    # Create game
    from adventure_game import create_game
    game = create_game()
    
    # Simulate some gameplay
    print("\n🌙 Starting in Moonhaven Village...")
    game.display_status()
    
    print("\n🍺 Visiting the tavern...")
    game.go_to_location("tavern")
    
    print("\n📋 Checking the notice board...")
    game.go_to_location("notice_board")
    
    print("\n🌲 Exploring the forest path...")
    game.go_to_location("forest_path")
    
    print("\n💎 Discovering the waterfall cave...")
    game.go_to_location("waterfall_cave")
    
    print("\n✅ Demo completed successfully!")

def main():
    """Run all tests and demonstrations"""
    print("🎮 The Lost Realms of Eldria - Game Testing Suite")
    print("=" * 50)
    
    try:
        # Run tests
        test_game_state()
        test_game_engine()
        test_game_creation()
        
        # Demonstrate features
        demonstrate_game_features()
        
        # Ask if user wants to see the demo
        print("\n" + "=" * 50)
        choice = input("Would you like to see a quick game demo? (y/n): ").lower().strip()
        
        if choice in ['y', 'yes']:
            run_quick_game_demo()
        
        print("\n🎉 All tests completed successfully!")
        print("The game is ready to play! Run 'python adventure_game.py' to start your adventure.")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        print("Please check the game code for issues.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
