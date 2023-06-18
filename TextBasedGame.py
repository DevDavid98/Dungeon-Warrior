# David A Garcia III

# import any module thats required for the text based game 
import random
import pygame
from sys import exit
from time import sleep
class Player():
    player_health = 5
    def __init__(self,name, player_type):
         self.name = name
         self.player_type = player_type

def player_controls():
        print("\n")
        print('To move directions type "go north", "go south", "go east" or "go west"')
        print('To grab a item type "get [item name]"')
        print("To quit the game type 'exit'")

def main_menu():
    print("WELCOME TO DUNGEON WARRIOR")
    print("-"*26)
    while True:
        print("\nTo begin press 'S' to start game")
        print("To view controls press 'C'")
        user_input = input("\nEnter a valid command: ")
        if user_input.lower() == "s":
            start()
        elif user_input.lower() == "c":
            player_controls()
        elif user_input.lower() == "exit":
             exit("Thank you for playing Dungeon Warrior")
        else:
             print("\n!!! Please enter a valid command !!!\n")

def knight_map():
 map_cells = [["Cell"]
              ["great hall"]
              ]

def backstory():
    print("In the early years of the kingdom the people flourished...")
    sleep(3)
    print("Over the years, the decades the kingdom went through trials and tribulations...")
    sleep(4)
    print("During the hard times the peasants learned to live with the hardships..")
    sleep(4)
    print("While the scum of the earth ruled in the castle taking lives with meaningless war and bickering...")
    sleep(4)
    print("You were sworn to protect the kingdom. Only for the corruption to reach your ranks..")
    sleep(4)
    print("You were drugged unconceious.")
    sleep(3)
    print("It is now your fate to find out why.")
    sleep(3)
    print("Escape the dark depths of the castles dungeon.")
    sleep(3)

def start():
    objective = "Retrieve your items and escape"
    player_types = ["Knight", "Wizard", "Warrior", "Thief"]
    backstory()
    print("-" * 60)
    print("You awaken in a dark cell trying to remember who you are..")
    sleep(3)
    player_name = input("What is your name?: ")
    player_role = input(f"{player_name} who were you? {player_types}: ")
    if player_role == player_types[0]:
        knight_map()



    



# Make sure file does not run when imported
if __name__ == "__main__":
    main_menu()
