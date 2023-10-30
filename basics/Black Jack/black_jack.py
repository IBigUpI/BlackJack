import cards
import bj_players

print("Wellcome to Black Jack!")

playing = True


# Deal first round of cards
def assign_cards():
    # Deal the cards to the Players
    for player_id in bj_players.Players.players:
        bj_players.Players.players[player_id]['player_cards'] = [cards.get_random_card(), cards.get_random_card()]
        for p_cards in bj_players.Players.players[player_id]['player_cards']:
            bj_players.Players.players[player_id]['player_card_value'] += (cards.get_card_value(p_cards))

    # Deal the cards to the Dealer
    bj_players.Players.dealer['cards'] = [cards.get_random_card(), cards.get_random_card()]
    for dealer in bj_players.Players.dealer['cards']:
        bj_players.Players.dealer['card_points'] += (cards.get_card_value(dealer))


# Tells the players their cards and ask them if they want to get another card.
def player_communication():
    for player_id in bj_players.Players.players:
        print(f"{bj_players.Players.players[player_id]['player_name']}, you have "
              f"{bj_players.Players.players[player_id]['player_points']} points, ")


while playing:
    bj_players.get_players()
    assign_cards()
    player_communication()
