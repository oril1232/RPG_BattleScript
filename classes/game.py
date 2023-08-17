import random

class bcolors:
    HEADER='\033[95m'
    OKBLUE='\033[94m'
    OKGREEN='\033[92m'
    WARNING='\033[93m'
    FAIL='\033[91m'
    ENDC='\033[0m'
    BOLD='\033[1m'
    UNDERLINE='\033[4m'

class Player:
    def __init__(self, hp, mp, atk, defence, magic):
        self.max_hp = hp
        self.currenthp = hp
        self.maxmp = mp
        self.currentmp = mp
        self.atk_low = atk - 10
        self.atk_high = atk + 10
        self.defence = defence
        self.magic = magic
        self.actions=["Attack","Magic"]

    def atk_damge(self):
        return  random.randrange(self.atk_high, self.atk_low)
    def magic_damage(self,i):
        lmagic=self.magic[i]["Damage"]-5
        hmagic=self.magic[i]["Damage"]+5
        return random.randrange(lmagic, hmagic)
    def self_dmg (self,dmg):
        HP= self.currenthp - dmg
        if HP<0:
            HP=0
        return HP
    def get_max_hp(self):
        return self.MaxHP

    def get_current_hp(self):
        return self.currenthp

    def get_max_mp(self):
        return self.maxmp

    def get_current_mp(self):
        return self.currentmp
    def reduce_mp(self,cost):
        self.currentmp-=cost

    def get_spell_name(self,i):
        return self.magic[i]["Name"]
    def get_spell_mp_cost(self,i):
        return self.magic[i]["Cost"]

    def choose_action(self):
        i=1
        print("Actions:")
        for item in self.actions:
            print(str(i)+":",item)
            i+=1


    def choose_magic(self):
        i=1
        print("Magic Spells")
        for spell in self.magic:
            print(str(i)+":",spell["Name"],"(cost:",str(spell["Cost"],")"))
            i+=1
