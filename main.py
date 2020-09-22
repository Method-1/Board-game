from gameClass import Game

my_file = open(r"C:\Users\adiab\gits\Board-game\data\storedGames.txt", "r")
content_list = my_file.readlines()
print(content_list[0])

# Create a menu for the user
while input is not "":
    title = input("Title: ")
    players = int(input("Player count: "))
    playtime = int(input("Time Limit: "))
    age = int(input("Recommended age: "))
    thegame = Game(title,players,playtime,age)
    thegame.save(title, players, playtime, age, "storedGames")
    thegame.read("storedGames")




def choices():
    print("\n Select between following alternatives")