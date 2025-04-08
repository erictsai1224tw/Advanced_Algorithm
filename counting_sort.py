def counting_sort(arr):
    if not arr:
        return arr
    
    # 步驟 1：找到最小值和最大值
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1
    
    # 步驟 2：創建計數數組並統計次數
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    
    # 步驟 3：生成排序結果
    sorted_arr = []
    for i in range(range_size):
        sorted_arr.extend([i + min_val] * count[i])
    
    return sorted_arr

# 測試
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)  # 輸出: [1, 2, 2, 3, 3, 4, 8]