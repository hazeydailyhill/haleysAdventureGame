import random
import os
import time
import gameMechanics
import art
import gamemap
from badGuy import *
from User import *

banana = "Kyle"
#IM RUNNING THINGS BELOW HERE!!!!!!!
#w,x,y,z = newPlayer() #w= name, x= age, y= height, z=SS#, ENTERED 100 FOR HEALTH, ENTERED ROBERT FOR ENEMY
#player1 = Player(w,x,y,z,100,Robert)
player1 = Player(banana, 100, "Robert Pattinson", False, False)
#print(player1.name)
#print(player1.health)

art.titleScreen()
gamemap.mapLoop()
def fight():
    robert = Enemy("Robert Pattinson", 1234567, 100, player1.name, False, False)
    os.system("cls")
    while robert.health > 0 and player1.health > 0:
        print("\n"+player1.name+"'s turn"+"\n")
        initialBleed = robert.bleed
        directDamage, robert.bleed = player1.menu()
        if initialBleed != robert.bleed:
            robert.bleed = True
        robert.health, robert.guard = gameMechanics.damageCheck(robert.health, directDamage, robert.bleed, robert.guard)
        gameMechanics.healthCheck(robert.name, robert.health, robert.bleed)
        time.sleep(1)
        if robert.health > 0:
            print("\n"+robert.name+"'s turn"+"\n")
            initialBleed = player1.bleed
            directDamage, player1.bleed = robert.robertAttack()
            if initialBleed != player1.bleed:
                player1.bleed = True
            player1.health, player1.guard = gameMechanics.damageCheck(player1.health, directDamage, player1.bleed, player1.guard)
            gameMechanics.healthCheck(player1.name, player1.health, player1.bleed)
        else:
            art.victoryAnimation()
            print(robert.name+" has been slain, thank God, his movies were crimes against humanity")
        if player1.health <= 0:
            art.deathAnimation()
            print(player1.name+" has died. The world deserved more.")
        #robert.health = 0 
        cont = input("\nhit enter to continue...\n")
        os.system("cls")
    art.credits()