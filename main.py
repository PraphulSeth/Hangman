import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)

lives = 6

display = []
for letter in chosen_word:
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
      print(f"You've already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
      print(f"You guessed {guess},  that's not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
            end_of_game = True
            print("You lose.")
        
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You Win!")
        
    print(stages[lives]) #clever code
