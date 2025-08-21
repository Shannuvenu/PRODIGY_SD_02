import random
import sys
BANNERS=[
    "🎯 Guessing Game – VENUGADU Edition",
    "🔢 I picked a number. Can you guess it?"
]
LEVELS = {
    "1": ("Easy", 1, 50, 10),    
    "2": ("Medium", 1, 100, 7),
    "3": ("Hard", 1, 500, 9),
}
def pick_level():
    print(BANNERS[0])
    print("Choose Difficulty:\n 1) Easy (1–50, 10 tries)\n 2) Medium (1–100, 7 tries)\n 3) Hard (1–500, 9 tries)")
    choice = input("Enter 1/2/3: ").strip()
    return LEVELS.get(choice, LEVELS["2"])  
def get_int(prompt):
    while True:
        s = input(prompt).strip()
        if s.lower() in ("q", "quit", "exit"):
            print("Bye! 👋")
            sys.exit(0)
        try:
            return int(s)
        except ValueError:
            print("❗ Enter a valid integer (or type 'q' to quit).")
def play_round():
    name, low, high, tries = pick_level()
    secret = random.randint(low, high)
    print(f"\n🧠 Level: {name} | Range: {low}–{high} | Attempts: {tries}")
    print("Type 'q' anytime to quit.\n")
    for attempt in range(1, tries + 1):
        guess = get_int(f"[{attempt}/{tries}] Your guess: ")
        if guess < low or guess > high:
            print(f"🔎 Stay in range {low}–{high}. Try again.")
            continue
        if guess == secret:
            print(f"✅ Correct! You cracked it in {attempt} tries. 🔥")
            return True
        hint = "Higher ↑" if guess < secret else "Lower ↓"
        diff = abs(guess - secret)
        heat = "🔥" if diff <= (high - low) * 0.05 else "🙂" if diff <= (high - low) * 0.15 else "🥶"
        print(f"❌ {hint} | Warmth: {heat}")
    print(f"\n⌛ Out of tries! The number was {secret}. Better luck next time 💪")
    return False
def main():
    print(BANNERS[1])
    wins = 0
    games = 0
    while True:
        won = play_round()
        games += 1
        wins += int(won)
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            break 
    print(f"\n📊 Session Stats → Games: {games} | Wins: {wins}")
    print("Thanks for playing! 🚀")
if __name__ == "__main__":
    main()
