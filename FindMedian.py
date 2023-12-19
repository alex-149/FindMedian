def find_median(nums1, nums2):
    # Combine the two lists and sort them
    merged_nums = sorted(nums1 + nums2)
    
    # Find the middle indices
    middle1 = len(merged_nums) // 2
    middle2 = (len(merged_nums) - 1) // 2
    
    # Calculate the median
    median = (merged_nums[middle1] + merged_nums[middle2]) / 2
    
    return median

# Example usage
result = find_median([1, 3], [2])
print(result)
