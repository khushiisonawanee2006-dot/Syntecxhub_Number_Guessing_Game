import random

best_score = None  # Track lowest attempts

while True:
    print("\n--- Number Guessing Game ---")
    print("Choose Difficulty Level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Exit option
    if choice == "4":
        print("Thanks for playing!")
        break

    # Difficulty selection
    elif choice == "1":
        secret = random.randint(1, 10)

    elif choice == "2":
        secret = random.randint(1, 50)

    elif choice == "3":
        secret = random.randint(1, 100)

    else:
        print("Invalid choice! Try again.")
        continue

    attempts = 0

    # Guessing loop
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > secret:
            print("Too high!")

        elif guess < secret:
            print("Too low!")

        else:
            print("Correct! You won in", attempts, "attempts.")

            # Best score update
            if best_score is None or attempts < best_score:
                best_score = attempts
                print("New Best Score:", best_score)
            else:
                print("Best Score:", best_score)

            break

    # Replay option
    replay = input("Do you want to play again? (yes/no): ").lower()

    if replay != "yes":
        print("Thanks for playing!")
        break