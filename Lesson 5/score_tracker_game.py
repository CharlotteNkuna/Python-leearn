# High Score Tracker Game

while True:

    score = input("Enter your game score (or type 'stop' to exit): ")

    # Check if the user wants to stop
    if score.strip().lower() == "stop":
        print("Game session ended!")
        break

    # Convert the input to a number
    score = int(score)

    # Check if it is a high score
    if score > 100:
        print("Wow! That's a new high score!")
    else:
        print("Good try, keep playing!")