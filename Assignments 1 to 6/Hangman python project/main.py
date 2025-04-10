import random

#Word List
words = ["python","programming","hangman","computer","development"]

# choose a random word
secret_word =random.choice(words)
guessed_words= ["_"] * len(secret_word)
attempts = 6
guessed_letters =[]


#INtroduction
print("Welcome to the Hangman Game.")
print("Guess the secret word letter by letter.")
print(f"The word has {len(secret_word)} letters.")
print("You have 6 chances. Good Luck\n")


while attempts > 0:
    # Display current progress
    print("word:","".join(guessed_letters))
    print(f"Guessed letters:{','.join(guessed_letters)}")

    #User INput
    guess =input("Guess'a letter:").lower()


     #input validation
    if len(guess) !=1 or  not guess.isalpha():
       print("invalid input! Please enter a single letter.\n")
       continue

 
     #check is the letter already guesssed
    if guess in guessed_letters:
        print("You already guessed that letter! Try again.\n")
        continue
    
    # Add the guessed letter to the list
    guessed_letters.append(guess)


      # Check the guessed letter is in the secret word
    if guess in secret_word:
      print(f"Good Job! {guess} is in the words.\n")
      for i in range(len(secret_word)):
         if secret_word[i] == guess:
            guessed_words[i]=guess

    else:
       print(f"Oops! {guess} in not in the word.\n")
       attempts-=1

       #Check is teh user has guessed  the word
       if "_" not in guessed_words:
          print("Congartulations! you guessed the word:", secret_word)
          break
       
       # If the user runs out of attempts
       if attempts ==0:
          print("Guess over! you run out of the attempts.")
          print(f"The secret word was: {secret_word}")






      
        
