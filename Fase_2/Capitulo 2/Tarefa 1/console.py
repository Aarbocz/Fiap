# Number of team members
MEMBERS = 5

# Set votes count
playstation = 0
xbox = 0
nintendo = 0

# Get vote for each member
for member in range(MEMBERS):
    vote = input("VOTE(playstation, xbox or nintendo): ").lower()

    if vote == "playstation":
        playstation += 1
    elif vote == "xbox":
        xbox += 1
    elif vote == "nintendo":
        nintendo += 1
    else:
        print("Invalid vote")

# Check winner
if playstation > xbox and playstation > nintendo:
    print(f"Winner Playstation with {playstation} votes.")
elif xbox > playstation and xbox > nintendo:
    print(f"Winner Xbox with {xbox} votes.")
elif nintendo > playstation and nintendo > xbox:
    print(f"Winner Nintendo with {nintendo} votes.")
else:
    print("Tie")