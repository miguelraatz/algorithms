def find_duplicate(nums):
    if not isinstance(nums, list) or any(
        not isinstance(num, int) or num < 0 for num in nums
    ):
        return False

    nums_sorted = sorted(nums)

    for num in range(1, len(nums_sorted)):
        if nums_sorted[num] == nums_sorted[num - 1]:
            return nums_sorted[num]

    return False
