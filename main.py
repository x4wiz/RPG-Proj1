from classes.game import Person
from classes.game import bcolors
from classes.magic import Spell
from classes.inventory import Item
import random



# Create black magic
fire = Spell("Fire", 10, 300, "Black")
thunder = Spell("Thunder", 10, 300, "Black")
blizzard = Spell("Blizzard", 10, 300, "Black")
meteor = Spell("Meteor", 20, 500, "Black")
quake = Spell("Quake", 14, 280, "Black")

# Create white magic
cure = Spell("Heal", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

# Create items

potion = Item("Potion", "potion", "Heals 50 damage", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 damage", 100)
megapotion = Item("Mega-Potion", "potion", "Heals 500 damage", 500)
elixer = Item("Elixer", "elixer", "Restores full HP/MP of one party member", 9999)
megaelixer = Item("Mega-Elixer", "elixer", "Restores full HP/MP of all party members", 9999)
grenade = Item("Grenade", "attack", "Attacks enemy for 500 HP", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": megapotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": megaelixer, "quantity": 2},
                {"item": grenade, "quantity": 5}]
            
# Instantiate characters
player1 = Person("Valos", 3260, 65, 111160, 34, player_spells, player_items)
player2 = Person("Nick ", 4160, 65, 200, 34, player_spells, player_items)
player3 = Person("Robot", 3089, 65, 130, 34, player_spells, player_items)

players = [player1, player2, player3]

enemy1 = Person("Imp   ", 3000, 65, 600, 25, [], [])
enemy2 = Person("Rock", 12000, 65, 400, 25, [], [])
enemy3 = Person("Imp   ", 3000, 65, 600, 25, [], [])

enemies = [enemy1, enemy2, enemy3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)


while running:
    print("========================\n")
    print("NAME                     HP                                     MP")
    for player in players:
        player.get_stats()
    
    print("\n")

    for enemy in enemies:
        enemy.get_enemeny_stats()

    for player in players:
    #Choose which way to attack
        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1
        print("You choose: ", player.actions[index])
    # Attack with weapon
        if index == 0:
            dmg = player.generate_damage()
            enemy_choice = player.choose_enemy(enemies)
            enemies[enemy_choice].take_dmg(dmg)
            print("\n" + bcolors.OKGREEN + str(player.name) + " attacked " + enemies[enemy_choice].name + " for " + str(dmg) + bcolors.ENDC + "\n")
            
            if enemies[enemy_choice].hp == 0:
                print(bcolors.FAIL + enemies[enemy_choice].name + "has died" + bcolors.ENDC)
                del enemies[enemy_choice]
    # Attack with magic
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose your spell:")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            spell_name = spell.name
            spell_cost = spell.cost

            if player.mp < spell_cost:
                print(bcolors.FAIL + "Not enough magic points!" + bcolors.ENDC)
                continue

            player.reduce_mp(spell_cost)

            if spell.type == "White":
                player.heal(magic_dmg)
                print(bcolors.OKGREEN + str(player.name) + " used a", str(spell.name), " spell and healed ", str(magic_dmg)," HP" + bcolors.ENDC + "\n")
            elif spell.type == "Black":
                enemy_choice = player.choose_enemy(enemies)
                enemies[enemy_choice].take_dmg(dmg)
                print(bcolors.OKBLUE + str(player.name) + " hit " + enemies[enemy_choice].name + " with " + str(spell_name),"for ", str(magic_dmg) + bcolors.ENDC + "\n")

                if enemies[enemy_choice].get_hp == 0:
                    print(bcolors.FAIL + enemies[enemy_choice].name.replace("  ","") + "has died" + bcolors.ENDC)
                    del enemies[enemy_choice]

#Attack with an Item
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose an Item to use:")) -1
            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] >=1:
                if item.type == "potion":
                    player.heal(item.prop)
                    print(bcolors.OKGREEN + str(player.name) + " used", item.name, "which ", item.description + bcolors.ENDC)
                elif item.type == "elixer":
                    if item.name == "Mega-Elixer":
                        for i in players:
                            player.hp = player.maxhp
                            player.mp = player.maxmp
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                    print(bcolors.OKGREEN + str(player.name) + " used", item.name, "and it restored his full HP and MP" + bcolors.ENDC)
                elif item.type == "attack":
                    enemy_choice = player.choose_enemy(enemies)
                    enemies[enemy_choice].take_dmg(dmg)
                    print(bcolors.FAIL + str(player.name) + " used ", item.name, "and it caused ", item.prop, " amount of damage to " + enemies[enemy_choice].name + bcolors.ENDC)
                    
                    if enemies[enemy_choice].get_hp == 0:
                        print(bcolors.FAIL + enemies[enemy_choice].name.replace("  ","") + "has died" + bcolors.ENDC)
                        del enemies[enemy_choice]
                
                player.items[item_choice]["quantity"] -= 1

            else:
                print(player.name + "don't have this item")
                continue


# Enemy attacks
    target = random.randrange(0,3)
    enemy_dmg = enemy1.generate_damage()
    players[target].take_dmg(enemy_dmg)
    print(bcolors.FAIL + "Enemy has hit" + players[target].name + " for " + str(enemy_dmg) + bcolors.ENDC)

"""
    #Printing current stats
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Enemy has defeated you!" + bcolors.ENDC)
        running = False


'''
print("Attack gamage: ", player.generate_damage())
print("Fire damage: ", player.generate_spell_damage(0))
print("Thunder damage: ", player.generate_spell_damage(1))
'''
"""