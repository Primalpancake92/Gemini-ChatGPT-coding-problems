def char_counter(sentence: str): 
    frequency = {}
    new_sentence = sentence.strip().lower()

    for char in new_sentence:
        if char != " ":
            if char in frequency:
                frequency[char] += 1
            else: 
                frequency[char] = 1
            
    return frequency        
            
    
def main(): 
    sentence = "Hello World"
    print(char_counter(sentence))
    

if __name__ == "__main__":
    main()