# David A Garcia III

# import any module thats required for the text based game 
import random
import pygame
from sys import exit

def player_controls():
        print("\n")
        print('To move directions type "go north", "go south", "go east" or "go west"')
        print('To grab a item type "get [item name]"')
        print("To quit the game type 'exit'")

def main_menu():
    print("WELCOME TO DUNGEON WARRIOR")
    print("-"*26)
    while True:
        print("To begin press 'S' to start game")
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

def start():
    pass


# Make sure file does not run when imported
if __name__ == "__main__":
    main_menu()