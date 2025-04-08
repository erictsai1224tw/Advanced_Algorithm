def quick_sort(arr, low, high):
    def partition(low, high):
        pivot = arr[high]  # 選擇最後一個元素作為樞軸
        i = low - 1  # i 表示小於樞軸的區域邊界
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    if low < high:
        # 找到分割點
        pi = partition(low, high)
        # 遞迴排序左半部分
        quick_sort(arr, low, pi - 1)
        # 遞迴排序右半部分
        quick_sort(arr, pi + 1, high)
    return arr

# 測試程式碼
arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort(arr, 0, len(arr) - 1)
print("排序後的陣列:", arr)