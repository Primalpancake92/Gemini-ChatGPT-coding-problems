def unique_finder(words: list[str]) -> dict[str, list[str]]:
    uniques = {}
    for word in words: 
        uniques[word] = sorted(set(char for char in word))
        
    return uniques


if __name__ == "__main__":
    words = ["apple", "banana", "cherry"]
    print(unique_finder(words))