import csv
import random

# check if guess was right
def check(guess):
    # get variables
    global correct
    global list_of_players
    global player
    global guesses

    # check if guess = the player
    if guess.lower() in player[1].lower():
        print("You got it!")
        # set correct = true so while loop will end
        correct = True
    # if guess is wrong
    else:
        print("---------- Wrong ----------")
        # find the guessed player in the list of players to see if the guess was close 
        for single in list_of_players:
            if guess.lower() in single[1].lower():

                if abs(float(single[3]) - float(player[3])) <= 3:

                # if age is within 3 years
                  if abs(float(single[3]) - float(player[3])) <= 3:

                    print("Age: Close")
                else:
                    print("Age: Far")

                # if PPG is within 3 points
                    if abs(float(single[29]) - float(player[29])) <= 3:
                      print("Points Per Game: Close")
                    else:
                      print("Points Per Game: Far")
                  # If 3pt% is within 20%
                    if abs(float(single[13]) - float(player[13])) <= 0.2:
                      print("3 Point Percentage: Close")
                    else:
                      print("3 Point Percentage: Far")

        print()
        print(f"Remaining Guesses: {guesses}")
        print("---------------------------")

# hint: what team the player plays on
def get_hint():
    global player
    print()
    print("---------- HINT! ----------")
    print(f"Team: {player[4]}")
    print("---------------------------")
    print()

# open csv file
file = open("NBA_Player_Stats.csv", "r")
# read csv file
data = list(csv.reader(file, delimiter=","))

# list to hold players info
list_of_players = []

# # get a random player from the list of players
# player = random.choice(list_of_players)

# intro message
print("\n\n\nWelcome to this basketball guessing game!\nAll possible players have a PPG of 15 or higher in the 2021-2022 season. You will be given 4 hints at the start of the game and can \nchoose to get one more hint by typing 'hint' instead of a player. \nClick enter to start.")
input("----------------------------------------------------------------------------\n")
print("\n\n\nSelect difficulty you want this game to be played on. \n\n1. Easy (over 15 ppg) \n2. Medium (5-15 ppg) \n3. Hard (total ppg, rpg, and apg) \n\nType the number of the difficulty you want to play on.")
n = int(input("----------------------------------------------------------------------------\n"))
# Clear the previously added players before refilling the list
list_of_players.clear()
# Check if list_of_players is not empty before selecting a random player
if list_of_players:
    player = random.choice(list_of_players)
else:
#No one found in the list
# Sort player list being out of range
    player = []
    for i in range(len(player)):
      if i == 1:
          player.pop(0)
      print(player[i])
  # Clear the previously added players before refilling the list
list_of_players.clear()
  # Iterate through the data and add players based on the selected difficulty level criteria
for line in data:
      if n == 1 and line[30] == "2021-2022" and float(line[29]) >= 15:
          list_of_players.append(line)
          print(f"- Position: {player[2]}\n- Age: {player[3]}\n- 3 Point Percentage: {player[13]}\n- Points Per Game: {player[29]}")
          if line not in list_of_players:
          list_of_players.append(line)
      elif n == 2 and line[30] == "2021-2022" and 5 <= float(line[29]) <= 15:
          print(f"- Position: {player[2]}\n- Age: {player[3]}\n- 3 Point Percentage: {player[13]}\n- Points Per Game: {player[29]}")
          list_of_players.append(line)
      elif n == 3 and line[30] == "2021-2022" and (float(line[29]) + float(line[24]) + float(line[23])) >= 25:
          list_of_players.append(line)
          print(f"- Position: {player[2]}\n- Age: {player[3]}\n- 3 Point Percentage: {player[13]}\n- Total PPG, APG, & RPG: {player[29]} + {player[24]} + {player[23]}")
          list_of_players.append(line)
  # Check if players are available for the selected difficulty level
if list_of_players:
      player = random.choice(list_of_players)
else:
      print("No players found for the selected difficulty level. Please check the data.")
      player = []  # Assign a default value or empty list to handle no player found scenario  
            
                


# # intro message
# print("\n\n\nWelcome to this basketball guessing game!\nAll possible players have a PPG of 15 or higher in the 2021-2022 season. You will be given 4 hints at the start of the game and can \nchoose to get one more hint by typing 'hint' instead of a player. \nClick enter to start.")
# input("----------------------------------------------------------------------------\n")
# print("\n\n\nSelect difficulty you want this game to be played on. \n\n1. Easy (over 15 ppg) \n2. Medium (5-15 ppg) \n3. Hard (total ppg, rpg, and apg) \n\nType the number of the difficulty you want to play on.")
# n = int(input("----------------------------------------------------------------------------\n"))
# if n == 1:
#     print("You chose Easy difficulty.")
#     print(f"- Position: {player[2]}\n- Age: {player[3]}\n- 3 Point Percentage: {player[13]}\n- Points Per Game: {player[29]}")
# elif n == 2:
#     print("You chose Medium difficulty.")
#     print(f"- Position: {player[2]}\n- Age: {player[3]}\n- 3 Point Percentage: {player[13]}\n- Points Per Game: {player[29]}")
# elif n == 3:
#     print("You chose Hard difficulty.")
# else:
#     print("Invalid input. Please choose 1, 2, or 3 for difficulty.")
# print(f"- Position: {player[2]}\n- Age: {player[3]}\n- 3 Point Percentage: {player[13]}\n- Points Per Game: {player[29]}")



  

# set variables
guesses = 4
correct = False
hint = False

# loop "Guess a player:" until no more guesses or they get the answer right
while guesses >= 0 and correct == False:
    guess = input("Guess a player: ")

    # if they want a hint
    if guess == "hint":
        if hint == False:
            get_hint()
            hint = True
        else:
            print("You already used your extra hint!\n")
    else:
        check(guess)
    # use a guess
    guesses = guesses - 1

# if they run out of guesses
if correct == False:
    print(f"---------- Game Over! ----------\nThe answer was {player[1]}")