import json
#f = open(r'C:\Users\adiab\gits\Board-game\data\storedGames.txt', 'r')
#title = input("Title: ")
#if title in f.read():
    #print("This game already exists, try again!")
#f = open(r'C:\Users\adiab\gits\Board-game\data\storedGames.json', 'r')
#data = f.read()
#print(type(data))

#my_dict = {"Title" : "Monopol", "Player Count" : "5", "Time Limit" : "50", "Recommended age" : "14"}
#dicty2 = {"e" : "f", "g" : "h"}
#dicty3 = {"Game" : []}
#dicty3.append("Bajs"[0])

#dicty3["Game"].append(my_dict)
#print(dicty3["Game"][0]["Title"])
#print(dicty3["Game"][3]["c"])

#dick_dict = dict(dick_list)
#filename = "storedGames"
my_dict = {"Title" : "Monopoly", "Player Count" : 4, "Time Limit" : 40, "Recommended age" : 69}
#my_dict2 = {"Game" : []}
# #my_dict2["Game"].append(my_dict)
with open("data/storedGames.json", "r+") as fp:
    loaded_file = json.load(fp)
    loaded_file["Game"].append(my_dict)
    print(loaded_file)
    
with open("data/storedGames.json", "w") as pf:
    json.dump(loaded_file, pf, indent=4)
    #json.dump(loaded_file, fp, indent=4)
    
