def unusual_traversal(array):
    # TODO: implement this function
    length = len(array)
    mid = length // 2
    
    left = mid - 1
    right = mid + 1
    result = [array[mid]]
        
    while left >= 0 and right < length:
        if left > 0:
            result.append(array[left - 1])
        result.append(array[left])
        result.append(array[right])
        if right < length - 1:
            result.append(array[right + 1])
        left -= 2
        right += 2
        
    return result