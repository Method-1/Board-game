class Game:
    def __init__(self, title, players, playtime, age):
        self.title = title
        self.players = players
        self.playtime = playtime
        self.age = age



    def save(self, title, players, playtime, age, filename):
        try:
            f = open("Board-game\data"+"\\"+filename+".txt", "a")
            f.write(title + ' = {' + '\n')
            f.write(f'\t"Title": "{title}",' + '\n')
            f.write(f'\t"Player Count": "{players}",' + '\n')
            f.write(f'\t"Time Limit": "{playtime}",' + '\n')
            f.write(f'\t"Recommended age": "{age}"' + '\n}\n\n')
            f.close()
        except Exception as e:
            print(e)

    def read(self, filename):
        try:
            f = open("Board-game\data"+"\\"+filename+".txt", "r")
            lines = f.readlines()
            for x in lines:
                print(x)
                f.close()
        except Exception as e:
            print(e)

    def printGames(self, filename):
        try:
            f = open("Board-game\data"+"\\"+filename+".txt", "r")
            lines = f.readlines()
            for line in lines:
                print(line)
            f.close()
        except Exception as e:
            print(e)

