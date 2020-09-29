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
    
    def menu_alternatives(self):
        print("\n Welcome to the ||Boardgame Archive||")
        print("\n Select between following alternatives:\n 1. Add a game in to the archive \n 2. Print out list of games in archive \n 3. Delete a game from the archive \n 4. Edit a game from the archive \n 5. Search for games with certain attributes \n 6. Create new file that stores games (overwrites the old one) \n 7. Exit")

    def delete_game(self, datalist, filename):
        self.datalist = datalist
        game_list = datalist["Game"]

        y = 0
        for i in game_list:
            print(y,i)
            y += 1
        
        try:
            remove_game = int(input("Choose game you want to remove: "))
            del game_list[remove_game]
            print("The game has been removed!")
        except Exception as e:
            print(e)
            print("Wrong input!")
            
            
        with open("data/"+filename+".json", "w") as pf:
            json.dump(datalist, pf, indent = 4)
    
    def edit_game(self, datalist, filename):
        
        with open("data/"+filename+".json", "w") as pf:
            json.dump(datalist, pf, indent = 4)
        


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
    
    def search(self, datalist, key, value, filename):
        self.datalist = datalist
        game_list = datalist["Game"]
        for item in game_list:
            if item[key] == value:
                print(item)
                


    def search_two(self, datalist, key, value, filename):
        self.datalist = datalist
        game_list = datalist["Game"]
        for item in game_list:
            if item[key] == value:
                print(item)
                