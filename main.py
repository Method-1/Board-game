from gameClass import Game, Archive
import os

#my_file = open(r"C:\Users\adiab\gits\Board-game\data\storedGames.txt", "r")
#content_list = my_file.readlines()
#print(content_list)

# Function that clears screen, used similar in C#, found the pythonic way for it at StackOverflow
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def choices():
    print("\n Select between following alternatives: \n 1. Create a file that stores every game (this is only done once!) \n 2. Add a game in to the archive \n 3. Print out list of games in archive \n 4. Delete a game from the archive \n 5. Edit a game from the archive \n 6. Search for a game \n 7. Exit ")
# Create a menu for the user

def menu(archive):
    choices()
    choice = 0
    while choice is not 7:
        choice = int(input("Choose one of the alternatives to proceed >: "))
        #f = open(r'C:\Users\adiab\gits\Board-game\data\storedGames.txt', 'r')
        if choice == 1:
            archive.create_json("storedGames")
        if choice == 2:
            title = input("Title: ")
            #test unique input
            data = archive.read("storedGames")
            my_list = data["Game"]
            for item in my_list:
                if item["Title"] == title:
                    print("\nThis game already exists in the archive!\nPress any key to go back to the menu!")
                    back_to_menu = input("")
                    if back_to_menu == "":
                        #Clearing the screen with function cls
                        cls()
                        #Going back to menu
                        menu(Game_Archive)

            players = int(input("Player count: "))
            playtime = int(input("Time Limit: "))
            age = int(input("Recommended age: "))
            archive.add_game(title, players, playtime, age)
        if choice == 3:
            cls()
            games = archive.read("storedGames")
            game_list = games["Game"]
            # prints out all games that are stored in the archive
            print("These are the games we have in the archive! \n")
            for i in game_list:
                print(i)
            # print out a message that let's the user go back to the menu
            print("\nPress any key to get back to the menu!")
            back_to_menu = input("")
            if back_to_menu == "":
                cls()
                menu(Game_Archive)
        # Building code that enables the user to edit a game in the archive, not finished.
        if choice == 5:
            cls()
            games = archive.read("storedGames")
            game_list = games["Game"]
            print("These are the games we have in the archive, if you want to edit a game, type the title of it.\n")
            for i in game_list:
                print(i["Title"])
            
            title = input("Title of game you want to edit: ")
            
                #if item["Title"] == title:
                     
            #if title == 
            
            
            


        #thegame = Game(title,players,playtime,age)
        #thegame.save(title, players, playtime, age, "storedGames")
        #thegame.read("storedGames")


Game_Archive = Archive("Archive")

menu(Game_Archive)