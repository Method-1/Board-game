class Game:
    def __init__(self, title, players, playtime, age):
        self.title = title
        self.players = players
        self.playtime = playtime
        self.age = age



    def save(self, title, players, playtime, age, filename):
        try:
            import json
            my_dict = {"Title" : title, "Player Count" : players, "Time Limit" : playtime, "Recommended age" : age}
            #my_dict2 = {"Game" : []}
            #my_dict2["Game"].append(my_dict)
            with open("data"+"\\"+filename+".json", "a") as fp:
                json.dump(my_dict, fp, indent=4)
        except Exception as e:
            print(e)



class Archive:
    def __init__(self, title):
        self.title = title
        self.game_list = []
    
    def read(self, filename):
        try:
            import json
            with open("data"+"\\"+filename+".json", "r") as fp:
                data = json.load(fp)
                print(data)

            #f = open("data"+"\\"+filename+".txt", "r")
            #lines = f.readlines()
            #for x in lines:
                #print(x)
                #f.close()
        except Exception as e:
            print(e)

    def add_game(self, title, players, playtime, age):
        new_game = Game(title, players, playtime, age)
        new_game.save(title, players, playtime, age, "storedGames")
        self.game_list.append(new_game)
    
    def gameList(self):
        for game in self.game_list:
            print(f"Title: {game.title}, Player count: {game.players}, Time limit: {game.playtime}, Recommended age: {game.age}")
