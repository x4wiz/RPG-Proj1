import random
from classes.magic import Spell

class bcolors:
    HEDER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_dmg (self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal (self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("It's ", self.name,"'s turn" + "\n")
        print("ACTIONS")
        for item in self.actions:
            print("   ", str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("MAGIC")
        for spell in self.magic:
            print("   ", str(i) + ".", spell.name, "(cost:", str(spell.cost)+ ")")
            i += 1

    def choose_item(self):
        i = 1
        print("ITEMS")
        for item in self.items:
            print("   ", str(i) + ".", item["item"].name, " - ", item["item"].description, "(x", item["quantity"],")")
            i += 1

    def choose_enemy(self, enemies):
        i = 1
        print(bcolors.FAIL + "ENEMIES" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp != 0:
                print(i, ". " + enemy.name)
                i += 1
        enemy_choice = int(input()) - 1
        return enemy_choice

    def get_enemeny_stats(self):
        hp_bar = ""
        hp_value = (self.hp/self.maxhp)*100/2

        while hp_value > 0:
            hp_bar += "█"
            hp_value -= 1
        while len(hp_bar) < 50:
            hp_bar += " "
        
        mdf1 = ""

        if len(str(self.hp)) < len(str(self.maxhp)):
            chp = len(str(self.hp))
            
            while chp < len(str(self.maxhp)):
                mdf1 += " "
                chp += 1

        print("                          __________________________________________________ ")
        print(bcolors.BOLD + str(self.name) + "    " + mdf1 + str(self.hp) + "/"+ str(self.maxhp) + "      |" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|     ")
        

    def get_stats(self):
        hp_bar = ""
        hp_value = (self.hp / self.maxhp)*100/4
        while hp_value > 0:
            hp_bar += "█"
            hp_value -= 1
        while len(hp_bar) < 25:
            hp_bar += " "

        mp_bar = ""
        mp_value = (self.mp / self.maxmp)*100/10
        while mp_value > 0:
            mp_bar += "█"
            mp_value -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        mdf1 = ""
        mdf2 = ""

        if len(str(self.hp)) < len(str(self.maxhp)):
            chp = len(str(self.hp))
            
            while chp < len(str(self.maxhp)):
                mdf1 += " "
                chp += 1

        if len(str(self.mp)) < len(str(self.maxmp)):
            smp = len(str(self.mp))
            while smp < len(str(self.maxmp)):
                mdf2 += " "
                smp += 1

        print("                          _________________________               __________ ")
        print(bcolors.BOLD + str(self.name) + "    " + mdf1 + str(self.hp) + "/"+ str(self.maxhp) + "       |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|      " + bcolors.BOLD + mdf2 + str(self.mp) + "/" + str(self.maxmp) + "  |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")
        