# Class wit the Player and Dealer dictionaries
class Players:
    players = {

    }

    dealer = {
        'cards': [],
        'card_points': 0,
    }


# This function adds the Players to the Players dictionary for further use.
def create_player(player_id, name, points, cards, card_value, ):
    Players.players[player_id] = dict(player_name=name,
                                      player_points=points,
                                      player_cards=[cards],
                                      player_card_value=card_value,
                                      min_points=True,
                                      winning_status='',
                                      draw=False
                                      )


# Gets from the user the amount and names of the players.
def get_players():
    more_players = True
    p_id = 1
    while more_players:
        get_player_name = input("What is your Name?\n")
        create_player(player_id=p_id, name=get_player_name, points=2600, cards='', card_value=0, )
        print(f"Welcome to the game {Players.players[p_id]['player_name']},"
              f" you start with {Players.players[p_id]['player_points']} points.")

        p_id += 1
        if input("Are there more players? (y/n)\n") != "y":
            more_players = False
