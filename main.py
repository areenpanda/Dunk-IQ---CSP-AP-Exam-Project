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
          # find the guessed player in the list of players to see if the guess was close or not
          for single in list_of_all_players:
              if guess.lower() in single[1].lower():
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

                  # if 3P% is within 0.2
                  if abs(float(single[14]) - float(player[14])) <= 0.2:
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
list_of_all_players = []

for line in data:
      list_of_all_players.append(line)
      # if player is not in list of players
      if line not in list_of_players:
        list_of_all_players.append(line)

  # intro message
print("\n\n\nWelcome to this basketball guessing game!\nAll possible players have a PPG of 15 or higher in the 2021-2022 season. You will be given 4 hints at the start of the game and \n can choose to get one more hint by typing 'hint' instead of a player.\n")
print("\n\n\nSelect difficulty you want this game to be played on. \n\n1. Easy (PTS + REB + AST) \n2. Medium (Above 15 PPG) \n3. Hard (5-15 PPG) \n4. Impossible (Less than 5 PPG) \n\nType the number of the difficulty you want to play on.")
difficulty = int(input("----------------------------------------------------------------------------\n"))

  # iterate through csv
for line in data:
      # pulls out 2021-2022 players
    if difficulty == 1:
      if line[30] == "2021-2022" and float(line[29]) + float(line[24]) + float(line[23]) >= 15:
      # no duplicates
        if line not in list_of_players:
          list_of_players.append(line)
    elif difficulty == 2:
          if line[30] == "2021-2022" and float(line[29]) > 15:
              # no duplicates
              if line not in list_of_players:
                  list_of_players.append(line)    
    elif difficulty == 3:
          if line[30] == "2021-2022" and float(line[29]) <= 15 and float(line[29]) >= 5:
              # no duplicates
              if line not in list_of_players:
                  list_of_players.append(line)

    elif difficulty == 4:
          if line[30] == "2021-2022" and float(line[29]) < 5:
              # no duplicates
              if line not in list_of_players:
                  list_of_players.append(line)
      

      

  # get a random player from the list of players
player = random.choice(list_of_players)

if difficulty == 1:
  print(f"- Position: {player[2]}\n- Age: {player[3]}\n- 3 Point Percentage: {player[13]}\n- Total PPG, APG, & RPG: {player[29]} + {player[24]} + {player[23]}")
elif difficulty == 2:
  print(f"- Position: {player[2]}\n- Age: {player[3]}\n- 3 Point Percentage: {player[13]}\n- Points Per Game: {player[29]}")
elif difficulty == 3:
  print(f"- Position: {player[2]}\n- Age: {player[3]}\n- 3 Point Percentage: {player[13]}\n- Points Per Game: {player[29]}")
elif difficulty == 4:
  print(f"- Position: {player[2]}\n- Age: {player[3]}\n- 3 Point Percentage: {player[13]}\n- Points Per Game: {player[29]}")

else:
  # print("Invalid Input")
  print()


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