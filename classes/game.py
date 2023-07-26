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
    def __init__(self, HP, MP, ATK, DEF, Magic):
        self.MaxHP = HP
        self.CurrentHP = HP
        self.MaxMP = MP
        self.CurrentMP = MP
        self.ATK_Low = ATK-10
        self.ATK_High = ATK + 10
        self.DEF = DEF
        self.Magic = Magic
        self.actions=["Attack","Magic"]

    def ATK_Damge(self):
        return  random.randrange(self.ATK_High,self.ATK_Low)