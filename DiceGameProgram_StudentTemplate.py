"""
Shashank Reddy
3/31/23

This program...
"""
from DiceGameClasses import Die
from DiceGameClasses import player
from DiceGameClasses import HighTwoGame

#example of play one game
print("Game one:")
game1 = HighTwoGame("Matt", "Ashley")
print(game1.playOneGame())

#example of play many games
print("")
print("Game two:")
game2 = HighTwoGame("Dexter", "Eugene")
print(game2.playManyGames(3))

