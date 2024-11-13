def counter(sentence: str):
    words = sentence.lower().split(" ")
    counted = {}
    for word in words:
        if word in counted:
            counted[word] += 1
        else:
            counted[word] = 1
    
    return counted
    
sentence = "Hello world hello"

print(counter(sentence))