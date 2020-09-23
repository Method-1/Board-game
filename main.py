from gameClass import Game, Archive

#my_file = open(r"C:\Users\adiab\gits\Board-game\data\storedGames.txt", "r")
#content_list = my_file.readlines()
#print(content_list)

def choices():
    print("\n Select between following alternatives: \n 1. Add a game in to the archive \n 2. Print out list of games in archive \n 3. Delete a game from the archive \n 4. Edit a game from the archive \n 5. Search for a game \n 6. Exit ")
# Create a menu for the user
def menu(archive):
    choices()
    choice = 0
    while choice is not 7:
        choice = int(input("Choose one of the alternatives to proceed >: "))
        #f = open(r'C:\Users\adiab\gits\Board-game\data\storedGames.txt', 'r')
        if choice == 1:
            title = input("Title: ")
            players = int(input("Player count: "))
            playtime = int(input("Time Limit: "))
            age = int(input("Recommended age: "))
            archive.add_game(title, players, playtime, age)
        if choice == 2:
            archive.read("storedGames")

        #thegame = Game(title,players,playtime,age)
        #thegame.save(title, players, playtime, age, "storedGames")
        #thegame.read("storedGames")


Game_Archive = Archive("Archive")

menu(Game_Archive)