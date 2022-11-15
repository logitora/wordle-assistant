def main():
    print(f"____________________________\n\n---Hello, welcome to the Wordle assistant! To start, input your first guess and then indicate the results. \nw = gray/wrong tile | y = yellow tile | g = green tile \nGood first guesses are SALET, SLATE, CRANE, or ADIEU")

    # reads through the valid answers file and appends it to possible. as the user guesses more words and adds more conditions, this list will show all valid guesses that fit the conditions
    possible = []
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
                print(f"Well done! The word, {guess}, was solved in {guesses} turn!")
            break
        
        # returned possible guess list is in a tuple, since we don't need it to be mutable. can only iterate through immutable list -- tuple 
        possible_guess = tuple(possible)
        # iterates through every word and removes words based on the conditions given in result
        for word in possible_guess:
            for i in range(5):
                if result[i] == "w" and guess[i] in word:
                    possible.remove(word)
                    break
                elif result[i] == "y" and guess[i] not in word:
                    possible.remove(word)
                    break
                elif result[i] == "y" and guess[i] == word[i]:
                    possible.remove(word)
                    break
                elif result[i] == "g" and guess[i] != word[i]:
                    possible.remove(word)
                    break
        
        amount = count(possible_guess)
        
        # TODO implement a measure to give each word to "rank" them on the best next guess. the best 4 will be printed as suggested guesses

        # for each guess, show info about which round, how many the list got narrowed down to, the <=4 best possible guesses, the guessed word, and then the result shown in emojis 🟩 🟨 ⬛
        print(f"____________________________\n\n---Guess {guesses}: \n Remaining words = {amount} \n Suggested guesses = 4 BEST SUGGESTED GUESSES HERE")
        for c in result:
            match c:
                case "g":
                    print("🟩", end="")
                case "y":
                    print("🟨", end="")
                case "w":
                    print("⬛", end="")
        print("")

if __name__ == "__main__":
    main()