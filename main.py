from classes.game import Player,bcolors
import random

magic=[{"Name":"Fireball","Cost":"25","Damage":random.randrange(8,48)},
       {"Name":" Lightning Bolt ","Cost":"25","Damage":random.randrange(8,48)},
       {"Name":"Ray Of Frost","Cost":"5","Damage":random.randrange(1,8)}]
player=Player(460,100,30,30,magic)