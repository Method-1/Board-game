class Game:
    def __init__(self, title, players, playtime, age):
        self.title = title
        self.players = players
        self.playtime = playtime
        self.age = age



    def save(self, title, players, playtime, age, filename):
        try:
            my_dict = {"Title" : title, "Player Count" : players, "Time Limit" : playtime, "Recommended age" : age}
            f = open("data"+"\\"+filename+".txt", "a")
            f.write(str(my_dict))
            f.write("\n")
            f.close()
        except Exception as e:
            print(e)

    def read(self, filename):
        try:
            f = open("data"+"\\"+filename+".txt", "r")
            lines = f.readlines()
            for x in lines:
                print(x)
                f.close()
        except Exception as e:
            print(e)

    def printGames(self, filename):
        try:
            f = open("data"+"\\"+filename+".txt", "r")
            lines = f.readlines()
            for line in lines:
                print(line)
            f.close()
        except Exception as e:
            print(e)

