# wordle-assistant
 #### Video Demo: https://youtu.be/OrVwqZirbi8 
 #### Description
![image](https://user-images.githubusercontent.com/111263856/206656463-e0ae4ec5-b768-42aa-9a7d-81dd6cc5caa5.png)

An assistive Wordle solver in Python! Wordle is a game where the user must guess the day's 5 letter word within 6 tries. The game will give information on the guessed letters
depending on certain conditions.
    Gray squares mean that the word will not have that letter anywhere at all
    Yellow squares mean that the word has that letter, but at a different index
    Green squares mean that the word has that letter in that index.
Essentially, this Wordle assistant should be used in tandem with solving the day's Wordle problem. First the user will guess in Wordle, then input that guess into the 
script and the resulting colors. The script will take that information and narrow down the list of possible words based on the information gained. The list of possible words
was gotten through the game's source code and sorted alphabetically. This list can be found in {valid answers.txt}, and is made up of a little more than 2300 words.

After narrowing down the list of possible guesses, the script will return the next best guess. This guess is chosen by a scoring system. 
Said scoring system depends on the frequency that a certain letter appears in each position (1 to 5 => 0 to 4 index). These values are stored in a hashmap/dictionary, where
the keys are each alphabetical letter, and the values are a list of 5 indices. These list values indicate how many times that letter appeared in that position. This frequency
dictionary is then passed into the proper scoring function, which utilizes a max_freq array. The max_freq array shows the highest number for a specific position, meaning if 
many different letters were found to occupy that position, the resulting number in max_freq in that index will be small. On the other hand, if it was found that one or very few
letters occupied that index, then the resulting max_freq for that index will be large.

The resulting best word will have the lowest score, meaning the difference between the max_freq and the word's letter frequency at that index is minimized. This eliminates
the most amount of words from the possible list, and would lead us to the next best guess/answer. In other words, by maximizing similarity, we narrow down our options the most!

TODO: integrate code into an Android mobile app using Android Studio and Java/Kotlin
