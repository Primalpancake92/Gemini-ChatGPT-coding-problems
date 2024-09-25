def longest_word(words: str) -> str:
    # split the words in to a list of string objects
    splited = words.split(" ")
    
    # declare the 'longest variable'
    longest = ""
    
    # iterate through these string objects
    for word in splited:
        # find the length of each word
        word_length = len(word)
        # if current word is longer than the 'longest variable'
        if word_length > len(longest):
            longest = word
    
    # return length of word
    return longest
    
    
if __name__ == "__main__":
    sentence = "I am currently doing a degree in software engineering"  
    print(longest_word(sentence))