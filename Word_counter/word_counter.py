def word_counter(words: list[str], argument: str):
    count = 0
    for word in words:
        if word == argument:
            count += 1

    return count


def main():
    f = input("Please enter the file name (include the extension): ")
    word_to_find = input("What is the word you would like to find in the file? ")
    
    list_of_words = []
    
    with open(f, "r") as file:
        for line in file:
            line.replace(",", " ").replace("."," ").replace("[", " ").replace("]", " ")
            words = line.split()
            list_of_words.extend(words)
    
    print(word_counter(list_of_words, word_to_find))
            
    
if __name__ == "__main__":
    main()