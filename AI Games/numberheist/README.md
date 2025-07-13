# 💣 Number Heist+ – Vault Guessing Game (Python)

**Number Heist+** is a fun, terminal-based number guessing game written in Python. Your mission is to crack a **secret vault code** between 1 and 100 within a limited number of attempts, depending on the difficulty level you choose. Each guess gives you feedback on how close you are, using **"Warmer"** or **"Colder"** hints!

---

## 🎮 Game Features

- 🔢 Randomly generated secret number between 1–100
- 🎯 Difficulty levels:
  - 🟢 Easy → 10 attempts
  - 🟡 Medium → 7 attempts
  - 🔴 Hard → 5 attempts
- ♻️ Avoid guessing the same number twice
- 🔥 Warmer/🧊 Colder hints based on guess proximity
- 📜 Displays sorted list of previous guesses
- 🚀 Option to replay after each game

---

## 🧠 How It Works

- The computer selects a **random number between 1 and 100**.
- You choose a **difficulty level** that limits how many guesses you get.
- After each guess:
  - You’re told if it’s **too high** or **too low**.
  - Then, you’ll be told if you’re **getting closer (warmer)** or **further (colder)** than your previous guess.
- The game ends when:
  - You guess the correct number ✅
  - You run out of attempts ❌

---

## ▶️ How to Run

### 1. Make sure Python 3 is installed:

```bash
python --version
