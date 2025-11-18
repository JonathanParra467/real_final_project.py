"""
Work within your Final Project files.
Add functional code that:
Collects user input for your program’s data (e.g., tasks, menu items, records).
Writes this information to one or more text files.
Uses try/except to handle errors (missing files, bad input).
You may use either append ('a') or write ('w') mode, depending on your design.
Include comments describing how this connects to your project plan.
"""



class Player:
    
    player_details = ("player details: ")

    def __init__(self, first_name, last_name, points):
        # Instance variables
        self.__first_name = first_name
        self.__last_name = last_name
        self.__points = points

    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
        
    def get_points(self):
        return self.__points

    def set_first_name(self, value):
        self.__first_name = value
    
    def set_last_name(self, value):
        self.__last_name = value

    def set_points(self, value):
        self.__points = value

    def print_player_details(self):
        print("player details:", vars(self))
    
    def print_info(self):
        print(self.__first_name)
        print(self.__last_name)
        print(self.__points)

def main():

        player = Player("player", "1", "500 points")
        
        print("Player details: ")
        print(player.get_first_name())
        print(player.get_last_name())
        print(player.get_points())

main()
        
class AI:
    
    ai_details = ("AI details: ")

    def __init__(self, bot_name, dice, points):
        # Instance variables
        self.__bot_name = bot_name
        self.__dice = dice
        self.__points = points

    def get_bot_name(self):
            return self.__bot_name
    
    def get_dice(self):
            return self.__dice
        
    def get_points(self):
            return self.__points

    def set_bot_name(self, value):
            self.__bot_name = value
    
    def set_dice(self, value):
            self.__dice = value

    def set_points(self, value):
            self.__points = value

    def print_player_details(self):
            print("AI details:", vars(self))
    
    def print_info(self):
        print(self.__bot_name)
        print(self.__dice)
        print(self.__points)

def main():

        ai = AI("Botter", "6 sided dice", "500 points")
        
        print("AI details: ")
        print(ai.get_bot_name())
        print(ai.get_dice())
        print(ai.get_points())

main()