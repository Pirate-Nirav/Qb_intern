import random
from Stages import stages
word_list = ["python", "banana", "jazz", "keyboard", "oxygen", "wizard", "galaxy",
    "puzzle", "kangaroo", "robot", "mountain", "island", "mystery", "rocket",
    "volcano", "pirate", "ninja", "castle", "dragon", "jungle", "cookie",
    "storm", "shadow", "tornado", "lizard"]
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for letter in chosen_word:
    display += "_"
lives = 6
game_over  = False

guessed_letters = set()

while game_over is not True:
    i = -7 + lives
    print(stages[i])
    print(f"Lives: {lives}")
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another.")
        continue
    if guess not in chosen_word:
        lives -= 1
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess


    print(display)

    if lives == 0:
        game_over = True
        print(stages[0])
        print(f"You lose. The word was: {chosen_word}")
    if not "_" in display:
        game_over = True
        print(f"You win.")
    if game_over:
        break