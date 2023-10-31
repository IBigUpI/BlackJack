import bj_players
import cards


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


# Deal one more card to the Player
def deal_one_more_card(p_id):
    card = cards.get_random_card()
    new_card_value = cards.get_card_value(card)
    bj_players.Players.players[p_id]['player_cards'] += [card]
    bj_players.Players.players[p_id]['player_card_value'] += new_card_value
    print(bj_players.Players.players)


# Check how many points Players have and set min points to false when min_points are less than min required
def check_points():
    for p_id in bj_players.Players.players:
        points = bj_players.Players.players[p_id]['player_points']
        if points < 200:
            bj_players.Players.players[p_id]['min_points'] = False


# Remove points equal to the game cost
def remove_points_for_start(player_id):
    if bj_players.Players.players[player_id]['min_points']:
        bj_players.Players.players[player_id]['player_points'] -= 200


# calculate if the player wins or the dealer
def calculate_winner(player_id):
    player_value = bj_players.Players.players[player_id]['player_card_value']
    dealer_value = bj_players.Players.dealer['card_points']
    if dealer_value < 17:
        bj_players.Players.dealer['cards'] += cards.get_random_card()
        for card in bj_players.Players.dealer['cards']:
            bj_players.Players.dealer['card_points'] += (cards.get_card_value(card))
            dealer_value = bj_players.Players.dealer['card_points']
            if dealer_value > 21:
                bj_players.Players.players['winning_status'] = True
    if player_value > 21:
        bj_players.Players.players['winning_status'] = False
    elif player_value > dealer_value:
        bj_players.Players.players['winning_status'] = True
    elif player_value < dealer_value:
        bj_players.Players.players['winning_status'] = False
    elif player_value == dealer_value:
        bj_players.Players.players['draw'] = True
