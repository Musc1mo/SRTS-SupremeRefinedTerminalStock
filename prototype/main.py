"""main.py - SRTS Prototype Demo

Simple demonstration of Stage 1 gameplay: Cellular Survival
Run this to see cells gathering resources, evolving, and fighting.

Usage:
    python main.py

For Warp AI: This demo shows the core gameplay loop.
Expand with proper game loop, rendering, and user input.
"""

from cell import SoupCell, EvolutionPath
import random
import time

def print_separator(char="=", length=70):
    print(char * length)

def simulate_soup_ecosystem():
    """Simulate a basic soup ecosystem with multiple cells."""
    
    print_separator()
    print("SRTS PROTOTYPE: Stage 1 - Cellular Survival")
    print_separator()
    print()
    
    # Create diverse soup civilizations
    civilizations = [
        SoupCell("Borscht", health=120),
        SoupCell("Miso", health=100),
        SoupCell("Tom Yam", health=110),
        SoupCell("Green Mold", health=90)
    ]
    
    print("=== INITIAL STATE ===")
    for cell in civilizations:
        print(cell)
    print()
    
    # Simulation rounds
    round_num = 1
    
    while len([c for c in civilizations if c.health > 0]) > 1:
        print(f"\n--- ROUND {round_num} ---")
        
        # Each cell performs actions
        for cell in civilizations:
            if cell.health <= 0:
                continue
            
            # Random action: gather resources or attack
            action = random.choice(["gather", "gather", "attack"])  # 2/3 chance to gather
            
            if action == "gather":
                cell.gather_resources()
                
                # Try to evolve if enough resources
                if cell.resources >= 10:
                    # Choose evolution based on civilization "personality"
                    if "Borscht" in cell.civilization:
                        cell.evolve(EvolutionPath.ADAPTATION)
                    elif "Tom Yam" in cell.civilization:
                        cell.evolve(EvolutionPath.AGGRESSION)
                    elif "Miso" in cell.civilization:
                        cell.evolve(EvolutionPath.STEALTH)
                    else:
                        cell.evolve(random.choice(list(EvolutionPath)))
            
            elif action == "attack":
                # Find a random living target
                potential_targets = [c for c in civilizations if c.health > 0 and c != cell]
                if potential_targets:
                    target = random.choice(potential_targets)
                    cell.attack_target(target)
        
        # Remove dead cells
        civilizations = [c for c in civilizations if c.health > 0]
        
        print(f"\nSurvivors: {len(civilizations)}")
        time.sleep(0.5)  # Slow down for readability
        round_num += 1
        
        # Safety limit
        if round_num > 20:
            print("\n[Maximum rounds reached]")
            break
    
    print_separator()
    print("=== FINAL STATE ===")
    for cell in civilizations:
        print(cell)
    
    if len(civilizations) == 1:
        winner = civilizations[0]
        print(f"\n🏆 WINNER: {winner.civilization}!")
        print(f"Final Stats: HP={winner.health}/{winner.max_health} ATK={winner.attack} DEF={winner.defense}")
    else:
        print("\n⚔️ STALEMATE: Multiple survivors remain")
    
    print_separator()
    print("\nPrototype complete. Ready for Warp AI expansion.")
    print("Next steps: Add proper game loop, rendering, player control.")
    print_separator()

if __name__ == "__main__":
    simulate_soup_ecosystem()
