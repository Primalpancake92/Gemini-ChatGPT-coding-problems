def sum_even(list):
    total_even = 0
    
    for i in range(len(list)):
        if list[i] % 2 == 0:
            total_even += list[i]
    
    return total_even


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    print(sum_even(numbers))