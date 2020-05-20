import constants
import copy
import random

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)

experienced = []
inexperienced = []

panthers = []
bandits = []
warriors = []


def clean_player_data():
    for player in players:
        player['height'] = int(player['height'][:2])
        player['guardians'] = player['guardians'].split(" and ")
        if player['experience'].lower() == "yes":
            player['experience'] = True
            experienced.append(player)
        else:
            player['experience'] = False
            inexperienced.append(player)


def balance_teams(team):
    while len(experienced) != 0 and len(team) < 3:
        team.append(experienced.pop(random.randrange(len(experienced))))

    while len(inexperienced) != 0 and len(team) < 6:
        team.append(inexperienced.pop(random.randrange(len(inexperienced))))


def player_names(team):
    my_players = []
    for player in team:
        my_players.append(player['name'])
    print(', '.join(my_players))


def player_experience(team):
    exp_players = 0
    no_exp = 0
    for player in team:
        if player['experience']:
            exp_players += 1
        else:
            no_exp += 1
    print('Total experienced: ' + str(exp_players))
    print('Total inexperienced: ' + str(no_exp))


def player_guardians(team):
    guardians = []
    for player in team:
        guardians.extend(player['guardians'])
    print(", ".join(guardians))


def player_height(team):
    total = 0
    for player in team:
        total += player['height']
    avg_height = round(total / len(team))
    print('Average height: ' + str(avg_height))


def total_players(team):
    teammates = len(team)
    print('Total players: ' + str(teammates))


def start():
    print('\nBASKETBALL TEAM STATS TOOL')
    print('\n------ MENU ------')
    while True:
        try:
            user_choice = int(input('\nPlease Choose:\n1: Display Team Stats\n2: Quit\n\nEnter an option: '))
        except ValueError:
            print('Oops! Looks like you did not enter a number.')
            continue
        if user_choice == 2:
            print('Thank you, have a great day!')
            break
        elif user_choice == 1:
            while True:
                try:
                    user_pick = int(
                        input(
                            '\nSelect a team below to see stats, or select option 4 to quit:\n1. Panthers\n2. Bandits\n3. Warriors\n4. Quit\n\nTeam Selection: '))
                    if user_pick == 4:
                        print("Thanks, and have a great day!!")
                        quit()
                except ValueError:
                    print('Oops! Looks like you did not enter a number.')
                    continue
                pick = True
                while pick:
                    if user_pick == 1:
                        print('Team: Panthers Stats\n----------')
                        total_players(panthers)
                        player_experience(panthers)
                        player_height(panthers)
                        print('Guardians:')
                        player_guardians(panthers)
                        print('Players on Team:')
                        player_names(panthers)
                        pick = False

                    elif user_pick == 2:
                        print('Team: Bandits Stats\n----------')
                        total_players(bandits)
                        player_experience(bandits)
                        player_height(bandits)
                        print('Guardians:')
                        player_guardians(bandits)
                        print('Players on Team:')
                        player_names(bandits)
                        pick = False

                    elif user_pick == 3:
                        print('Team: Warriors Stats\n----------')
                        total_players(warriors)
                        player_experience(warriors)
                        player_height(warriors)
                        print('Guardians:')
                        player_guardians(warriors)
                        print('Players on Team:')
                        player_names(warriors)
                        pick = False
                    else:
                        user_pick = int(input(
                            "Oops, looks like you didn't select one of the teams.\nSelect a team below to see stats:\n1. "
                            "Panthers\n2. Bandits\n3. Warriors\n\nTeam Selection: "))
        else:
            print("Please select option 1 or 2.")


def main_function():
    clean_player_data()
    balance_teams(panthers)
    balance_teams(bandits)
    balance_teams(warriors)
    start()


if __name__ == '__main__':
    main_function()
