def unique_modifier(nums):
    for num in range(len(nums)):
        nums[num] += 20
        if num == 2:
            nums[num] = 100
        if num == 4:
            nums[num] *= 5
    return nums


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(unique_modifier(numbers))