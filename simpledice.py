import random

def roll():
  min_value = 1
  max_vlaue = 6
  roll = random.randint(min_value, max_vlaue)

  return roll

while True:
  players = input("Eneter the number of players (1-4): ")
  if players.isdigit():
    players = int(players)
    if 1 <= players <= 4:
      break
    else:
      print("Please enter a number between 1 and 4")

max_score = 30
player_scores = [0 for _ in range(players)]

# The game will be stopped when one of the players reaches max_score, and every player have reached their turn.
while max(player_scores) < max_score:
  for player_idx in range(players):
    print("\nPlayer {} total score: {} \n".format(player_idx + 1, player_scores[player_idx]))
    current_score = 0

    while True:
      should_roll = input("Do you want to roll(y)?")
      if should_roll.lower() != "y":
        break

      value = roll()
      if value == 1 :
        current_score = 0;
        print("You rolled a 1, you lose all your points! Your turn is over!")
        break
      else:
        current_score += value
        print("You rolled a {}".format(value))

      print("Your scores is :", current_score)

    player_scores[player_idx] += current_score
    print("Your total score is:", player_scores[player_idx])


max_score = max(player_scores)
winner_idx = player_scores.index(max_score) + 1
print("Player number:", winner_idx, "is the winner with the highest score of :", max_score)











