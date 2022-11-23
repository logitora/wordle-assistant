# goes through all of the current, valid words in possible. counts the number of times a certain letter appears in a certain position/index
# we need to make a score system that will favor words with letters that appear the least in a certain position. this will narrow down the list of possible answers/best guesses the most. 
def letter_freq(possible):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    freq = {}
    for c in alphabet:
        letterfreq = [0, 0, 0, 0, 0]
        for i in range(5):
            for word in possible:
                if word[i] == c:
                    letterfreq[i] += 1
        freq.update({c: letterfreq})
    return freq

def word_score(freq, possible):
    max_freq = [0, 0, 0, 0, 0]
    words = {}
    
    # updates max_freq array. this will be the basis of our scoring system, which will measure the difference between a word's letter frequency at a certain index and the max_freq
    """max_freq will record the maximum freq that any letter appears at the specified index. this means that if a specific position is occupied by a certain letter a lot, then the max_freq of that postion will be large. if out of all possible words, that position is occupied by many different letters, then the max_freq for that position will be small"""
    for letter in freq:
        for i in range(5):
            if max_freq[i] < freq[letter][i]:
                max_freq[i] = freq[letter][i]
    
    # assigns a score/rank to each filtered word in possible based on the difference btw max freq of a letter at an index and the word's letter freq at a certain index
    """lower score = better. for a word to have a lower score, the similarity will be maximized. in other words, the lowest scoring word/best word will have the most letters that are close to the max_freq amount. as said above, in order for max_freq to be large in a certain index, it would have to be occupied by a smaller variety of letters. when going through the filtered word options in possible array, we will look for words that contain the most common letters in the specified indeces.
    any information gained on these letters is good information, i.e. if it was wrong, then that will eliminate the most amount of words. if it was yellow, it eliminates the common letter from that index. if it was green, the options narrow down to all words with that letter in that index"""
    for word in possible:
        score = 1
        for i in range(5):
            char = word[i]
            score += (max_freq[i] - freq[char][i])**2
        words.update({word: score})

    return words

def find_best_word(freq, possible):
    """takes the word score and returns the word with the lowest score. this word will be the best next guess"""
    best_score = 1e8
    next = ""
    scores = word_score(freq, possible)
    for word in possible:
        if scores[word] < best_score:
            best_score = scores[word]
            next = word
    return next

def main():
    print(f"____________________________\n\n---Hello, welcome to the Wordle assistant! To start, input your first guess and then indicate the results. \nw = gray/wrong tile | y = yellow tile | g = green tile \nGood first guesses are SALET, SLATE, CRANE, or ADIEU")

    # reads through the valid answers file and appends it to possible. as the user guesses more words and adds more conditions, this list will show all valid guesses that fit the conditions
    possible = []
    correct = {}
    try:
        # using with will ensure the file is closed automatically
        with open("valid answers.txt") as w:
            for word in w:
                possible.append(word.strip())
    except FileNotFoundError:
        print("File not found")

    # get guesses and apply conditions   
    for guesses in range(1, 7):
        guess = input("Word: ").lower()
        result = input("Result: ").lower()
        if result == "ggggg":
            if guesses == 1:
                print(f"This very very insane....They need to check him pc and game.....Maybe he not cheating but maybe he using the game deficit ...and this cant seem on game screen..He needs to check-up....Maybe everyone dont knows him trick.He incredible....I want to ask his where is the comming of your skill's ?")
            else:
                print(f"Well done! The word, {guess.upper()}, was solved in {guesses} turns!")
            break

        # returned possible guess list is in a tuple, since we don't need it to be mutable. can only iterate through immutable list -- tuple 
        possible_guess = tuple(possible)

        # keeps track of any green tiles and where in the word they show up
        for i in range(5):
            if result[i] == "g":
                if guess[i] not in correct:
                    correct[guess[i]] = [i]
                else:
                    correct[guess[i]].append(i)

        for word in possible_guess:
            for i in range(5):
                if result[i] == "g" and guess[i] != word[i]:
                    possible.remove(word)
                    break
                elif result[i] == "y" and guess[i] not in word:
                    possible.remove(word)
                    break
                elif result[i] == "y" and guess[i] == word[i]:
                    possible.remove(word)
                    break
                elif result[i] == "w" and guess[i] in word:     # handles the situation where a word has the same letter as gray and green
                    if guess[i] not in correct:                 # ex: answer = PRIME and our guess is PENCE. this will look through our options and keep the words with E at pos 4
                        possible.remove(word)                   # wheras before it would just throw it out since E @ pos 1 would cause words with E to be removed, leading to 0
                        break                                   # suggested words.
                    else:
                        for pos in correct[guess[i]]:
                            if word[pos] == guess[i]:
                                continue

        suggest = find_best_word(letter_freq(possible), possible)
        
        amount = len(possible)
        
        # TODO implement a measure to give each word to "rank" them on the best next guess. the best 4 will be printed as suggested guesses

        # for each guess, show info about which round, how many the list got narrowed down to, the <=4 best possible guesses, the guessed word, and then the result shown in emojis 🟩 🟨 ⬛
        print(f"____________________________\n\n---Guess {guesses+1} \n Remaining words = {amount}")

        for c in result:
            if c == "g":
                print("🟩", end="")
            elif c == "y":
                print("🟨", end="")
            elif c == "w":
                print("⬛", end="") 

        print(f"\nSuggested guess = {suggest.upper()}")

if __name__ == "__main__":
    main()