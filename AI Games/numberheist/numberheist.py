import random

def get_difficulty():
    print("Choose difficulty level:")
    print("1. 🟢 Easy (10 attempts)")
    print("2. 🟡 Medium (7 attempts)")
    print("3. 🔴 Hard (5 attempts)")
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print("❗ Invalid choice. Please enter 1, 2, or 3.")

def number_heist():
    print("\n💣 Welcome to NUMBER HEIST+ 💣")
    print("Crack the vault code between 1 and 100.\n")

    attempts_left = get_difficulty()
    secret = random.randint(1, 100)
    previous_diff = None
    guessed_numbers = set()

    while attempts_left > 0:
        try:
            guess = int(input(f"\n🔐 Enter your guess ({attempts_left} attempts left): "))
        except ValueError:
            print("❗ Please enter a valid number between 1 and 100.")
            continue

        if not 1 <= guess <= 100:
            print("🚫 Number must be between 1 and 100!")
            continue

        if guess in guessed_numbers:
            print("🔁 You've already tried that number. Try something else.")
            continue

        guessed_numbers.add(guess)

        if guess == secret:
            print("\n🎯 JACKPOT! VAULT UNLOCKED!")
            print(f"✅ The vault code was: {secret}")
            break

        current_diff = abs(secret - guess)
        if previous_diff is None:
            print("📉 Too low!" if guess < secret else "📈 Too high!")
        else:
            if current_diff < previous_diff:
                print("🔥 Getting Warmer!")
            elif current_diff > previous_diff:
                print("🧊 Getting Colder!")
            else:
                print("😐 Same distance...")

        previous_diff = current_diff
        attempts_left -= 1
        print(f"📜 Previous guesses: {sorted(guessed_numbers)}")

    if attempts_left == 0 and guess != secret:
        print("\n💥 HEIST FAILED!")
        print(f"🔒 The vault code was: {secret}")

def play_game():
    while True:
        number_heist()
        again = input("\n🔁 Play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing NUMBER HEIST+!")
            break

# Run the game
if __name__ == "__main__":
    play_game()