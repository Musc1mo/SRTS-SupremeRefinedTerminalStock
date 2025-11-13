"""Cell.py - Base cell class for SRTS prototype

This module contains the fundamental SoupCell class that represents
a single organism in the primordial soup. Cells can evolve along three paths:
- Aggression (attack damage)
- Adaptation (defense/resource gathering)
- Stealth (camouflage/speed)

For use with Warp AI: This is a vibe-coding prototype for rapid iteration.
"""

import random
from enum import Enum

class EvolutionPath(Enum):
    """Evolution specialization paths"""
    AGGRESSION = "aggression"
    ADAPTATION = "adaptation"
    STEALTH = "stealth"

class SoupCell:
    """Represents a single cell organism in the soup ecosystem.
    
    Attributes:
        civilization (str): Name of the soup civilization (e.g., 'Borscht', 'Miso')
        health (int): Current hit points
        max_health (int): Maximum hit points
        attack (int): Base attack damage
        defense (int): Damage reduction
        speed (int): Movement/action speed
        stealth (int): Camouflage effectiveness (0-100)
        resources (int): Gathered resources for evolution
        evolution_points (dict): Points invested in each path
    """
    
    def __init__(self, civilization="Generic", health=100):
        self.civilization = civilization
        self.health = health
        self.max_health = health
        
        # Base stats
        self.attack = 10
        self.defense = 5
        self.speed = 10
        self.stealth = 0  # 0 = fully visible, 100 = invisible
        
        # Resource management
        self.resources = 0
        self.evolution_points = {
            EvolutionPath.AGGRESSION: 0,
            EvolutionPath.ADAPTATION: 0,
            EvolutionPath.STEALTH: 0
        }
        
        # Status effects
        self.is_moving = False
        self.poison_stacks = 0
    
    def evolve(self, path: EvolutionPath, cost=10):
        """Spend resources to evolve along a specific path.
        
        Args:
            path: Which evolution path to upgrade
            cost: Resource cost for upgrade
            
        Returns:
            bool: True if evolution succeeded, False if insufficient resources
        """
        if self.resources < cost:
            return False
        
        self.resources -= cost
        self.evolution_points[path] += 1
        
        # Apply stat changes based on path
        if path == EvolutionPath.AGGRESSION:
            self.attack += 5
            print(f"{self.civilization} cell evolved SPIKES! Attack: {self.attack}")
        
        elif path == EvolutionPath.ADAPTATION:
            self.defense += 3
            self.max_health += 10
            self.health += 10  # Heal on evolution
            print(f"{self.civilization} cell grew SHELL ARMOR! Defense: {self.defense}")
        
        elif path == EvolutionPath.STEALTH:
            self.stealth += 20
            self.speed += 3
            print(f"{self.civilization} cell developed CAMOUFLAGE! Stealth: {self.stealth}%")
        
        return True
    
    def attack_target(self, target):
        """Attack another cell.
        
        Args:
            target: Another SoupCell to attack
            
        Returns:
            dict: Combat result with damage dealt and kill status
        """
        # Calculate damage
        base_damage = self.attack
        actual_damage = max(1, base_damage - target.defense)
        
        # Apply damage
        target.health -= actual_damage
        
        result = {
            "attacker": self.civilization,
            "defender": target.civilization,
            "damage": actual_damage,
            "defender_killed": target.health <= 0
        }
        
        print(f"{self.civilization} attacks {target.civilization} for {actual_damage} damage!")
        
        if target.health <= 0:
            print(f"{target.civilization} has been eliminated!")
            # Attacker gains resources from kill
            self.resources += 5
        
        return result
    
    def gather_resources(self, amount=2):
        """Gather resources from the environment.
        
        Args:
            amount: Base amount to gather (modified by adaptation evolution)
        """
        # Adaptation path bonus
        adaptation_bonus = self.evolution_points[EvolutionPath.ADAPTATION] * 0.5
        total_gathered = int(amount * (1 + adaptation_bonus))
        
        self.resources += total_gathered
        print(f"{self.civilization} gathered {total_gathered} resources (Total: {self.resources})")
    
    def is_visible(self):
        """Check if cell is currently visible to enemies.
        
        Returns:
            bool: True if visible, False if camouflaged
        """
        # Stealth only works when not moving
        if self.is_moving:
            return True
        
        # Random chance based on stealth stat
        detection_roll = random.randint(0, 100)
        return detection_roll > self.stealth
    
    def __repr__(self):
        return (f"<SoupCell {self.civilization}: HP={self.health}/{self.max_health} "
                f"ATK={self.attack} DEF={self.defense} Resources={self.resources}>")

# --- EXAMPLE USAGE FOR WARP AI ---

if __name__ == "__main__":
    print("=" * 60)
    print("SRTS PROTOTYPE: Cell Evolution System")
    print("=" * 60)
    
    # Create two rival cells
    borscht = SoupCell("Borscht", health=120)
    mold = SoupCell("Green Mold", health=80)
    
    print(f"\n{borscht}")
    print(f"{mold}\n")
    
    # Borscht gathers resources
    print("--- Gathering Phase ---")
    borscht.gather_resources()
    borscht.gather_resources()
    borscht.gather_resources()
    borscht.gather_resources()
    borscht.gather_resources()
    
    # Borscht evolves aggression
    print("\n--- Evolution Phase ---")
    borscht.evolve(EvolutionPath.AGGRESSION)
    
    # Combat
    print("\n--- Combat Phase ---")
    result = borscht.attack_target(mold)
    
    print(f"\n{borscht}")
    print(f"{mold}")
    
    print("\n=" * 60)
    print("Prototype complete. Ready for Warp AI iteration.")
    print("=" * 60)
