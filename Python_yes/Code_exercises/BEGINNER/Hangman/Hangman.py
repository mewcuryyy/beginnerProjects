import random
import hangman_art
import hangman_words

#choose random word from word list
chosen_word = random.choice(hangman_words.word_list)

#creating empty list of blanks
display = []
for letter in chosen_word:
    display.append("_")

guessed_letters = []

#creating variable to track lives
lives = 6

#guessing letters
end_of_game = False

print(hangman_art.logo)
print(' '.join(display))
print(hangman_art.stages[lives])

while not end_of_game:
    if "_" not in display:
        print("You Win!")
        end_of_game = True
    else:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print(f"You've already guessed {guess}.")
            print(' '.join(display))
            print(hangman_art.stages[lives])
        else:
            if guess not in chosen_word:
                lives -= 1
                print(f"You guessed {guess}. That's not in the word. You lose a life.")
                print(' '.join(display))
                print(hangman_art.stages[lives])
                if lives == 0:
                    print(f"You lose, the word was {chosen_word}.")
                    end_of_game = True
            else:
                for i in range(len(chosen_word)):
                    if chosen_word[i] == guess:
                        display[i] = guess
                print(' '.join(display))
                print(hangman_art.stages[lives])
            guessed_letters.append(guess)




