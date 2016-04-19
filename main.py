#Importing csv module for reading soccer_players.csv
import csv


#Three base team placeholders
teams = [[], [], []]
#Email template to be formated with team info later
emailTemp = """Dear {}, \n    Your child was placed on the {} team! They will
    conduct their next practice {}, Hope to see 
    you all there!"""
#Practices for each team    
DragonPrac = 'March 17, at 1pm'
SharkPrac = 'March 17, at 3pm'
RaptorPrac = 'March 18, at 1pm'

#Prints the input team's roster
#couldn't find a way to turn the list varible into a string..
def roster(team):
    if team == Dragons:
        #using a count throw away variable so the teams are numbered
        count = 1
        print('Dragons:')
        for player in team:
            print(count, '. ', player['Name'], '| Experienced? ', player['Soccer Experience'])
            count += 1
    elif team == Sharks:
        count = 1
        print('Sharks:')
        for player in team:
            print(count, '. ', player['Name'], '| Experienced? ', player['Soccer Experience'])
            count += 1
    elif team == Raptors:
        count = 1
        print('Raptors:')
        for player in team:
            print(count, '. ', player['Name'], '| Experienced? ', player['Soccer Experience'])
            count += 1

#usign the email template, creates an email for each player's parents
def email(team):
    for player in team:
        #creates a new file with the player's name
        filename = player['Name'] + "'s Team placement.txt"
        with open(filename, 'a') as txt:
            #formats the email template according to the team
            if team == Dragons:
                txt.write(emailTemp.format(player['Guardian Name(s)'], 'Dragons', DragonPrac))
            elif team == Sharks:
                txt.write(emailTemp.format(player['Guardian Name(s)'], 'Sharks', SharkPrac))
            elif team == Raptors:
                txt.write(emailTemp.format(player['Guardian Name(s)'], 'Raptors', RaptorPrac))

#opens soccer_players.csv and creates the entire_league list of dicts
with open('soccer_players.csv', newline = '') as file:
    data = csv.DictReader(file)
    entire_league = [line for line in data]

#Sorts the league into two lists, experienced players and inexperienced
#couldn't find a way to sort by height without using a lamda
experienced_players = [player for player in entire_league if player["Soccer Experience"] == "YES"]
inexperienced_players = [player for player in entire_league if player["Soccer Experience"] == "NO"]

#uses enumerate to provide even indexed lists
for position, player in enumerate(experienced_players + inexperienced_players):
    teams[position % len(teams)].append(player)
#assigns team variables to the placeholder list teams
Dragons = [team for team in teams[0]]
Sharks = [team for team in teams[1]]
Raptors = [team for team in teams[2]]
#added them to a tuple to make it easy to iterate through them
#I'm sure there is a much easier way to do this
teamTup = (Dragons, Sharks, Raptors)
#calls needed functions based on team
for team in teamTup:
    if team == Dragons:
        roster(team)
        email(team)
    if team == Raptors:
        roster(team)
        email(team)
    if team == Sharks:
        roster(team)
        email(team)