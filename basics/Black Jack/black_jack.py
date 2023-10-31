import bj_players
import calculations

print("Wellcome to Black Jack! \nOne game is 200 points, if you win you get 200 if you hit BlackJack"
      "you get 2x the amount of the game cost")

playing = True


# Tells the players their cards and ask them if they want to get another card.
def player_communication():
    # communicates to the players what cards
    print(f"\nThe Dealers card is:{bj_players.Players.dealer['cards'][0]} and HIDDEN\n")

    for player_id in bj_players.Players.players:
        calculations.remove_points_for_start(player_id=player_id)
        # Communicates to the Players how many points they have
        print(f"{bj_players.Players.players[player_id]['player_name']}, at the moment you have "
              f"{bj_players.Players.players[player_id]['player_points']} points")

        # Tells the player his cards
        print(f"{bj_players.Players.players[player_id]['player_name']}, "
              f"your cards are {' and '.join(bj_players.Players.players[player_id]['player_cards'])} ")

        # Asks the Player if he wants to get another card
        another_card = input("Would you like to hit for another card (y/n)?\n")
        if another_card == "y":
            calculations.deal_one_more_card(p_id=player_id)


while playing:
    bj_players.get_players()
    calculations.assign_cards()
    calculations.check_points()
    player_communication()
