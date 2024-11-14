def mergery(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    merged = {}
    for key, value in dict1.items():
        merged[key] = value
        
    for k, v in dict2.items():
        merged[k] = v
    
    return merged
                
                
if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"b": 4, "d": 5}
    
    print(mergery(dict1, dict2))