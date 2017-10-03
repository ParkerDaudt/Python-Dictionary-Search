import nltk
from nltk.corpus import words




start_string = raw_input("Welcome to Dictionary Checker! Would you like to play (Yes/no)?: ")
if start_string == "no":
	print("Goodbye")
while start_string != "no":
	test_string = raw_input("Please enter a string contining two words, with no spaces: ")

	length = len(test_string)

	print("You entered " + test_string)

	if length == 0:
		print("No Words Found, Empty Input")
	
	else:
		a = 1

		while a <= length:
			first_part = test_string[0:a]
			second_part = test_string[a:length]
			if a < length and a != 0:
				if first_part in words.words() and second_part in words.words():
					result = "The two words are " + first_part + " and " + second_part
					print(result)
					start_string = raw_input("Would you like to try again (Yes/no)?: ")
					if start_string == "no":
						print("Goodbye")
						break
					break
	
				else: 
					a = a + 1
			else:
				print("No Words Found")
				start_string = raw_input("Would you like to try again (Yes/no)?: ")
				if start_string == "no":
					print("Goodbye")
					break
				break

