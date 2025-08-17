import time
import random
import sys
from typing import Dict, List, Optional, Callable

class GameState:
    """Manages the current state of the game"""
    def __init__(self):
        self.current_location = "start"
        self.inventory = []
        self.health = 100
        self.gold = 50
        self.reputation = 0
        self.completed_quests = []
        self.game_flags = {}
        
    def add_item(self, item: str):
        """Add an item to player's inventory"""
        if item not in self.inventory:
            self.inventory.append(item)
            print(f"✨ You acquired: {item}")
    
    def remove_item(self, item: str):
        """Remove an item from player's inventory"""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def has_item(self, item: str) -> bool:
        """Check if player has a specific item"""
        return item in self.inventory
    
    def modify_health(self, amount: int):
        """Modify player's health"""
        self.health = max(0, min(100, self.health + amount))
        if amount > 0:
            print(f"❤️  Health restored by {amount}")
        elif amount < 0:
            print(f"💔 Health reduced by {abs(amount)}")
    
    def modify_gold(self, amount: int):
        """Modify player's gold"""
        self.gold = max(0, self.gold + amount)
        if amount > 0:
            print(f"💰 Gained {amount} gold")
        elif amount < 0:
            print(f"💸 Lost {abs(amount)} gold")
    
    def modify_reputation(self, amount: int):
        """Modify player's reputation"""
        self.reputation += amount
        if amount > 0:
            print(f"🌟 Reputation increased by {amount}")
        elif amount < 0:
            print(f"👎 Reputation decreased by {abs(amount)}")

