def second_largest(nums: list[int]) -> int:
    # initialise the max number as 0 first
    max_num = 0
    # find the max through a for loop
    for i in range(len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
   
    nums.remove(max_num) 
    
    second_max = 0
    
    for j in range(len(nums)):
        if nums[j] > second_max:
            second_max = nums[j]

    print(second_max)
    

if __name__ == "__main__":
    second_largest([4, 1, 3, 4, 5, 6])
    print(second_largest([10, 10, 10]))