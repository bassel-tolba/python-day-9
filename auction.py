pids = {}
import art
print(art.logo)
answer = "yes"
while answer == "yes":
    name = input("what is your name ?: ")
    bide = int(input("what is your bid ?: "))
    pids[name] = bide
    answer = input("do anyone else want to bid ?")

lowest_bid = 0
for bid in pids:
    if pids[bid] > int(lowest_bid):
        lowest_bid = pids[bid]

for key, value in pids.items():
    if value == lowest_bid:
        winner = key
    
print(f"the winner is {winner} with a bid of {lowest_bid}")