''' Del 1 - Samling över spel
Du väljer själv vilka datastrukturer du vill ha och vilka filer du vill lagra i, men varje spel ska
MINSTA ha följande egenskaper:
1. Titel
2. Antal spelare
3. Tidsåtgång
4. Rekommenderad ålder
Om du själv kommer på något som också vore bra att ha med, så ta med det.
Samlingen ska sparas på fil, så att den finns kvar från gång till gång med programmet. Ni
ska inte skapa en sql-databas, utan använd som sagt olika datastrukturer och lagring på fil '''

# Create a datastructure file (list, dict, tuples etc..) that saves these attributes from input
#1. Titel
#2. Antal spelare
#3. Tidsåtgång
#4. Rekommenderad ålder
# Steg 1: Skapa klass med dessa attributer
# Steg 2: Lagra objekt i valfri datatyp
# Steg 3: Skriv lagrade objekt till txt-fil
'''import json

games = {'Title' : input(''), 'Amount of players' : input(''), 'Playtime' : input(''), 'Recommended Age' : input('')}
json = json.dumps(games)
f = open('games.json', 'w')
f.write(json)
f.close()

print(json)'''
title = input("Title: ")
playerCount = input("Player count: ")
timeLimit = input("Time Limit: ")

f = open("stored.txt", "a")
f.write(title + ' = {' + '\n')
f.write(f'\t"Title": "{title}",' + '\n')
f.write(f'\t"Player Count": "{playerCount}",' + '\n')
f.write(f'\t"Time Limit": "{timeLimit}"' + '\n}\n\n')
f.close()


''' Del 2 - Inmatning
 Vid inmatning av ett nytt spel är det viktigt att validera alla indata, det vill säga, se till att det
som ska vara siffror är siffror. En rekommendation är också att se till att namnet är unikt.
I det här läget rekommenderas du se till att inmatningen görs från
kommandotolken/terminalen, men kom ihåg att skriva modulärt, så att det går att ändra i
framtiden!
Se till att det inskrivna spelet sparas på fil. '''

# Make sure every input is correct. Example: convert number inputs to int. Save user input in file.


'''Del 3 - Lista program
 Programmet ska kunna visa en fullständig lista på alla spel som är inlagda. Den ska läsas in
från fil. '''

# Print list of all games that exist in input-file

'''Del 4 - Redigering av inlagda spel
Programmet ska ha funktioner för att radera och redigera inlagda spel. Gör även det här så
att det fungerar från kommandotolken/terminalen i nuläget. Dock behöver det vara
självförklarande för en användare från första gången programmet används'''

# Create functions that will allow the user to delete and edit existing games (With instructions for user)

'''Del 5 - Filtrering
Användaren ska kunna fylla i en eller flera önskade egenskaper hos ett spel (till exempel
antal spelare och speltid) och då få en lista på enbart de spel som uppfyller dessa kriterier'''

# Create a function that allows the user to search for a game based on it's attributes

'''Del 6 - Utökningar
Om du har kommit så här långt, och gjort det på ett bra sätt, så har du klarat av den
grundläggande uppgiften.
Men för att lära dig mer och öka dina chanser för ett bra betyg så bör du vidareutveckla ditt
program på något vis. Det finns många sätt att göra detta, och du väljer själv vilka du tycker
är rimligt att prioritera. Här är några förslag:
● Gör det möjligt att hantera flera olika personers spelsamlingar
● Låt användaren registrera när ett spel spelats
● Låt användaren sätta betyg på spel, och rangordna den visade listan efter dessa
● Visa spel som bara nästan uppfyller kriterierna, men visa dem sist i listan
Det går förstås också bra att hitta på egna förbättringsmöjligheter.'''

# Create function that allows the user to rate the game and print the list of all games that are rated best.
