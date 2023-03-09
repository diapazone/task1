def small(arr): 
    min_ = arr[0]
    for ele in arr:
        if ele < min_:
           min_ = ele
    return min_ 
