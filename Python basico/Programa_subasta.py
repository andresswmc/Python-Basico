import os
from logo import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"El ganador es {winner} con una oferta de: ${highest_bid}")

while not bidding_finished:
  name = input("Como te llamas?: ")
  price = int(input("Cual es tu oferta?: $"))
  bids[name] = price
  should_continue = input("Hay alguna otra oferta? Escribe 'si' o 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "si":
    os.system('cls')