# Dictionary Checker

The Dictionary Checker is a simple Python program that takes a string containing two concatenated words without spaces and attempts to identify and separate the words.

## Dependencies

- NLTK (Natural Language Toolkit)

## How it works

1. The program first imports the required libraries (`nltk` and `words` corpus from `nltk.corpus`).
2. It then prompts the user to start the game by asking whether they want to play.
3. If the user inputs "no", the program exits, otherwise it continues to the next step.
4. The user is prompted to input a string containing two concatenated words with no spaces.
5. The program then iterates through the input string, dividing it into two parts at each possible position.
6. For each division, the program checks if both parts are valid words using the `words.words()` function from the NLTK library.
7. If a valid pair of words is found, the program prints the separated words and asks the user if they want to try again.
8. If the user inputs "no", the program exits. If no valid pair of words is found, the program informs the user and prompts them to try again.

## Example Usage

```python
Welcome to Dictionary Checker! Would you like to play (Yes/no)?: Yes
Please enter a string containing two words, with no spaces: icecream
You entered icecream
The two words are ice and cream
Would you like to try again (Yes/no)?: no
Goodbye
