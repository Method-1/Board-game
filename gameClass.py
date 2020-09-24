import json

class Game:
    def __init__(self, title, players, playtime, age):
        self.title = title
        self.players = players
        self.playtime = playtime
        self.age = age



    def save(self, title, players, playtime, age, filename):
        try:
            my_dict = {"Title" : title, "Player Count" : players, "Time Limit" : playtime, "Recommended age" : age}
            with open("data/"+filename+".json", "r+") as fp:
                loaded_file = json.load(fp)
                loaded_file["Game"].append(my_dict)

            with open("data/"+filename+".json", "w") as pf:
                json.dump(loaded_file, pf, indent = 4)
        except Exception as e:
            print(e)



class Archive:
    def __init__(self, title):
        self.title = title
        self.game_list = []
    
    def printGames(self, filename):
        try:
            
            with open("data/"+filename+".json", "r") as fp:
                data = json.load(fp)
                print(data)

        except Exception as e:
            print(e)

    def add_game(self, title, players, playtime, age):
        new_game = Game(title, players, playtime, age)
        new_game.save(title, players, playtime, age, "storedGames")
        self.game_list.append(new_game)

    def create_json(self, filename):
        
        my_dict = {"Game" : []}
        with open("data/"+filename+".json", "w") as fp:
                json.dump(my_dict, fp, indent=4)

        
    def read(self, filename):
        try:
            with open("data/"+filename+".json", "r") as fp:
                data = json.load(fp)
                return data
        except Exception as e:
            print(e)