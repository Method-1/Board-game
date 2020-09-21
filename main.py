from gameClass import Game

# Create a menu for the user
while input is not "":
    title = input("Title: ")
    players = int(input("Player count: "))
    playtime = int(input("Time Limit: "))
    age = int(input("Recommended age: "))
    thegame = Game(title,players,playtime,age)
    thegame.save(title, players, playtime, age, "storedGames")
    

