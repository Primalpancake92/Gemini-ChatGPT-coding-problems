def palindrome(word: str) -> bool:
    # make the word in lower case
    word = word.lower()
    # declare its reversed version
    reverse_word = ""
    # use a for loop to iterate backwards
    for character in range(len(word) - 1, -1, -1):
        # concatenate each character together
        reverse_word += word[character]
    # now we check if the 'reversed' word is equal to the argument, 'word'     
    if reverse_word == word:
        # if so return True
        return True
    #if not return the opposite
    return False

# the main method, where the code is executed
if __name__ == "__main__":
    # asks for user input
    some_word = input("Enter a word: ")
    # prints out the return statement
    print(palindrome(some_word))