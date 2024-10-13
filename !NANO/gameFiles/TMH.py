from game_play import setup_game, play_game

def the_missing_heirloom():
    # Run the game logic
    name = "Detective D!BZY"
    print('This is a text based detective game.\n'
          'You play as the famous detective D!BZY.\n'
          'Tonight is very special.\n'
          'You have been invited to one of the party\'s of the well known baron & baroness Decuard.\n'
          'These party\'s are known for their lavish dinners and amazing live orchestra\'s in the ballroom.\n'
          'Because you know them for a while you can call them by their first names.\n'
          'Mark and Helen have asked for your help in the past.\n'
          'Without you realizing it going into the party, they will need your help again tonight...\n'
          'The Decuard family heirloom has gone missing and it is your job to get to the bottom of this mess.\n')
    player = setup_game(name)
    play_game(player)

if __name__ == "__main__":
    the_missing_heirloom()  # Call the function to start the game
