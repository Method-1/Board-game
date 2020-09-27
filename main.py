from gameClass import Game, Archive
import os
import json

#my_file = open(r"C:\Users\adiab\gits\Board-game\data\storedGames.txt", "r")
#content_list = my_file.readlines()
#print(content_list)

# Function that let's user press any key to go back to menu
def backMenu():
    print("Press any key to get back to the menu!")
    back_to_menu = input("")
    if back_to_menu == "":
        cls()
        menu(Game_Archive)

# Function that clears screen, used similar in C#, found the pythonic way for it at StackOverflow
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def choices():
    print("\n Select between following alternatives: \n 1. Create a file that stores every game (this is only done once!) \n 2. Add a game in to the archive \n 3. Print out list of games in archive \n 4. Delete a game from the archive \n 5. Edit a game from the archive \n 6. Search for games with certain attributes \n 7. Exit ")
# Create a menu for the user

def menu(archive):
    choices()
    choice = 0
    while choice is not 7:
        choice = int(input("Choose one of the alternatives to proceed >: "))
        #f = open(r'C:\Users\adiab\gits\Board-game\data\storedGames.txt', 'r')
        if choice == 1:
            cls()
            archive.create_json("storedGames")
        if choice == 2:
            cls()
            title = input("Title: ")
            #test unique input
            data = archive.read("storedGames")
            my_list = data["Game"]
            for item in my_list:
                if item["Title"] == title:
                    print("\nThis game already exists in the archive!\n")
                    backMenu()

            players = int(input("Player count: "))
            playtime = int(input("Time Limit: "))
            age = int(input("Recommended age: "))
            archive.add_game(title, players, playtime, age)
            print("Your game has been added!")
            backMenu()
        if choice == 3:
            cls()
            games = archive.read("storedGames")
            game_list = games["Game"]
            # prints out all games that are stored in the archive
            print("These are the games we have in the archive! \n")
            for i in game_list:
                print(i)
            # print out a message that let's the user go back to the menu
            backMenu()
        # Let's the user remove a game (not finished)
        if choice == 4:
            cls()
            games = archive.read("storedGames")
            game_list = games["Game"]
            remove_game = int(input("Enter the title of the game you want to remove: "))
            for i in range(len(game_list)):
                if game_list[i]["Time Limit"] == remove_game:
                    print(game_list[i])
                    

        # Building code that enables the user to edit a game in the archive. (not finished).
        if choice == 5:
            cls()
            games = archive.read("storedGames")
            game_list = games["Game"]
            print("These are the games we have in the archive, if you want to edit a game, type the title of it.\n")
            for i in game_list:
                print(i["Title"])
            
            title = input("Title of game you want to edit: ")
        #Search for games by attributes (finished)
        if choice == 6:
            cls()
            games = archive.read("storedGames")
            game_list = games["Game"]

            print("Pick how you want to search for game: \n 1. Search by title \n 2. Search by player count \n 3. Search by time limit \n 4. Search by recommended age")
            new_choices = 0
            new_choices = int(input("Choose what you want to do: "))

            if new_choices == 1:
                cls()
                title_search = input("Enter title to search for all games with that title: ")
                print(f"You searched for games with the title: ¬¬¬{title_search}¬¬¬ \nBelow is the result: \n")
                for i in range(len(game_list)):
                    if game_list[i]["Title"] == title_search:
                        print(game_list[i])
                backMenu()

            if new_choices == 2:
                cls()
                search_pcount = int(input("Enter number of players: "))
                print(f"You searched for a game with the player count: {search_pcount}\nBelow is the result: \n")
                
                for i in range(len(game_list)):
                    if game_list[i]["Player Count"] == search_pcount:
                        print(game_list[i])
                backMenu()

            if new_choices == 3:
                cls()
                time_limit = int(input("Enter time limit number in minutes: "))
                print(f"You searched for a game with the timit limit of: {time_limit}\nBelow is the result: \n")

                for i in range(len(game_list)):
                    if game_list[i]["Time Limit"] == time_limit:
                        print(game_list[i])
                backMenu()
            
            if new_choices == 4:
                cls()
                search_age = int(input("Search games by recommended age: "))
                print(f"You searched for games with recommended age: {search_age}\nBelow is the result: \n")
                for i in range(len(game_list)):
                    if game_list[i]["Recommended age"] == search_age:
                        print(game_list[i])
                backMenu()


Game_Archive = Archive("Archive")

menu(Game_Archive)