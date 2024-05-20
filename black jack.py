# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:53:00 2024

@author: smaug
"""

import random

# Define a single deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
single_deck = [(rank, suit) for suit in suits for rank in ranks]

# Function to create a multi-deck shoe
def create_shoe(num_decks):
    return single_deck * num_decks

# Shuffle the shoe
def shuffle_shoe(shoe):
    random.shuffle(shoe)
    return shoe
# Function to evaluate the value of a hand
def hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank, _ = card
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            aces += 1
            value += 11
        else:
            value += int(rank)
    
    # Adjust for aces
    while value > 21 and aces:
        value -= 10
        aces -= 1
    
    return value

# Function to check for blackjack
def is_blackjack(hand):
    return hand_value(hand) == 21 and len(hand) == 2
# Function to deal a card
def deal_card(shoe):
    return shoe.pop()

# Function to deal initial hands
def deal_initial_hands(shoe):
    player_hand = [deal_card(shoe), deal_card(shoe)]
    dealer_hand = [deal_card(shoe), deal_card(shoe)]
    return player_hand, dealer_hand
# Player action to hit
def player_hit(player_hand, shoe):
    player_hand.append(deal_card(shoe))

# Dealer action to hit
def dealer_hit(dealer_hand, shoe):
    dealer_hand.append(deal_card(shoe))
# Main game logic
def play_blackjack(num_decks):
    shoe = create_shoe(num_decks)
    shuffle_shoe(shoe)
    
    player_hand, dealer_hand = deal_initial_hands(shoe)
    
    print(f"Dealer's hand: {dealer_hand[0]} and [Hidden]")
    print(f"Player's hand: {player_hand} with value {hand_value(player_hand)}")
    
    # Player's turn
    while True:
        action = input("Do you want to hit or stand? (h/s): ").strip().lower()
        if action == 'h':
            player_hit(player_hand, shoe)
            print(f"Player's hand: {player_hand} with value {hand_value(player_hand)}")
            if hand_value(player_hand) > 21:
                print("Player busts! Dealer wins.")
                return
        elif action == 's':
            break
        else:
            print("Invalid action. Please choose 'h' to hit or 's' to stand.")
    
    # Dealer's turn
    print(f"Dealer's hand: {dealer_hand} with value {hand_value(dealer_hand)}")
    while hand_value(dealer_hand) < 17:
        dealer_hit(dealer_hand, shoe)
        print(f"Dealer's hand: {dealer_hand} with value {hand_value(dealer_hand)}")
        if hand_value(dealer_hand) > 21:
            print("Dealer busts! Player wins.")
            return
    
    # Determine the winner
    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)
    
    if player_value > dealer_value:
        print("Player wins!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")
        
        
  # Run the game with 6 decks
play_blackjack(6)
      
