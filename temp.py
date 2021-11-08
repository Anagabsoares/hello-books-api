def getPairsCount(list_number: list[int], target_sum_value:int) -> int:
    if not list_number:
        return False 
    freq_map = {}
    count = 0
    for item  in range(len(list_number)):
        match_pair = target_sum_value - list_number[item] 
        if match_pair in freq_map:
            count += freq_map[match_pair] 
        # handle duplicates 
        if list_number[item] in freq_map:
            freq_map[list_number[item]] += 1
        else:
            freq_map[list_number[item]] = 1
    return count
# Driver function
arr = [1,3,4,3]
target_sum_value = 44

print(getPairsCount(arr, target_sum_value))
