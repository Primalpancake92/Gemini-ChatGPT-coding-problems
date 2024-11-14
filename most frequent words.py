def frequent_word(words: list[str]) -> list[str]:
    counted_words = {}
    for word in words:
        if word in counted_words:
            counted_words[word] += 1
        else:
            counted_words[word] = 1
            
    highest_word_count = max(counted_words.values())
    
    most_frequent_words = {word: count for word, count in counted_words.items() if count == highest_word_count}
    
    return most_frequent_words

if __name__ == "__main__":
    words = ["apple", "banana", "apple", "banana", "orange"]
    print(frequent_word(words))