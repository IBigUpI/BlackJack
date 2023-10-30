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
