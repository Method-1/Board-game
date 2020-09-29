import json
#f = open(r'C:\Users\adiab\gits\Board-game\data\storedGames.txt', 'r')
#title = input("Title: ")
#if title in f.read():
    #print("This game already exists, try again!")
#f = open(r'C:\Users\adiab\gits\Board-game\data\storedGames.json', 'r')
#data = f.read()
#print(type(data))
#age = int(input("age: "))
#players = int(input("Players: "))
my_dict = {"Title" : "Höps", "Player Count" : 5, "Time Limit" : "50", "Recommended age" : 42}
my_dict2 = {"Title": "Monopoly", "Player Count" : 10, "Time Limit" : "60", "Recommended age" : 12}
my_dict3 = {"Title": "Jumanji", "Player Count" : 2, "Time Limit" : "60", "Recommended age" : 14}
my_dict4 = {"Title": "Fia med knuff", "Player Count" : 5, "Time Limit" : "60", "Recommended age" : 14}
#dicty2 = {"e" : "f", "g" : "h"}
dicty3 = {"Game" : []}
#dicty3.append("Bajs"[0])

dicty3["Game"].append(my_dict)
dicty3["Game"].append(my_dict2)
dicty3["Game"].append(my_dict3)
dicty3["Game"].append(my_dict4)
my_list = dicty3["Game"]
#print(my_list)
#dic = dicty3["Game"]
rec_age = input(": ")
pc = input(": ")
age_val = int(input(": "))
pc_val = int(input(": "))
example = my_list
values = [age_val]
result = [d for d in example if d[rec_age] in values]

values2 = [pc_val]
result2 = [d for d in result if d[pc] in values2]
print(result2)

#dic2 = []
#for item in dic:
    #if item["Recommended age"] == age:
        #x = item
        #dic2.append(x)
        #print(dic2)
#for item in dic2:
    #if item["Player Count"] == players:
        #print(item)
        #for x in item:
            #print(x["Title"])
    #print (item["Title"])
#print(dicty3["Game"][0].values())
#print(dicty3["Game"][3]["c"])

#dick_dict = dict(dick_list)
#filename = "storedGames"
#my_dict = {"Title" : "Monopoly", "Player Count" : 4, "Time Limit" : 40, "Recommended age" : 69}
#my_dict2 = {"Game" : []}
# #my_dict2["Game"].append(my_dict)
'''with open("data/storedGames.json", "r+") as fp:
    loaded_file = json.load(fp)
    loaded_file["Game"].append(my_dict)
    print(loaded_file)
    
with open("data/storedGames.json", "w") as pf:
    json.dump(loaded_file, pf, indent=4)
     #json.dump(loaded_file, fp, indent=4)'''
    
