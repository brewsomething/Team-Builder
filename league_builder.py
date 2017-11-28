import csv
import random

# add experienced player to team roster if space available on team
def player_distribution(team1, team2, team3):

    #   if player is experienced AND there is room on the team, add to the team
    if player['Soccer Experience'] == 'YES' and team1[2] < exp_count:
        team1[1].append(player)
        team1[2] += 1
    elif player['Soccer Experience'] == 'YES' and team2[2] < exp_count:
        team2[1].append(player)
        team2[2] += 1
    elif player['Soccer Experience'] == 'YES' and team3[2] < exp_count:
        team3[1].append(player)
        team3[2] += 1

    #   if player is not experienced AND there is room on the team, add to the team
    elif player['Soccer Experience'] == 'NO' and team1[3] < noexp_count:
        team1[1].append(player)
        team1[3] += 1
    elif player['Soccer Experience'] == 'NO' and team2[3] < noexp_count:
        team2[1].append(player)
        team2[3] += 1
    elif player['Soccer Experience'] == 'NO' and team3[3] < noexp_count:
        team3[1].append(player)
        team3[3] += 1

# write text file with team name and player info for each team
def teams_list(team):
    with open('teams.txt', 'a') as file:
        file.write(team[0]+'\n')
        for row in team[1]:
            file.write(str(row['Name'])+', '+row['Soccer Experience']+', '+row['Guardian Name(s)'] + '\n')
        file.write('\n')

# write letters to guardians
def letters_to_guardians(team):
    for player in team[1]:
        with open('letters/{}.txt'.format(player['Name']), 'a') as file:
            file.write("Dear {},\n\nWe are excited to inform you that {} will be playing for the {} this year! The first practice will be on Wednesday, February 7, 2018 at 4:30PM. The location of this practice will be sent out at a later date. Please feel free to contact us with any questions.\n\nThank you,\n\nThe Management\n".format(player['Guardian Name(s)'], player['Name'], team[0]))


if __name__ == '__main__':

    teams = 3

    # lists to count total number of experience and non-experienced players
    exp_players = []
    non_exp_players = []

    # team info as list for three teams - [team name, players (list of dicts), experienced players count, non-experienced players count)]
    team1 = ['Dragons', [], 0, 0]
    team2 = ['Sharks', [], 0, 0]
    team3 = ['Raptors', [], 0, 0]

    # read the data from the supplied CSV file. Store that data in an appropriate data type
    with open('data/soccer_players.csv', newline='') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        player_list = list(player_reader)

    # separate player list into categories for counting experienced & non-experienced players
    for row in player_list:
        if row['Soccer Experience'] == 'YES':
            exp_players.append(row)
        else:
            non_exp_players.append(row)

    # determine total experienced players per team
    exp_count = len(exp_players)/teams
    # determine total non-experienced players per team
    noexp_count = len(non_exp_players)/teams

    # randomize player list
    rand_player_list = random.sample(player_list, len(player_list))

    # iterate through all players in list
    for player in rand_player_list:

        # add players to teams
        player_distribution(team1, team2, team3)

    # write team info to teams.txt
    teams_list(team1)
    teams_list(team2)
    teams_list(team3)

    # write letters to team members' guardians
    letters_to_guardians(team1)
    letters_to_guardians(team2)
    letters_to_guardians(team3)
