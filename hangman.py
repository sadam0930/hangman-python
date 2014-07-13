import string
import random

#this hangman game randomly guesses and plays by itself
#this version of hangman uses a random word from the file in 'pg244.txt'
with open('pg244.txt', 'r') as f:
	data = f.read()

end_of_header = data.find('*** START')
start_of_footer = data.find('*** END')

book = data[end_of_header:start_of_footer]
book_stripped = book.translate(string.maketrans("", ""), string.punctuation).lower()
book_split = book_stripped.split()

#to play with a different set of words, replace book_split with a list of different words
word = random.choice(book_split)
game_word = list(word)
visibleWord = []
word_length = len(game_word)
correct_guesses = 0
endGame = False
numChanches = 25
guesses = []

for i in range(word_length):
	visibleWord.append('_')

while(not endGame):
	numGuesses = len(guesses)
	
	newGuess = False
	while(not newGuess):
		print 'Guess a word: '
		#choice can be configured to take a user input instead
		choice = random.choice(string.ascii_lowercase)
		print choice
		if choice in guesses:
			print "You already guessed that. Try again"
		else:
			newGuess = True
			guesses.append(choice)
			
	
	if choice in visibleWord:
		continue
	elif choice in game_word:
		correct_guesses += 1
		visibleWord[game_word.index(choice)] = choice
		print visibleWord
	
	if numGuesses == numChanches:
		print "You ran out of guesses! You Lose!"
		print "The word was: " + word
		endGame = True
	elif correct_guesses == word_length:
		print "Congratulations! You've won!"
		print "{} {}".format("Number of guesses: ", numGuesses)
		endGame = True
	
		
