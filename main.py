from gameClass import Game, Archive
import os
import json


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


def menu(archive):
    archive.menu_alternatives()
    choice = 0
    #Use this line of code to create a file (if file doesn't exist)
    #archive.create_json("storedGames")
    #Opens json file named storedGames and opens it for reading.
    games = archive.read("storedGames")
    #variable that stores the list with dictionaries
    game_list = games["Game"]

    while choice != 7:
        try:
            choice = int(input("Choose one of the alternatives to proceed >: "))
            cls()
            if choice == 1:
                title = input("Title: ").lower()
                #test unique input
                for item in game_list:
                    if item["Title"] == title:
                        print("\nThis game already exists in the archive!\n")
                        backMenu()

                players = int(input("Player count: "))
                playtime = int(input("Time Limit: "))
                age = int(input("Recommended age: "))
                archive.add_game(title, players, playtime, age)
                print("Your game has been added!")
                backMenu()
            if choice == 2:
            # prints out all games that are stored in the archive
                print("These are the games we have in the archive! \n")
                for i in game_list:
                    print(i)
                # print out a message that let's the user go back to the menu
                backMenu()
            # Let's the user remove a game
            if choice == 3:
                archive.delete_game(games, "storedGames")
                backMenu()
                    
            # code that enables the user to edit a game in the archive. 
            if choice == 4:
                y = 0
                print("These are the games we have in the archive.\n")
                for i in game_list:
                    print(y,i)
                    y += 1
            
                chosen_game = int(input("\nChoose game you want to edit: "))
                my_dict = game_list[chosen_game]
                cls()
                print(f"You have chosen to edit: {my_dict}")
                print("Choose what you want to edit: \n1. Title \n2. Player count \n3. Time limit \n4. Recommended age")
                choice = 0
                choice = int(input("Select choice: "))
                if choice == 1:
                    new_title = input("Add new title: ").lower()
                    my_dict["Title"] = new_title
                    print("Title is now edited!")
                    archive.edit_game(games, "storedGames")
                    backMenu()
                if choice == 2:
                    new_playercount = int(input("Add new player count: "))
                    my_dict["Player Count"] = new_playercount
                    print("Player count is now edited!")
                    archive.edit_game(games, "storedGames")
                    backMenu()
                if choice == 3:
                    new_timelimit = int(input("Add new time limit: "))
                    my_dict["Time Limit"] = new_timelimit
                    print("Time limit is now edited!")
                    archive.edit_game(games, "storedGames")
                    backMenu()
                if choice == 4:
                    new_age = int(input("Add new recommended age: "))
                    my_dict["Recommended age"] = new_age
                    print("Recommended age is now edited!")
                    archive.edit_game(games, "storedGames")
                    backMenu()

            #Search for games by attributes (finished)
            if choice == 5:
                filter_choice = 0
                print("1. Filter game by one attribute \n2. Filter game by more than one attribute")
                filter_choice = int(input("Choose what to do: "))
                
                if filter_choice == 1:
                    cls()
                    new_choices = 0
                    print("Pick how you want to search for game: \n 1. Search by title \n 2. Search by player count \n 3. Search by time limit \n 4. Search by recommended age")
                    new_choices = int(input("Choose what you want to do: "))

                    if new_choices == 1:
                        title_search = input("Enter title to search for all games with that title: ").lower()
                        print(f"You searched for games with the title: ¬¬¬{title_search}¬¬¬ \nBelow is the result: \n")
                        archive.search(games, "Title", title_search, "storedGames")
                        backMenu()

                    if new_choices == 2:
                        search_pcount = int(input("Enter number of players: "))
                        print(f"You searched for a game with the player count: {search_pcount}\nBelow is the result: \n")
                        archive.search(games,"Player Count", search_pcount, "storedGames")
                        backMenu()

                    if new_choices == 3:
                        time_limit = int(input("Enter time limit number in minutes: "))
                        print(f"You searched for a game with the timit limit of: {time_limit}\nBelow is the result: \n")
                        archive.search(games, "Time Limit", time_limit, "storedGames")
                        backMenu()
            
                    if new_choices == 4:
                        search_age = int(input("Search games by recommended age: "))
                        print(f"You searched for games with recommended age: {search_age}\nBelow is the result: \n")
                        archive.search(games, "Recommended age", search_age, "storedGames")
                        backMenu()

                if filter_choice == 2:
                    cls()
                    title_choice = input("Title? [y/n]").lower()
                    title_choice = "Title"
                    if title_choice == "y":
                        my_key = "Title"
                        my_title = input("Enter title name: ").lower()


                    '''get_choice_title = input("Title? [y/n]").lower()
                    if get_choice_title == "y":
                        get_title = input("Search title: ").lower()
                        title_key = "Title"
                    elif get_choice_title == "n":
                        pass

                    get_choice_playerc = input("Player Count? [y/n]").lower()
                    if get_choice_playerc == "y":
                        get_playerc = int(input("Search player count: "))
                        playerc_key = "Player Count"
                    elif get_choice_playerc == "n":
                        pass

                    get_choice_timelimit = input("Time limit? [y/n]").lower()
                    if get_choice_timelimit == "y":
                        get_timelimit = int(input("Search time limit: "))
                        timelimit_key = "Time Limit"
                    elif get_choice_timelimit == "n":
                        pass

                    get_choice_age = input("Recommended age? [y/n]").lower()
                    if get_choice_age == "y":
                        get_age = int(input("Search recommended age: "))
                        age_key = "Recommended age"
                    elif get_choice_age == "n":
                        pass
                    archive.search_two(games, title_key, playerc_key, get_title, get_playerc, "storedGames")'''

        
            if choice == 6:
                archive.create_json("storedGames")
                print("New file created, old file overwritten. ~")
                backMenu()

            if choice == 7:
                exit()
        except Exception as e:
            print(e)
            print("Wrong input! Go back to menu and try again")
            backMenu()


Game_Archive = Archive("Archive")

menu(Game_Archive)