class GameEngine:
    """Main game engine that handles story progression and user interactions"""
    
    def __init__(self):
        self.state = GameState()
        self.locations = {}
        self.current_scene = None
        self.game_running = True
        
    def add_location(self, location_id: str, scene_func: Callable):
        """Add a location/scene to the game"""
        self.locations[location_id] = scene_func
    
    def go_to_location(self, location_id: str):
        """Move to a specific location"""
        if location_id in self.locations:
            self.state.current_location = location_id
            self.current_scene = self.locations[location_id]
            return True
        return False
    
    def get_user_input(self, prompt: str, valid_options: List[str] = None) -> str:
        """Get and validate user input"""
        while True:
            try:
                user_input = input(f"\n{prompt} ").strip().lower()
                if valid_options is None or user_input in valid_options:
                    return user_input
                else:
                    print(f"❌ Please choose from: {', '.join(valid_options)}")
            except KeyboardInterrupt:
                print("\n\n👋 Thanks for playing! Goodbye!")
                sys.exit(0)
            except EOFError:
                print("\n\n👋 Thanks for playing! Goodbye!")
                sys.exit(0)
    
    def display_status(self):
        """Display current player status"""
        print(f"\n{'='*50}")
        print(f"🏥 Health: {self.state.health}/100")
        print(f"💰 Gold: {self.state.gold}")
        print(f"🌟 Reputation: {self.state.reputation}")
        print(f"🎒 Inventory: {', '.join(self.state.inventory) if self.state.inventory else 'Empty'}")
        print(f"{'='*50}")
    
    def type_text(self, text: str, delay: float = 0.03):
        """Display text with typing effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def clear_screen(self):
        """Clear the console screen"""
        print("\n" * 50)
    
    def run(self):
        """Main game loop"""
        self.clear_screen()
        self.show_intro()
        
        while self.game_running:
            if self.current_scene:
                self.current_scene(self)
            else:
                # Default to start location
                self.go_to_location("start")
    
    def show_intro(self):
        """Display game introduction"""
        print("🎮" * 20)
        print("    THE LOST REALMS OF ELDRIA")
        print("🎮" * 20)
        print()
        
        self.type_text("Welcome, brave adventurer! You find yourself in the mystical realm of Eldria...")
        self.type_text("A land where magic flows like rivers and ancient secrets lie hidden in every shadow.")
        self.type_text("Your journey begins in the peaceful village of Moonhaven, but destiny has greater plans for you.")
        print()
        
        name = input("What is your name, traveler? ").strip()
        if not name:
            name = "Brave Adventurer"
        
        self.type_text(f"Ah, {name}! The stars have foretold your arrival...")
        self.type_text("Your adventure is about to begin. Choose wisely, for every decision shapes your destiny.")
        print()
        
        input("Press Enter to begin your journey...")
        self.clear_screen()

def create_game():
    """Create and configure the game with all scenes and locations"""
    game = GameEngine()
    
    # Define all game scenes
    def start_scene(game_engine):
        """Starting scene in Moonhaven village"""
        game_engine.clear_screen()
        game_engine.type_text("🌙 MOONHAVEN VILLAGE")
        game_engine.type_text("You stand in the center of Moonhaven, a quaint village nestled between rolling hills.")
        game_engine.type_text("The air is crisp with the scent of pine and the distant sound of a blacksmith's hammer.")
        game_engine.type_text("Villagers go about their daily business, casting curious glances your way.")
        print()
        
        game_engine.display_status()
        
        game_engine.type_text("What would you like to do?")
        choice = game_engine.get_user_input(
            "1. Visit the local tavern\n2. Check the notice board\n3. Talk to the village elder\n4. Explore the forest path\n5. Check your inventory\nChoice: ",
            ["1", "2", "3", "4", "5"]
        )
        
        if choice == "1":
            game_engine.go_to_location("tavern")
        elif choice == "2":
            game_engine.go_to_location("notice_board")
        elif choice == "3":
            game_engine.go_to_location("elder")
        elif choice == "4":
            game_engine.go_to_location("forest_path")
        elif choice == "5":
            game_engine.go_to_location("inventory")
    
    def tavern_scene(game_engine):
        """Tavern scene with first major decision"""
        game_engine.clear_screen()
        game_engine.type_text("🍺 THE GOLDEN ALE TAVERN")
        game_engine.type_text("The tavern is warm and inviting, filled with the sound of laughter and clinking mugs.")
        game_engine.type_text("A bard strums a lute in the corner, singing tales of distant lands and heroic deeds.")
        game_engine.type_text("At the bar, you notice a mysterious figure in dark robes, watching you intently.")
        print()
        
        game_engine.type_text("🎯 DECISION POINT #1: The Mysterious Stranger")
        game_engine.type_text("The stranger approaches you with a proposition...")
        game_engine.type_text("'I have a map to an ancient temple filled with treasures,' they whisper.")
        game_engine.type_text("'But I need a partner for this dangerous journey. Are you interested?'")
        print()
        
        choice = game_engine.get_user_input(
            "1. Accept the offer (requires 20 gold)\n2. Decline politely\n3. Ask for more details\n4. Return to village square\nChoice: ",
            ["1", "2", "3", "4"]
        )
        
        if choice == "1":
            if game_engine.state.gold >= 20:
                game_engine.state.modify_gold(-20)
                game_engine.state.add_item("Ancient Map")
                game_engine.state.game_flags["accepted_quest"] = True
                game_engine.type_text("You hand over 20 gold and receive the ancient map.")
                game_engine.type_text("'Meet me at the forest edge at dawn tomorrow,' the stranger says.")
                game_engine.go_to_location("start")
            else:
                game_engine.type_text("❌ You don't have enough gold for this venture.")
                game_engine.go_to_location("start")
        elif choice == "2":
            game_engine.state.modify_reputation(5)
            game_engine.type_text("You decline politely. The stranger nods respectfully and leaves.")
            game_engine.type_text("The villagers seem to appreciate your cautious nature.")
            game_engine.go_to_location("start")
        elif choice == "3":
            game_engine.type_text("'The temple lies in the Darkwood Forest, guarded by ancient traps and creatures.'")
            game_engine.type_text("'The reward could be worth thousands of gold pieces...'")
            game_engine.type_text("The stranger seems impatient with your questions.")
            game_engine.go_to_location("tavern")
        elif choice == "4":
            game_engine.go_to_location("start")
    
    def notice_board_scene(game_engine):
        """Notice board with quest opportunities"""
        game_engine.clear_screen()
        game_engine.type_text("📋 VILLAGE NOTICE BOARD")
        game_engine.type_text("Various notices and requests are pinned to the weathered wooden board.")
        game_engine.type_text("Some are recent, others have been here for weeks.")
        print()
        
        game_engine.type_text("Available Quests:")
        game_engine.type_text("1. 🐺 Hunt wolves threatening the village (Reward: 30 gold)")
        game_engine.type_text("2. 🌿 Gather rare herbs for the healer (Reward: 15 gold + healing potion)")
        game_engine.type_text("3. 📦 Deliver a package to the next village (Reward: 25 gold)")
        print()
        
        choice = game_engine.get_user_input(
            "1. Accept wolf hunting quest\n2. Accept herb gathering quest\n3. Accept delivery quest\n4. Return to village square\nChoice: ",
            ["1", "2", "3", "4"]
        )
        
        if choice == "1":
            game_engine.state.add_item("Wolf Hunting Contract")
            game_engine.state.game_flags["wolf_quest"] = True
            game_engine.type_text("You take the wolf hunting contract from the board.")
            game_engine.type_text("The village guard will provide you with a weapon.")
            game_engine.go_to_location("start")
        elif choice == "2":
            game_engine.state.add_item("Herb Gathering List")
            game_engine.state.game_flags["herb_quest"] = True
            game_engine.type_text("You take the herb gathering list.")
            game_engine.type_text("The healer's hut is near the forest edge.")
            game_engine.go_to_location("start")
        elif choice == "3":
            game_engine.state.add_item("Delivery Package")
            game_engine.state.game_flags["delivery_quest"] = True
            game_engine.type_text("You take the delivery package.")
            game_engine.type_text("The recipient is in the village of Stonebridge, a day's journey away.")
            game_engine.go_to_location("start")
        elif choice == "4":
            game_engine.go_to_location("start")
    
    def elder_scene(game_engine):
        """Village elder with wisdom and lore"""
        game_engine.clear_screen()
        game_engine.type_text("👴 VILLAGE ELDER'S COTTAGE")
        game_engine.type_text("The elder's cottage is filled with books, scrolls, and mysterious artifacts.")
        game_engine.type_text("Elder Thorne sits by the fireplace, his wise eyes twinkling with ancient knowledge.")
        print()
        
        game_engine.type_text("'Ah, a new face in Moonhaven,' the elder says warmly.")
        game_engine.type_text("'I sense great potential in you, young one. Perhaps you seek knowledge?'")
        print()
        
        choice = game_engine.get_user_input(
            "1. Ask about the village's history\n2. Inquire about local legends\n3. Seek advice for your journey\n4. Return to village square\nChoice: ",
            ["1", "2", "3", "4"]
        )
        
        if choice == "1":
            game_engine.type_text("'Moonhaven was founded by the Moonweaver family, blessed by the goddess Luna.'")
            game_engine.type_text("'We've lived in peace for generations, but dark times may be coming...'")
            game_engine.state.modify_reputation(3)
            game_engine.go_to_location("elder")
        elif choice == "2":
            game_engine.type_text("'Legends speak of the Crystal Caverns beneath the mountains.'")
            game_engine.type_text("'They say the crystals there can grant visions of the future...'")
            game_engine.state.add_item("Crystal Cavern Knowledge")
            game_engine.go_to_location("elder")
        elif choice == "3":
            game_engine.type_text("'Trust your instincts, but remember: not all that glitters is gold.'")
            game_engine.type_text("'Sometimes the greatest treasures are found in unexpected places.'")
            game_engine.state.modify_reputation(5)
            game_engine.go_to_location("elder")
        elif choice == "4":
            game_engine.go_to_location("start")
    
    def forest_path_scene(game_engine):
        """Forest path with second major decision"""
        game_engine.clear_screen()
        game_engine.type_text("🌲 FOREST PATH")
        game_engine.type_text("The forest path winds through ancient trees, their branches creating a natural canopy.")
        game_engine.type_text("Sunlight filters through the leaves, creating dancing patterns on the forest floor.")
        game_engine.type_text("You hear the distant sound of running water and the calls of forest creatures.")
        print()
        
        game_engine.type_text("🎯 DECISION POINT #2: The Forest Crossroads")
        game_engine.type_text("The path splits into three directions:")
        game_engine.type_text("1. A well-traveled path leading to a nearby village")
        game_engine.type_text("2. A narrow, overgrown trail that seems to lead deeper into the forest")
        game_engine.type_text("3. A path that follows the sound of water")
        print()
        
        choice = game_engine.get_user_input(
            "1. Take the well-traveled path\n2. Follow the overgrown trail\n3. Follow the water sound\n4. Return to village\nChoice: ",
            ["1", "2", "3", "4"]
        )
        
        if choice == "1":
            game_engine.type_text("You follow the well-traveled path...")
            game_engine.type_text("After a short walk, you reach the village of Stonebridge.")
            game_engine.state.modify_reputation(2)
            if game_engine.state.game_flags.get("delivery_quest"):
                game_engine.state.modify_gold(25)
                game_engine.state.remove_item("Delivery Package")
                game_engine.state.completed_quests.append("Delivery Quest")
                game_engine.type_text("✅ You successfully delivered the package and earned 25 gold!")
            game_engine.go_to_location("stonebridge")
        elif choice == "2":
            game_engine.type_text("You venture down the overgrown trail...")
            game_engine.type_text("The path becomes increasingly difficult to follow.")
            game_engine.type_text("Suddenly, you stumble upon a hidden clearing with rare herbs!")
            if game_engine.state.game_flags.get("herb_quest"):
                game_engine.state.add_item("Rare Herbs")
                game_engine.state.modify_gold(15)
                game_engine.state.add_item("Healing Potion")
                game_engine.state.completed_quests.append("Herb Quest")
                game_engine.type_text("✅ You found the rare herbs and completed the quest!")
            else:
                game_engine.state.add_item("Rare Herbs")
                game_engine.type_text("You found some rare herbs. These might be valuable!")
            game_engine.go_to_location("hidden_clearing")
        elif choice == "3":
            game_engine.type_text("You follow the sound of water...")
            game_engine.type_text("You discover a beautiful waterfall with a small cave behind it.")
            game_engine.type_text("Inside the cave, you find an old chest!")
            game_engine.go_to_location("waterfall_cave")
        elif choice == "4":
            game_engine.go_to_location("start")
    
    def inventory_scene(game_engine):
        """Inventory management scene"""
        game_engine.clear_screen()
        game_engine.type_text("🎒 INVENTORY")
        print()
        
        if game_engine.state.inventory:
            for i, item in enumerate(game_engine.state.inventory, 1):
                game_engine.type_text(f"{i}. {item}")
        else:
            game_engine.type_text("Your inventory is empty.")
        
        print()
        game_engine.display_status()
        
        game_engine.get_user_input("Press Enter to return to village square...")
        game_engine.go_to_location("start")
    
    def stonebridge_scene(game_engine):
        """Stonebridge village scene"""
        game_engine.clear_screen()
        game_engine.type_text("🏘️  STONEBRIDGE VILLAGE")
        game_engine.type_text("Stonebridge is a larger village, known for its stone architecture and bustling market.")
        game_engine.type_text("Merchants call out their wares, and the air is filled with the aroma of fresh bread.")
        print()
        
        choice = game_engine.get_user_input(
            "1. Visit the market\n2. Check the local inn\n3. Return to Moonhaven\nChoice: ",
            ["1", "2", "3"]
        )
        
        if choice == "1":
            game_engine.type_text("The market is filled with various goods and merchants.")
            if game_engine.state.gold >= 10:
                buy = game_engine.get_user_input(
                    "Would you like to buy a healing potion for 10 gold? (y/n): ",
                    ["y", "n"]
                )
                if buy == "y":
                    game_engine.state.modify_gold(-10)
                    game_engine.state.add_item("Healing Potion")
            game_engine.go_to_location("stonebridge")
        elif choice == "2":
            game_engine.type_text("The inn is cozy and welcoming.")
            game_engine.type_text("You rest for a while and feel refreshed.")
            game_engine.state.modify_health(20)
            game_engine.go_to_location("stonebridge")
        elif choice == "3":
            game_engine.go_to_location("start")
    
    def hidden_clearing_scene(game_engine):
        """Hidden clearing in the forest"""
        game_engine.clear_screen()
        game_engine.type_text("🌿 HIDDEN CLEARING")
        game_engine.type_text("The clearing is bathed in golden sunlight, with rare flowers blooming everywhere.")
        game_engine.type_text("A small stone altar stands in the center, covered in ancient runes.")
        print()
        
        choice = game_engine.get_user_input(
            "1. Examine the altar\n2. Gather more herbs\n3. Return to forest path\nChoice: ",
            ["1", "2", "3"]
        )
        
        if choice == "1":
            game_engine.type_text("The runes glow faintly as you approach...")
            game_engine.type_text("You feel a surge of magical energy!")
            game_engine.state.modify_health(30)
            game_engine.state.modify_reputation(10)
            game_engine.type_text("The altar's magic has restored your health and blessed you!")
            game_engine.go_to_location("hidden_clearing")
        elif choice == "2":
            game_engine.state.add_item("More Rare Herbs")
            game_engine.type_text("You gather additional rare herbs.")
            game_engine.go_to_location("hidden_clearing")
        elif choice == "3":
            game_engine.go_to_location("forest_path")
    
    def waterfall_cave_scene(game_engine):
        """Waterfall cave with third major decision"""
        game_engine.clear_screen()
        game_engine.type_text("💎 WATERFALL CAVE")
        game_engine.type_text("Behind the waterfall, you find a small cave illuminated by glowing crystals.")
        game_engine.type_text("An ornate chest sits in the center, but you notice strange markings on the floor.")
        game_engine.type_text("The air is thick with ancient magic.")
        print()
        
        game_engine.type_text("🎯 DECISION POINT #3: The Ancient Chest")
        game_engine.type_text("The chest looks valuable, but the markings suggest it might be trapped.")
        game_engine.type_text("You also notice a small passage leading deeper into the cave.")
        print()
        
        choice = game_engine.get_user_input(
            "1. Try to open the chest\n2. Explore the deeper passage\n3. Leave the cave\nChoice: ",
            ["1", "2", "3"]
        )
        
        if choice == "1":
            game_engine.type_text("You carefully approach the chest...")
            if game_engine.state.has_item("Ancient Map"):
                game_engine.type_text("The map's markings help you avoid the trap!")
                game_engine.state.add_item("Ancient Artifact")
                game_engine.state.modify_gold(100)
                game_engine.state.modify_reputation(15)
                game_engine.type_text("✅ You successfully opened the chest and found a valuable artifact!")
            else:
                game_engine.type_text("A magical trap activates!")
                game_engine.state.modify_health(-30)
                game_engine.type_text("You're injured by the trap, but you manage to escape.")
            game_engine.go_to_location("forest_path")
        elif choice == "2":
            game_engine.type_text("You venture deeper into the cave...")
            game_engine.type_text("You discover an ancient library filled with forgotten knowledge!")
            game_engine.state.add_item("Ancient Tome")
            game_engine.state.modify_reputation(20)
            game_engine.type_text("The knowledge you've found could be priceless!")
            game_engine.go_to_location("forest_path")
        elif choice == "3":
            game_engine.type_text("You decide to leave the cave for now.")
            game_engine.go_to_location("forest_path")
    
    # Add all scenes to the game
    game.add_location("start", start_scene)
    game.add_location("tavern", tavern_scene)
    game.add_location("notice_board", notice_board_scene)
    game.add_location("elder", elder_scene)
    game.add_location("forest_path", forest_path_scene)
    game.add_location("inventory", inventory_scene)
    game.add_location("stonebridge", stonebridge_scene)
    game.add_location("hidden_clearing", hidden_clearing_scene)
    game.add_location("waterfall_cave", waterfall_cave_scene)
    
    return game

def main():
    """Main function to run the game"""
    print("🎮 Starting The Lost Realms of Eldria...")
    print("Loading game assets...")
    
    # Create and run the game
    game = create_game()
    game.run()

if __name__ == "__main__":
    main()
