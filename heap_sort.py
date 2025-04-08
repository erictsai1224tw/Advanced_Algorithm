def heapify(arr, n, i):
    """
    將以 i 為根節點的子樹轉換為最大堆
    
    參數:
    arr -- 輸入數組
    n -- 堆的大小
    i -- 當前子樹的根節點索引
    """
    largest = i  # 初始化最大值為根節點
    left = 2 * i + 1  # 左子節點
    right = 2 * i + 2  # 右子節點
    
    # 如果左子節點存在且大於根節點
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # 如果右子節點存在且大於當前最大值
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # 如果最大值不是根節點，則交換並繼續向下調整
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    堆積排序算法
    
    參數:
    arr -- 待排序的數組
    
    返回:
    排序後的數組
    """
    n = len(arr)
    
    # 建立最大堆（從最後一個非葉節點開始向上調整）
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # 一個一個提取元素
    for i in range(n - 1, 0, -1):
        # 將當前根節點（最大值）移到末尾
        arr[i], arr[0] = arr[0], arr[i]
        # 對剩餘堆進行調整
        heapify(arr, i, 0)
    
    return arr

# 測試代碼
if __name__ == "__main__":
    test_array = [12, 11, 13, 5, 6, 7]
    print("原始數組:", test_array)
    sorted_array = heap_sort(test_array)
    print("排序後數組:", sorted_array)